from ssd1306 import SSD1306_I2C
from machine import Pin, I2C

class Display:
    
    def __init__(self):
        self.oled = SSD1306_I2C(128, 64, I2C(1, sda=Pin(6), scl=Pin(7)))
    
    def clear(self):
        self.oled.fill_rect(0,0,128,64,0)
        
    def render(self, fbuf, x, y):
        self.oled.blit(fbuf, x, y)
        
    def show(self):
        self.oled.show()
    
    def text(self, string, x, y):
        self.oled.text(string, x, y)