import os
import logging
import shutil
import argparse
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from PIL.ExifTags import TAGS

# कॉन्फ़िगरेशन
INPUT_DIR = "images"
OUTPUT_DIR = "processed_images"
WATERMARK_FILE = "watermark.png"
LOG_FILE = "process_log.txt"
DUPLICATE_THRESHOLD = 100

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler(LOG_FILE, encoding='utf-8'), logging.StreamHandler()]
)

def get_image_path(directory, filename):
    return Path(directory) / filename

def is_valid_image(path):
    return path.exists() and path.suffix.lower() in ('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.webp')

def add_watermark(image_path, watermark_path, output_path, text):
    try:
        with Image.open(watermark_path) as wm:
            wm = wm.resize((output_path.width, output_path.height))
            overlay = Image.new('RGBA', output_path.size, (0, 0, 0, 0))
            overlay.paste(wm, ((output_path.width - wm.size[0]) // 2, (output_path.height - wm.size[1]) // 2))
            result = Image.alpha_composite(image_path.convert('RGBA'), overlay)
            return result
    except Exception as e:
        logging.error(f"Watermark failed: {e}")
        return image_path

def process_images(input_dir, output_dir, watermark_path):
    input_path = get_image_path(input_dir, "input.txt")
    if not input_path.exists():
        logging.error("Input file 'input.txt' not found.")
        return

    try:
        with open(input_path, 'r') as f: filenames = [f.strip() for f in f if f.strip()]
    except Exception as e: logging.error(f"Input file error: {e}")
        return

    files = []
    seen = set()
    for name in filenames:
        path = get_image_path(input_dir, name)
        if is_valid_image(path):
            if name not in seen:
                seen.add(name)
                files.append(path)

    if not files:
        logging.info("No valid images found.")
        return

    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(os.path.dirname(watermark_path), exist_ok=True)

    font = None
    try:
        with open(watermark_path, 'r') as f: font = ImageFont.truetype(f.read(), 40)
    except FileNotFoundError:
        logging.warning("Watermark font not found. Using default.")
        font = None

    for i, path in enumerate(files, 1):
        try:
            name = path.name
            temp_path = Path(output_dir) / f"{name}_tmp.jpg"
            with Image.open(path) as img:
                img = img.convert('RGB')
                if img.size[0] <= 100 or img.size[1] <= 100:
                    logging.warning(f"Skipping small image: {name}")
                    continue

                result = add_watermark(path, watermark_path, temp_path, f"Photo by {Path.home()}") if font else img
                result.save(temp_path, "JPEG")
                shutil.move(temp_path, Path(output_dir) / name)
                logging.info(f"Processed: {name}")
        except Exception as e:
            logging.error(f"Error processing {name}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Image Processor")
    parser.add_argument("--input", type=str, default=INPUT_DIR, help="Input directory")
    parser.add_argument("--output", type=str, default=OUTPUT_DIR, help="Output directory")
    parser.add_argument("--watermark", type=str, default=WATERMARK_FILE, help="Watermark file")
    args = parser.parse_args()

    if not os.path.exists(args.input):
        logging.error("Input directory not found.")
        exit(1)

    logging.info(f"Starting processing: {args.input} -> {args.output}")
    process_images(args.input, args.output, args.watermark)
    logging.info("Processing completed.")
