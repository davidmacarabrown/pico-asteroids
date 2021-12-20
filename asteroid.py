import framebuf
import random

class Asteroid:
    
    def __init__(self):
        self.pos_x = random.randrange(1, 128)
        self.pos_y = random.randrange(-65, -5)
        self.width = 5
        self.height = 5
        
        with open(f"/img/asteroid.pbm", "rb") as image:
            image.readline()
            image.readline()
            image.readline()
            img = bytearray(image.read())
            
        self.fbuf = framebuf.FrameBuffer(img, self.width, self.height, framebuf.MONO_HLSB)