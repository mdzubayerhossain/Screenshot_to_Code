import base64
import pytesseract
from PIL import Image
import io
import logging

# Configure Tesseract path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

logger = logging.getLogger(__name__)

def extract_text_from_image(image_data):
    """Process base64 image data and extract text using Tesseract OCR"""
    try:
        if not image_data:
            raise ValueError("Empty image data received")
            
        # Handle data URL format
        if ',' in image_data:
            image_data = image_data.split(',')[1]
            
        image_bytes = base64.b64decode(image_data)
        image = Image.open(io.BytesIO(image_bytes))
        
        if image.mode != 'RGB':
            image = image.convert('RGB')
            
        text = pytesseract.image_to_string(image)
        return text.strip()
        
    except Exception as e:
        logger.error(f"OCR failed: {str(e)}")
        raise Exception(f"OCR Error: {str(e)}")