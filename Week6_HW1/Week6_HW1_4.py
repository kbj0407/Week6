import RPi.GPIO as GPIO
import time

SW1 = 5
SW2 = 6
SW3 = 13
SW4 = 19

click_count = [0, 0, 0, 0]

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(SW1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
        sw1Value = GPIO.input(SW1)
        sw2Value = GPIO.input(SW2)
        sw3Value = GPIO.input(SW3)
        sw4Value = GPIO.input(SW4)


        if sw1Value == 1:
            click_count[0] = click_count[0] + 1
            print('SW1 click', click_count[0])  
        if sw2Value == 1:
            click_count[1] = click_count[1] + 1
            print('SW2 click', click_count[1])
        if sw3Value == 1:       
            click_count[2] = click_count[2] + 1
            print('SW3 click', click_count[2])
        if sw4Value == 1:
            click_count[3] = click_count[3] + 1
            print('SW4 click', click_count[3])

        time.sleep(0.1)

except KeyboardInterrupt:
    pass

GPIO.cleanup()
