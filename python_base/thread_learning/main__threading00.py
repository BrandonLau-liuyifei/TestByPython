# ！/usr/bin/env python
# -*- coding：utf-8 -*-
# 代码判断子线程结束，主线程再结束
import logging
import threading
import time

logging.basicConfig(level=logging.INFO)

loops = [2, 4]


def loop(nloop, nsec):
    logging.info("start loop" + str(nloop) + "at" + time.ctime())
    time.sleep(nsec)
    logging.info("end loop" + str(nloop) + "at" + time.ctime())


def main():
    logging.info("start all at" + time.ctime())
    threads = []
    nloops = len(loops)
    for i in range(nloops):
        t = threading.Thread(target=loop, args=(i, loops[i]))
        threads.append(t)
    for i in range(nloops):
        threads[i].start()
    for i in range(nloops):
        threads[i].join()
    logging.info("end all at" + time.ctime())


if __name__ == '__main__':
    main()

    '''
    INFO:root:start all atSun Jun  6 19:08:40 2021
    INFO:root:start loop0atSun Jun  6 19:08:40 2021
    INFO:root:start loop1atSun Jun  6 19:08:40 2021
    INFO:root:end loop0atSun Jun  6 19:08:42 2021
    INFO:root:end loop1atSun Jun  6 19:08:44 2021
    INFO:root:end all atSun Jun  6 19:08:44 2021
    '''
