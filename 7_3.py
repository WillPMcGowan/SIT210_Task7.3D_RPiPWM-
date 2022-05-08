import time
from gpiozero import DistanceSensor
from gpiozero import PWMLED
import RPi.GPIO 
from signal import signal, pause 
# assign led to pwm pin 18
led = PWMLED(18)
sensor = DistanceSensor(echo=24, trigger=23 )

def main():
    while True:   
        led.on()
        distance = sensor.value
        # print the distance in CM
        print("distance:", format(distance * 100, ".0f"), "CM")
        # reverse the distance to make LED brighter instead of darker
        d = round(1.0 - distance,1)           
        # change led intensity
        led.value = d
        time.sleep(0.1)

if __name__ == "__main__":
    try:
        main()
    except:
        pass
    finally:
        # cleanly exit
        RPi.GPIO.cleanup()
