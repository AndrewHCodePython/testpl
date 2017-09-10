#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-
#import re


# string = "People » Scott Zoltok » View | Toronto Ultimate Club"
# print(string)
# out = re.search('\u00BB\s{1}(.+?)\s{1}\u00BB', string, re.UNICODE).group(1)
# print (out)
import time
import sys


def progress(count, total, suffix=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))
    print(filled_len)
    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', suffix))
    sys.stdout.flush()  # As suggested by Rom Ruben

total = 100
i = 0
while i < total:
    progress(i, total, suffix='Doing very long job')
    time.sleep(0.5)  # emulating long-playing job
    i += 1
