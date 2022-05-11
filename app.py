from io import BytesIO
from barcode import Gs1_128
from barcode.writer import ImageWriter
from PIL import Image, ImageDraw

options = {
    'font_size': 5,
    'dpi': 300,
    'module_height': 4,
    'text_distance': 1,
    }

with open('dcode.jpeg', 'wb') as f:
    Gs1_128(str('231'), writer=ImageWriter()).write(f,options)

def add_margin(pil_img, top, right, bottom, left, color):
    width, height = pil_img.size
    new_width = width + right + left
    new_height = height + top + bottom
    result = Image.new(pil_img.mode, (new_width, new_height), color)
    result.paste(pil_img, (left, top))
    return result

img = Image.open('dcode.jpeg')
img = add_margin(img, 24, 5, 5, 5, "#fff")
I1 = ImageDraw.Draw(img)
I1.text((35,2),"\nEjemplo de nombre de producto \n\n\n\n\n\nCodigo intero", fill="black",align="center")
img.save("dcode.jpeg")
img.show()