#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time

from assisipy import casu

class CasuL:

    def __init__(self, rtc_file, id_):

        self.casu = casu.Casu(rtc_file,log=False)
        self.time_on = 0
        self.time_start = time.time()
        self.id = int(id_)
        # Parse rtc file name to get CASU id
        # assumes casu-xxx.rtc file name format


if __name__ == '__main__':

    icasu = ['48', '49', '53', '54', '55', '56']

    begin_path = '../../rtc/casu-0'
    end_path = '.rtc'
    casus = [CasuL(begin_path + ic + end_path, ic) for ic in icasu]

    delta_s = 0.2
    dur_s = 2 * delta_s
    dt_l = 2.0
    sequence = [[49, delta_s, dur_s],
                [48, 2 * delta_s, dur_s],
                [55, 2 * delta_s, dur_s],
                [53, 3 * delta_s, dur_s],
                [56, 3 * delta_s, dur_s],
                [54, 4 * delta_s, dur_s],
                ]

    while(1):
        for i, item in enumerate(sequence):
            if i == 0:
                time.sleep(item[1])
            else:
                time.sleep(item[1] - sequence[i-1][1])
            time_now = time.time()
            for casu in casus:
                if time_now - casu.time_start >= casu.time_on:
                    casu.casu.set_diagnostic_led_rgb(0,0,0)
                    casu.time_on = 0
                    if casu.id == item[0]:
                        casu.time_start = time.time()
                        casu.time_on = item[2]
                        casu.casu.set_diagnostic_led_rgb(1,1,1)
