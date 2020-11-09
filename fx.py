import pytesseract

from PIL import Image

im = Image.open("20201022153443.jpg")

text = pytesseract.image_to_string(im,lang='fx',config= ' --psm 7')

print(text)

