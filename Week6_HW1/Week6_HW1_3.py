import RPi.GPIO as GPIO
import time

SW1 = 5
SW2 = 6
SW3 = 13
SW4 = 19

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(SW1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

prev_SW1Value = 0
prev_SW2Value = 0
prev_SW3Value = 0
prev_SW4Value = 0

try:
    while True:
        SW1Value = GPIO.input(SW1)
        SW2Value = GPIO.input(SW2)
        SW3Value = GPIO.input(SW3)
        SW4Value = GPIO.input(SW4)

        if SW1Value == 1 and prev_SW1Value == 0:
            print('Click1')
        if SW2Value == 1 and prev_SW2Value == 0:
            print('Click2')
        if SW3Value == 1 and prev_SW3Value == 0:
            print('Click3')
        if SW4Value == 1 and prev_SW4Value == 0:
            print('Click4')

        prev_SW1Value = SW1Value
        prev_SW2Value = SW2Value
        prev_SW3Value = SW3Value
        prev_SW4Value = SW4Value

        time.sleep(0.1)

except KeyboardInterrupt:
    pass

GPIO.cleanup()
