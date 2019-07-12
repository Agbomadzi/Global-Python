from gpiozero import LED
from time import sleep

led = LED(18)
led1 = LED(17)
led2 = LED(22)
led3 = LED(27)

while True:
    led.on()
    sleep(0.04)
    led.off()
    sleep(0.04)
    
    led2.on()
    sleep(0.04)
    led2.off()
    sleep(0.04)
    
    led1.on()
    sleep(0.04)
    led1.off()
    sleep(0.04)
    
    led3.on()
    sleep(0.04)
    led3.off()
    sleep(0.04)