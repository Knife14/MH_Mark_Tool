# -*- coding: utf-8 -*- #

# -----------------------------
# Topic: classify Chinese simplified
# Created: 2024.01.02
# History:
# <version>    <time>        <desc>
# v0.1      2024/01/02    basic build success
# -----------------------------

from paddleocr import PaddleOCR, draw_ocr
from PIL import Image

import datetime


class Classify():
    def __init__(self):
        self.on_init()
    
    def on_init(self):
        self.ocr = PaddleOCR(lang="ch", use_gpu="false", use_angle_cls="false")
    
    def ima_to_str(self, ima):
        
        print('start:', datetime.datetime.now())
        result = self.ocr.ocr(ima, cls=True)
        for idx in range(len(result)):
            res = result[idx]
            for line in res:
                print(line)
        print('end:', datetime.datetime.now())
        

if __name__ == "__main__":
    imas = ['./temp/梦幻西游_screenshot5.png',
           './temp/梦幻西游_screenshot6.png']
    
    ins = Classify()
    for ima in imas:
        ins.ima_to_str(ima)