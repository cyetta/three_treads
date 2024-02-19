#!/usr/bin/env python3
import time
from threading import Thread
import site_parser


# Define custom class for thread with perfomance counter
class CustomThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.tic = None
        self.elapsed_time = None

    def run(self):
        self.tic = time.perf_counter()
        site_parser.print_table(
            'https://www.w3schools.com/html/html_tables.asp', 'ws-table-all')
        self.elapsed_time = time.perf_counter() - self.tic


# The main thread in which two child CustomThreads are executed.
def three_treads():
    # Init thread
    thread1 = CustomThread()
    thread2 = CustomThread()

    # Runing thread
    thread1.start()
    thread2.start()

    # Waiting while thread end, not more than 15 second
    thread1.join(15)
    thread2.join(15)

    # Printing thread execution time
    print(f"Thread 1 execution time {thread1.elapsed_time:0.4f}")
    print(f"Thread 2 execution time {thread2.elapsed_time:0.4f}")


three_treads()
