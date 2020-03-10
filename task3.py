# sudo apt-get install tesseract-ocr
# pip install pytesseract
import pytesseract
config = ("-l eng --oem 1 --psm 3")
text = pytesseract.image_to_string('TASK2.png', config=config)
print(text)
