#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Seed casu for vibration pattern.
Blinks the red LED every 10 seconds and sends messages to neighbors.
"""

from assisipy import casu

import sys
import time

amplitudes = [[50,0],
              [50,0,50,20]]

frequencies = [[440,1],
               [440,1,1000,200]]

durations = [[500,100],
             [1000,100,200,500]]

sleep_periods = [[20,40],
                 [20,5]]

if __name__ == '__main__':

    c = casu.Casu(sys.argv[1])

    counter = 0
    while True:
        for (a,f,d,t) in zip(amplitudes,frequencies,durations,sleep_periods):
            c.set_diagnostic_led_rgb(g=1)
            c.set_vibrations_pattern(d,f,a)
            time.sleep(t[0])
            c.send_message('right','blink')
            c.set_diagnostic_led_rgb(g=0)
            c.set_speaker_standby()
            time.sleep(t[1])
