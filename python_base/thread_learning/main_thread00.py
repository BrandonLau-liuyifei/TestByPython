# ！/usr/bin/env python
# -*- coding：utf-8 -*-
import time, logging, _thread

logging.basicConfig(level=logging.INFO)


def loop1():
    logging.info("start loop1 at " + time.ctime())
    time.sleep(4)
    logging.info("end loop1 at" + time.ctime())


def loop2():
    logging.info("start loop2 at " + time.ctime())
    time.sleep(4)
    logging.info("end loop2 at" + time.ctime())


def main():
    # logging.info("start all at " + time.ctime())
    # loop1()
    # loop2()
    # logging.info("end all at "+time.ctime())
    '''
    INFO:root:start all at Sun Jun  6 15:12:50 2021
    INFO:root:start loop1 at Sun Jun  6 15:12:50 2021
    INFO:root:end loop1 atSun Jun  6 15:12:54 2021
    INFO:root:start loop2 at Sun Jun  6 15:12:54 2021
    INFO:root:end loop2 atSun Jun  6 15:12:58 2021
    INFO:root:end all at Sun Jun  6 15:12:58 2021
    '''
    # _thread 模块没有守护线程的作用，执行主线程会kill掉子线程，需要在主线程结束前等待
    logging.info("start all at " + time.ctime())
    _thread.start_new_thread(loop1, ())
    _thread.start_new_thread(loop2, ())
    time.sleep(6)
    logging.info("end all at " + time.ctime())
    '''
    INFO:root:start all at Sun Jun  6 15:20:55 2021
    INFO:root:end all at Sun Jun  6 15:20:55 2021
    '''
    '''
    INFO:root:start all at Sun Jun  6 18:54:40 2021
    INFO:root:start loop2 at Sun Jun  6 18:54:40 2021
    INFO:root:start loop1 at Sun Jun  6 18:54:40 2021
    INFO:root:end loop2 atSun Jun  6 18:54:44 2021
    INFO:root:end loop1 atSun Jun  6 18:54:44 2021
    INFO:root:end all at Sun Jun  6 18:54:46 2021
    '''


if __name__ == '__main__':
    main()
