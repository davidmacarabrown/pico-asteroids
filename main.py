from machine import Pin
from time import sleep
import framebuf
from ship import Ship
from display import Display
from star import Star
import gc

left = machine.Pin(29, machine.Pin.IN)
right = machine.Pin(28, machine.Pin.IN)
shield = machine.Pin(27, machine.Pin.IN)


def main():
    display = Display()

    ship = Ship()
    stars = []
    
    for n in range(1, 10):
        new_star = Star()
        stars.append(new_star)
    
    display.render(ship.fbuf, ship.pos_x, ship.pos_y)
    for star in stars:
            display.oled.pixel(star.pos_x, star.pos_y, 1)
            
    display.show()
    
    count = 0
    
    while True:
        
        display.clear()
        display.text(str(count), 0, 0)
        count += 1
        
        if left.value() == 1:
            ship.move_left()
        if right.value() == 1:
            ship.move_right()
        
        for star in stars:
            star.pos_y += 1 
            display.oled.pixel(star.pos_x, star.pos_y, 1)
        
        display.render(ship.fbuf, ship.pos_x, ship.pos_y)
        
        display.show()
        
        sleep(0.01)

        
if __name__ == "__main__":
    gc.enable()
    main()