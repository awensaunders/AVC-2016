#!/usr/bin/env python3

import serial 
import RPi.GPIO as gpio

def init_serial_and_gpio(tty, baud):
    gpio.setmode(gpio.BOARD)
    global _ser
    _ser = serial.Serial(tty, baud)

class RoboClaw(object):
    """docstring for RoboClaw"""
    def __init__(self, selectpin):
        self.pin = selectpin
        gpio.setup(self.pin, gpio.OUT, initial = gpio.LOW)
    
    def _write(self, val):
        _ser.write(bytes([val]))
        
    def stop(self):
        self._write(0)
    
        
        