# -*- coding: utf-8 -*- #

# -----------------------------
# Topic: screen shot on an application
# Created: 2024.01.01
# History:
# <version>    <time>        <desc>
# v0.1      2024/01/01    basic build success
# -----------------------------

import pyautogui
import pygetwindow


def window_screenshot(window_title):
    # ATTENTION: to need to change the condition of while
    while True:
        windows = pygetwindow.getAllWindows()

        if target_window := next(
            (window for window in windows if window_title in window.title and window == pygetwindow.getActiveWindow()), 
            None):
            left, top, width, height = \
                target_window.left, target_window.top, target_window.width, target_window.height
            screenshot = pyautogui.screenshot(region=(left, top, width, height))
            
            # ATTENTION: to need to change route !
            screenshot.save(f"./temp/{window_title}_screenshot.png")
            break


if __name__ == '__main__':
    target_window_title = "Chrome"
    
    window_screenshot(target_window_title)
