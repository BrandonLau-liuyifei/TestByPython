# ！/usr/bin/env python
# -*- coding：utf-8 -*-
import _thread
import logging
import time

logging.basicConfig(level=logging.INFO)

# 主动判断子线程的状态
loops = [2, 4]


def loop(nloop, nsec, lock):
    logging.info("start at" + str(nloop) + "at" + time.ctime())
    time.sleep(nsec)
    logging.info("end at" + str(nloop) + "at" + time.ctime())
    lock.release()


def main():
    logging.info("start all at " + time.ctime())
    locks = []
    nloops = range(len(loops))
    for i in nloops:
        lock = _thread.allocate_lock()
        lock.acquire()
        locks.append(lock)
    for i in nloops:
        _thread.start_new_thread(loop, (i, loops[i], locks[i]))
    for i in nloops:
        while locks[i].locked(): pass
    logging.info("end all at " + time.ctime())


if __name__ == '__main__':
    main()
'''
INFO:root:start all at Sun Jun  6 19:46:58 2021
INFO:root:start at0atSun Jun  6 19:46:58 2021
INFO:root:start at1atSun Jun  6 19:46:58 2021
INFO:root:end at0atSun Jun  6 19:47:00 2021
INFO:root:end at1atSun Jun  6 19:47:02 2021
INFO:root:end all at Sun Jun  6 19:47:02 2021
'''
