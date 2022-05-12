import random

from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time

# Es wird I2C 0 verwendet Pin (GP0) und Pin (GP1)
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=40000)
oled = SSD1306_I2C(128, 64, i2c)

menu_list = ['sensoren',
             'sensor 1',
             'sensor 2',
             'sensor 3',
             'sensor 4',
             'sensor 5',
             'sensor 6'
             ]
sensor_1 = 40
sensor_2 = 30
sensor_3 = 10
sensor_4 = 50


def sensor_overview():
    # SENSOREN ÜBERSICHT
    for a in range(0, 110, 1):
        oled.fill(0)

        oled.fill_rect(0, 0, 128, 20, 1)
        oled.rect(0, 0, 128, 64, 1)
        oled.text(menu_list[0].upper(), 8, 6, 0)

        oled.fill_rect(5, 24, 21, 12, 1)
        oled.fill_rect(5, 43, 21, 12, 1)
        oled.fill_rect(69, 24, 21, 12, 1)
        oled.fill_rect(69, 43, 21, 12, 1)

        oled.text("1: ", 8, 27, 0)
        oled.text("2: ", 8, 46, 0)
        oled.text("3: ", 72, 27, 0)
        oled.text("4: ", 72, 46, 0)
        oled.text(str(a) + "%", 31, 27, )
        oled.text(str(sensor_2) + "%", 31, 46, )
        oled.text(str(sensor_3) + "%", 96, 27, )
        oled.text(str(sensor_4) + "%", 96, 46, )
        oled.show()
        time.sleep_ms(10)


def sensor_detail():
    # SENSOREN Detail
    oled.fill(0)

    oled.fill_rect(0, 0, 128, 20, 1)
    oled.rect(0, 0, 128, 64, 1)
    oled.text(menu_list[1].upper(), 8, 6, 0)

    oled.text("set [" + str(sensor_1) + "%" + "]", 8, 27)

    oled.text("range: " + str(sensor_2) + " - " + str(sensor_3), 8, 46)

    oled.show()


for i in range(1, 10):
    sensor_overview()
    time.sleep(5)
    sensor_detail()
    time.sleep(5)
