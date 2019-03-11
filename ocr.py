try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

 #tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract"

print(pytesseract.image_to_string(Image.open("goldLimit.PNG")))