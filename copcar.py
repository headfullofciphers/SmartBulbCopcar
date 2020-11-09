from yeelight import Bulb
from time import sleep
import vlc
import os

os.environ["VLC_VERBOSE"] = str("-1")

interval = 0.5
file = 'police2.wav'
sleep(3)
print("RUN!")
player = vlc.MediaPlayer(file)
bulbR = Bulb("192.168.0.157")
bulbL = Bulb("192.168.0.45")
sleep(2)

bulbR.turn_on()
bulbL.turn_on()

print("FREEZE!\n\n")
sleep(1)
print("Put your hand's in the air!\n")

for i in range(0,4):
    
    player.play()
    
    bulbL.set_rgb(0, 0, 255)
    bulbR.set_rgb(255, 0, 0)
    
    bulbL.set_brightness(0)
    bulbR.set_brightness(100)

    sleep(interval)
    
    bulbR.set_brightness(0)
    bulbL.set_brightness(100)
    
    bulbR.set_rgb(0, 0, 255)
    
    sleep(interval)
    
    bulbL.set_rgb(255, 0, 0)

    bulbL.set_brightness(0)
    bulbR.set_brightness(100)
    
    sleep(interval)
    
    bulbR.set_brightness(0)
    bulbL.set_brightness(100)
    
    
    sleep(interval)
    player.stop()

    print(f"***Siren {i+1}***")

print("\nBUSTED")
bulbR.turn_off()
bulbL.turn_off()
