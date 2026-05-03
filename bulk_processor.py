import os
import shutil
import logging
import time
import argparse
from PIL import Image, ImageDraw, ImageFont

# लॉगिंग सेटअप
logging.basicConfig(
    filename='image_processing.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# त्रुटि लॉगिंग सेटअप
error_logging = logging.getLogger('error_logger')
error_logging.setLevel(logging.ERROR)
error_handler = logging.FileHandler('error_log.txt')
error_handler.setLevel(logging.ERROR)
error_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
error_handler.setFormatter(error_formatter)
error_logging.addHandler(error_handler)

# फ़ंक्शन: फ़ाइल का आकार बदलना
def resize_image(image_path, output_path, width=800, height=600):
    try:
        with Image.open(image_path) as img:
            img = img.resize((width, height), Image.ANTIALIAS)
            img.save(output_path)
            logging.info(f"Resized {image_path} to {output_path}")
    except Exception as e:
        error_logging.error(f"Error resizing {image_path}: {e}")

# फ़ंक्शन: छवि का क्रॉप करना
def crop_image(image_path, output_path):
    try:
        with Image.open(image_path) as img:
            width, height = img.size
            
            # खाली किनारों और कोनों की जाँच करें
            if width == 0 or height == 0:
                error_logging.error(f"Image {image_path} is empty")
                return
                
            # खाली बाएँ और ऊपरी किनारों को हटा दें
            if width <= 10:
                img = img.crop((10, 10, width-10, height-10))
            elif height <= 10:
                img = img.crop((10, 10, width-10, height-10))
            
            # खाली निचले किनारों को हटा दें
            if width <= 10:
                img = img.crop((10, 10, width-10, height-10))
            elif height <= 10:
                img = img.crop((10, 10, width-10, height-10))
            
            # खाली ऊपरी और निचले कोनों को हटा दें
            if width <= 10:
                img = img.crop((10, 10, width-10, height-10))
            elif height <= 10:
                img = img.crop((10, 10, width-10, height-10))
            
            # खाली कोनों और किनारों की जाँच करें
            if width <= 10 or height <= 10:
                error_logging.error(f"Image {image_path} has no valid area for cropping")
                return
                
            # छवि को क्रॉप करके नए कैनवास पर स्थानांतरित करें
            cropped_img = img.crop((10, 10, width-10, height-10))
            cropped_img.save(output_path)
            logging.info(f"Clipped {image_path} to {output_path}")
    except Exception as e:
        error_logging.error(f"Error cropping {image_path}: {e}")

# फ़ंक्शन: वॉटरमार्क जोड़ना
def add_watermark(image_path, output_path, watermark_text="My Watermark", font_size=30, font_color=(255, 255, 255)):
    try:
        with Image.open(image_path) as img:
            width, height = img.size
            
            # वॉटरमार्क टेक्स्ट का आकार और स्थान निर्धारित करें
            font = ImageFont.load_default()
            text_bbox = font.getbbox(watermark_text, (0, 0))
            text_width = text_bbox[2] - text_bbox[0]
            text_height = text_bbox[3] - text_bbox[1]
            
            # यदि छवि बहुत छोटी है, तो टेक्स्ट को ऊपर की ओर स्थानांतरित करें
            if height < 200:
                x = width // 2 - text_width // 2
                y = height // 2 - text_height // 2 - 50
            else:
                # यदि छवि बहुत बड़ी है, तो टेक्स्ट को नीचे की ओर स्थानांतरित करें
                x = width // 2 - text_width // 2
                y = height - 100
            
            # वॉटरमार्क को छवि के नीचे के निचले हिस्से में जोड़ें
            watermark = Image.new('RGBA', img.size, (0, 0, 0, 0))
            draw = ImageDraw.Draw(watermark)
            draw.text((x, y), watermark_text, font=font, fill=font_color)
            
            # वॉटरमार्क को मूल छवि पर परत करें
            watermarked_img = Image.alpha_composite(img, watermark)
            watermarked_img.save(output_path)
            logging.info(f"Added watermark to {image_path} to {output_path}")
    except Exception as e:
        error_logging.error(f"Error adding watermark to {image_path}: {e}")

# फ़ंक्शन: छवि को प्रोसेस करना
def process_image(image_path, output_dir, output_file):
    try:
        input_path = os.path.join(image_path, image_file)
        output_path = os.path.join(output_dir, output_file)
        
        # पहले आकार बदलने की कोशिश करें
        resize_image(input_path, output_path)
        
        # फिर क्रॉप करने की कोशिश करें
        crop_image(output_path, output_path)
        
        # फिर वॉटरमार्क जोड़ने की कोशिश करें
        add_watermark(output_path, output_path)
        
    except Exception as e:
        error_logging.error(f"Error processing {image_path}: {e}")

# फ़ंक्शन: अद्वितीय छवियों की पहचान करना
def get_unique_files(directory):
    unique_files = set()
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path):
                size = os.path.getsize(file_path)
                modification_time = os.path.getmtime(file_path)
                unique_files.add((file_path, size, modification_time))
    return list(unique_files)

# फ़ंक्शन: निर्देशिकाओं को स्कैन करके छवियों का प्रोसेसिंग करना
def process_images(input_directory, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    unique_files = get_unique_files(input_directory)
    
    if not unique_files:
        logging.info("No unique files found in the specified directory.")
        return
    
    for file_path, size, modification_time in unique_files:
        # फ़ाइल नाम से एक अद्वितीय नाम निकालें
        file_name = os.path.basename(file_path)
        unique_file_name = os.path.splitext(file_name)[0]
        output_file = f"{unique_file_name}_processed.{os.path.splitext(file_name)[1]}"
        
        # प्रक्रिया फ़ंक्शन को कॉल करें
        process_image(file_path, output_directory, output_file)

# मुख्य फ़ंक्शन
def main():
    parser = argparse.ArgumentParser(description='Bulk image processing tool')
    parser.add_argument('input_directory', help='Input directory containing images')
    parser.add_argument('output_directory', help='Output directory for processed images')
    args = parser.parse_args()
    
    process_images(args.input_directory, args.output_directory)

if __name__ == '__main__':
    main()
