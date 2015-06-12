# -*- coding:koi8-r -*-

import sched
import time
import threading


class SingletonDecorator:
    def __init__(self, klass):
        self.klass = klass
        self.instance = None

    def __call__(self, *args, **kwds):
        if self.instance is None:
            self.instance = self.klass(*args, **kwds)
        return self.instance


class Scheduler:
    def __init__(self):
        self.start_time = time.time()
        self.timer = sched.scheduler(time.time, time.sleep)

    def scheduler(self, interval, job, *args):
        """
        В отдельном потоке запускает планировщик на выполнение функции через
        интервал.
        :param interval: задается в секундах
        :param job: испольняемая функция по расписания
        :param args: аргументы функции
        :return:
        """
        print('fire', time.time())
        self.timer.enter(interval, 1, job, argument=args)
        t = threading.Thread(target=self.timer.run)
        t.start()

    def get_time_modeling(self):
        return time.time() - self.start_time


timerSingleton = SingletonDecorator(Scheduler)
