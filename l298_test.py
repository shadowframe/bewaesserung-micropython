from l298 import DCMotor
from machine import Pin, PWM
import time

# motor left
frequency = 500
pin1 = Pin(12, Pin.OUT)
pin2 = Pin(11, Pin.OUT)
enable_l = PWM(Pin(10))

# motor right
pin3 = Pin(7, Pin.OUT)
pin4 = Pin(8, Pin.OUT)
enable_r = PWM(Pin(9))

enable_r.freq(500)
enable_l.freq(500)
dc_motor = DCMotor(pin1, pin2, pin3, pin4, enable_l, enable_r, 40000, 65535)

for i in range(0, 3):
    print(i)

    dc_motor.forward(90)  # motor is running
    print("forward")
    time.sleep(2)

    dc_motor.stop()  # stops motor
    time.sleep(1)

    dc_motor.backwards(100)  # the motor turns in the opposite direction
    time.sleep(1)

    dc_motor.stop()  # stops motor
    time.sleep(1)

    print("left")
    dc_motor.left(100)
    time.sleep(0.5)

    dc_motor.stop()
    time.sleep(1)

    print("right")
    dc_motor.right(100)
    time.sleep(0.5)

    dc_motor.stop()
    time.sleep(1)
