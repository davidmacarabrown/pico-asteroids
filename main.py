from machine import Pin
import time
import framebuf
from ship import Ship
from display import Display
from asteroid import Asteroid
from star import Star
import gc

left = machine.Pin(28, machine.Pin.IN) #A2
right = machine.Pin(27, machine.Pin.IN) #A1
start = machine.Pin(26, machine.Pin.IN) #A0


running = False
display = Display()

def start_reset(pin):
    time.sleep(0.1)
    if start.value():
        global running
        running = True
        pin.irq(handler= None)

def game():
    
    ship = Ship()
    stars = []
    asteroids = []
    
    global running
    count = 0
    
    while running == True:
        
        display.clear()
        
        if len(stars) < 50:
            new_star = Star()
            stars.append(new_star)
            
        if len(asteroids) < 5:
            new_asteroid = Asteroid()
            asteroids.append(new_asteroid)
        
        display.render(ship.fbuf, ship.pos_x, ship.pos_y)
        
        s = 0
        clear_stars = []
        for star in stars:
            display.oled.pixel(star.pos_x, star.pos_y, 1)
            if star.pos_y > 64:
                clear_stars.append(s)
            s += 1
        
        a = 0
        clear_asteroids = []
        for asteroid in asteroids:
            if asteroid.pos_y > 15:
                display.render(asteroid.fbuf, asteroid.pos_x, asteroid.pos_y)
            if asteroid.pos_y > 70:
                clear_asteroids.append(a)
            a += 1
            
        display.text(str(count), 0, 0)
        
        if left.value() == 1:
            ship.move_left()
        if right.value() == 1:
            ship.move_right()
        
        for star in stars:
            star.pos_y += 1 
            display.oled.pixel(star.pos_x, star.pos_y, 1)
            
        for index in clear_stars:
            stars.pop(index)
        
        for index in clear_asteroids:
            asteroids.pop(index)
            
        for asteroid in asteroids:
            if asteroid.pos_y in range(54, 64, 1) and (asteroid.pos_x + 2) in range(ship.pos_x, ship.pos_x + 10, 1):
                display.clear()
                display.text("Game Over", 0, 16)
                display.text("Press Start To", 0, 24)
                display.text("Play Again", 0, 32)
                display.show()
                start.irq(handler=start_reset)
                running = False
                return
                
            if count %4 == 0:
                asteroid.pos_y += 1
        
        display.render(ship.fbuf, ship.pos_x, ship.pos_y)
        
        display.show()
        count += 1


def main():
    display.clear()
    start.irq(trigger=Pin.IRQ_RISING, handler=start_reset)
    display.text("Press Start...", 0, 28)
    display.show()
    
    while True:
        global running
            
        if running:
            game()
                         
if __name__ == "__main__":
    gc.enable()
    main()


