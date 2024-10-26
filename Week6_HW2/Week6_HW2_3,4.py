import RPi.GPIO as GPIO
import time

BUZZER = 12
SW1 = 5
SW2 = 6
SW3 = 13
SW4 = 19

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER, GPIO.OUT)
GPIO.setup(SW1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

p = GPIO.PWM(BUZZER, 261)
p.start(50)

try :
    while True :
        sw1Value = GPIO.input(SW1)
        sw2Value = GPIO.input(SW2)
        sw3Value = GPIO.input(SW3)
        sw4Value = GPIO.input(SW4)
        p.start(50)

        if sw1Value == 1 :
            p.ChangeFrequency(262)
            time.sleep(1.0)
        if sw2Value == 1 :
            p.ChangeFrequency(294)
            time.sleep(1.0)
        if sw3Value == 1 :
            p.ChangeFrequency(330)
            time.sleep(1.0)
        if sw4Value == 1 :
            p.ChangeFrequency(349)
            time.sleep(1.0)
        p.stop()
        time.sleep(1.0)

except KeyboardInterrupt :
    pass

p.stop()
GPIO.cleanup()