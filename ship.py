import framebuf

class Ship():
    
    def __init__(self):
        self.width = 10
        self.height = 10
        self.pos_x = 60
        self.pos_y = 54
        self.fbuf = None
        
        with open(f"/img/ship.pbm", "rb") as image:
            image.readline()
            image.readline()
            image.readline()
            img = bytearray(image.read())
            
        self.fbuf = framebuf.FrameBuffer(img, self.width, self.height, framebuf.MONO_HLSB)
        
    def move_right(self):
        if self.pos_x < 110:
            self.pos_x += 1
            
    def move_left(self):
        if self.pos_x > 0:
            self.pos_x -= 1