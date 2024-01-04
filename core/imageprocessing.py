# -*- coding: utf-8 -*- #

# -----------------------------
# Topic: cognite images and translate
# Created: 2024.01.02
# History:
# <version>    <time>        <desc>
# v0.1      2024/01/02    basic build success
# -----------------------------

from paddleocr import PaddleOCR

import cv2


class ImageProcessing():
    def __init__(self):
        self.on_init()
    
    def on_init(self):
        self.ocr = PaddleOCR(lang="ch", use_gpu="false", use_angle_cls="false")
    
    def ima_to_str(self, ima: str):
        result = self.ocr.ocr(ima, cls=True)
    
    def find_package(self, tem: str, tar: str):
        template = cv2.imread(tem, cv2.IMREAD_GRAYSCALE)
        target = cv2.imread(tar, cv2.IMREAD_GRAYSCALE)

        # compare with template image
        result = cv2.matchTemplate(target, template, cv2.TM_CCOEFF_NORMED)
        _, _, _, max_loc = cv2.minMaxLoc(result)

        # cutting the target image
        h, w = template.shape
        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        segmented = target[top_left[1]: bottom_right[1],
                           top_left[0]: bottom_right[0]]
        # cv2.imshow('Segmented Block', segmented)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

if __name__ == "__main__":
    ins = ImageProcessing()
    
    # imas = ['./temp/梦幻西游_screenshot5.png',
    #        './temp/梦幻西游_screenshot6.png']
    # for ima in imas:
    #     ins.ima_to_str(ima)
    
    tem = './resources/package_v.jpg'
    tar = './temp/mhxy_screenshot7.jpg'
    
    ins.find_package(tem, tar)