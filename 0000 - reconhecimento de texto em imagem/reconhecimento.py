# Important: pytesseract must be installed in your wheel (PIP),
# as well be installed into your file programs from OS
# 
# https://github.com/tesseract-ocr/tesseract/wiki
#

import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'tesseract_path/tesseract.exe'
try:
    from PIL import Image
except ImportError:
    import Image


def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    text = pytesseract.image_to_string(Image.open(filename))
    # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text

print(ocr_core('file_path/image.JPG',))