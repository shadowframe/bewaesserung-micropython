from dcmotor import DCMotor
from machine import Pin, PWM
from time import sleep

frequency = 500
pin1 = Pin(12, Pin.OUT)
pin2 = Pin(11, Pin.OUT)
enable = PWM(Pin(10))
enable.freq(frequency)
# dc_motor = DCMotor(pin1, pin2, enable)
dc_motor = DCMotor(pin1, pin2, enable, 50000, 65535)
dc_motor.forward(100)
sleep(10)
dc_motor.stop()
sleep(10)
dc_motor.backwards(100)
sleep(10)
dc_motor.forward(60)
sleep(10)
dc_motor.stop()
