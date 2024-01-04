# -*- coding: utf-8 -*- #

# -----------------------------
# Topic: cognite images and translate
# Created: 2024.01.02
# History:
# <version>    <time>        <desc>
# v0.1      2024/01/02    basic build success
# -----------------------------

from pynput import keyboard


class Classify():
    def __init__(self):
        self.on_init()
    
    def on_init(self):
        self.ocr = PaddleOCR(lang="ch", use_gpu="false", use_angle_cls="false")
    
    def ima_to_str(self, ima: str):
        result = self.ocr.ocr(ima, cls=True)
        

if __name__ == "__main__":
    ins = Classify()
    
    # imas = ['./temp/梦幻西游_screenshot5.png',
    #        './temp/梦幻西游_screenshot6.png']
    # for ima in imas:
    #     ins.ima_to_str(ima)