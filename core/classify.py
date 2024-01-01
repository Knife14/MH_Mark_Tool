# -*- coding: utf-8 -*- #

# -----------------------------
# Topic: classify Chinese simplified
# Created: 2024.01.02
# History:
# <version>    <time>        <desc>
# v0.1      2024/01/02    basic build success
# -----------------------------

import pytesseract
from PIL import Image


class Classify():
    def __init__(self):
        self.on_init()
    
    def on_init(self):
        pytesseract.pytesseract.tesseract_cmd = r"./tools/ocr/tesseract.exe"
    
    def ima_to_str(self, ima):
        result = pytesseract.image_to_string(ima, lang='chi_sim')

        print(result)
        

if __name__ == "__main__":
    image = Image.open('./temp/梦幻西游_screenshot1.png')
    
    ins = Classify()
    ins.ima_to_str(image)