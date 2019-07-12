from gpiozero import LED, Button
from signal import pause

led = LED(18)
button = Button(2)

def when_pressed():
    print("pressed")
    
    
def when_released():
    print("released")
    


button.when_pressed = led.on
button.when_released = led.off

pause()
