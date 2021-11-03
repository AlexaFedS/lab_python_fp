import time
from contextlib import contextmanager

class cm_timer_1:
    def __init__(self):
        self._start_time = time.time()

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(exc_type, exc_val, exc_tb)
        else:
            print('time ', time.time() - self._start_time)


@contextmanager
def cm_timer_2():
    _start_time = time.time()
    yield 1
    print('time ', time.time() - _start_time)


def main():
    with cm_timer_1():
        time.sleep(5.5)

    with cm_timer_2():
        time.sleep(5.5)

if __name__== "__main__":
    main()