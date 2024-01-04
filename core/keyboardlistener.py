# -*- coding: utf-8 -*- #

# -----------------------------
# Topic: keyboard listener
# Created: 2024.01.04
# History:
# <version>    <time>        <desc>
# v0.1      2024/01/04    basic build success
# -----------------------------

import keyboard


class KeyboardListener():
    def __init__(self):
        self.key_combination =('alt', 'e')
        self.current_keys = set()
        
        self.on_init()
        
    def on_init(self):
        keyboard.add_hotkey(self.key_combination, self.cognition_alte)
    
    def on_start(self):
        try:
            keyboard.wait()
        except KeyboardInterrupt:
            self.on_end()
    
    def on_end(self):
        keyboard.unhook_all()
    
    def cognition_alte(self):
        # ATTENTION: to run when mhxy is the active process.
        print('alt + e')
        
        
if __name__ == "__main__":
    ins = KeyboardListener()

    ins.on_start()