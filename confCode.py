from barcode import Gs1_128
from barcode.writer import ImageWriter
from PIL import Image, ImageDraw
import random
import win32print
import win32ui
from PIL import Image, ImageWin

options = {
    'font_size': 5,
    'dpi': 300,
    'module_height': 4,
    'text_distance': 1,
    }

def add_margin(pil_img, top, right, bottom, left, color):
    width, height = pil_img.size
    new_width = width + right + left
    new_height = height + top + bottom
    result = Image.new(pil_img.mode, (new_width, new_height), color)
    result.paste(pil_img, (left, top))
    return result

def print_code(file_name):
    HORZRES = 100
    VERTRES = 50
    LOGPIXELSX = 88
    LOGPIXELSY = 90

    PHYSICALWIDTH = 110
    PHYSICALHEIGHT = 700

    PHYSICALOFFSETX = 300
    PHYSICALOFFSETY =700

    printer_name = win32print.GetDefaultPrinter ()

    hDC = win32ui.CreateDC()
    hDC.CreatePrinterDC(printer_name)
    printable_area = hDC.GetDeviceCaps(HORZRES), hDC.GetDeviceCaps (VERTRES)
    printer_size = hDC.GetDeviceCaps (PHYSICALWIDTH), hDC.GetDeviceCaps (PHYSICALHEIGHT)
    printer_margins = hDC.GetDeviceCaps (PHYSICALOFFSETX), hDC.GetDeviceCaps (PHYSICALOFFSETY)

    bmp = Image.open (file_name)
    # if bmp.size[0] > bmp.size[1]:
    #     bmp = bmp.rotate (90)

    ratios = [1.0 * printable_area[0] / bmp.size[0], 1.0 * printable_area[1] / bmp.size[1]]
    scale = min (ratios)

    hDC.StartDoc (file_name)
    hDC.StartPage ()

    dib = ImageWin.Dib (bmp)
    scaled_width, scaled_height = [int (scale * i) for i in bmp.size]
    x1 = int ((printer_size[0] - scaled_width) / 2)
    y1 = int ((printer_size[1] - scaled_height) / 2)
    x2 = x1 + scaled_width
    y2 = y1 + scaled_height

    print(x1, y1, x2, y2)
    dib.draw(hDC.GetHandleOutput(), (1, 10, 1024, 400))

    hDC.EndPage()
    hDC.EndDoc()
    hDC.DeleteDC()
    # os.remove(file_name)

class create_code_bar:
    def __init__(self,codebar,internalCode,productName):
        nameRandom = str(random.randint(1, 99999999999))
        with open(nameRandom+'.jpg', 'wb') as f:
            Gs1_128(str(codebar), writer=ImageWriter()).write(f,options)

        img = Image.open(nameRandom+'.jpg')
        img = add_margin(img, 24, 5, 5, 5, "#fff")
        I1 = ImageDraw.Draw(img)
        I1.text((35,2),productName+'\n', fill="black",align="center")
        I1.text((35,100),internalCode+'\n', fill="black",align="center")
        img.save(nameRandom+".jpg")
        # img.show()
        print_code(nameRandom+".jpg")
        

