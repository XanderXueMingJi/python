import _thread
import time


class ThreadTest(object):
    def __init__(self):
        self.count = 0
        self.lock = None

    def runnable(self):
        self.lock.acquire()
        print('thread ident is ' + str(_thread.get_ident()) +
              ', lock acquired!')
        for i in range(0, 100000):
            self.count += 1
        print('thread ident is ' + str(_thread.get_ident()) +
              ', pre lock release!')
        self.lock.release()

    def test(self):
        self.lock = _thread.allocate_lock()
        for i in range(0, 10):
            _thread.start_new_thread(self.runnable, ())


if __name__ == '__main__':
    test = ThreadTest()
    test.test()
    print('thread is running...')
    time.sleep(5)
    print('test finish, count is:' + str(test.count))
