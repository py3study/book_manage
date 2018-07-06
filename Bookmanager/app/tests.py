from django.test import TestCase

import time


#!/usr/bin/env python
# coding: utf-8

import random
import time
import sys
from multiprocessing import Process


def processBar_tortoise(num, total, name_icon):  # 进度条
    rate = num / total
    rate_num = int(rate * 100)
    s = '起点 ' + '> ' * (total-2) + '终点'
    if rate_num == 100:
        s = s.split()
        s[num] = name_icon
        y = ''.join(s)
        r = '\r{}\n'.format(y)
    else:
        s = s.split()
        s[num] = name_icon
        y = ''.join(s)
        r = '\r{}'.format(y)
    sys.stdout.write(r)
    sys.stdout.flush


def processBar_hare(num, total, name_icon):  # 进度条
    rate = num / (total+1)
    rate_num = int(rate * 100)
    s = '起点 ' + '> ' * (total-3) + '终点'
    if rate_num == 100:
        s = s.split()
        s[num] = name_icon
        y = ''.join(s)
        r = '\r{}\n'.format(y)
    else:
        s = s.split()
        s[num] = name_icon
        y = ''.join(s)
        r = '\r{}'.format(y)
    sys.stdout.write(r)
    sys.stdout.flush


def tortoise(total_step):
    start_time = time.time()
    step = 0
    while step < total_step:
        time.sleep(0.2)
        step += 1
        processBar_tortoise(step, total_step+1, '🐢')
    end_time = time.time()
    print('\n乌龟花了多少时间:{:.2f}'.format(end_time-start_time))


def hare(total_step):
    start_time = time.time()
    step = 0
    flags = [1, 0]
    while step < total_step:
        time.sleep(0.2)
        sleeping = flags[int(random.random() * 10) % 2]
        if sleeping:
            processBar_hare(step, total_step, '🐇zzz')
        else:
            step += 2
            processBar_hare(step, total_step+2, '🐇')
    end_time = time.time()
    print('\n兔子花了多少时间:{:.2f}'.format(end_time - start_time))


if __name__ == '__main__':
    t = Process(target=tortoise, args=(20,))
    h = Process(target=hare, args=(20,))
    t.start()
    h.start()
