#!/usr/bin/env python3
import roboclaw

class RoboClaw(object):
    """docstring for RoboClaw"""
    def __init__(self, address):
        self.address = address
    
    def move_both(self, val):
        """Takes 1 argument: val. Val should be any integer between 0 and 127, where 0 is full reverse, 64 is stop, and 127 is full forward"""
        roboclaw.ForwardBackwardM1(self.address, val)
        roboclaw.ForwardBackwardM1(self.address, val)
        