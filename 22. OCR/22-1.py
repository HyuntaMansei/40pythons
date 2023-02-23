from PIL import Image
import pytesseract

image = r'C:\Users\jchoi\Documents\40 pythons\22. OCR\imagetoocr.png'
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

text = pytesseract.pytesseract.image_to_string(Image.open(image), lang='kor+eng')

# print(text)

with open(r'C:\Users\jchoi\Documents\40 pythons\22. OCR\textbyocr.txt', 'w') as f:
    f.write(text)

