#!/usr/bin/env python
# encoding: utf-8
# @Author    : w2n1ck
# @Time      : 2018/4/27 下午2:53
# @Introduce : 主程序

import sys, os
parentdir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
from utils.scheduler import Scheduler
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def main():
    try:
        s = Scheduler()
        s.run()
    except:
        main()


if __name__ == '__main__':
    main()