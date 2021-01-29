# thread use shared memory, but great on I/O devices, bound by GIL
# not killable so possible memory leaks and race condition
# process has separate memory and can use multiple cpu
# process is slower to start

from threading import Thread
import os

def square_numbers():
    for i in range(1000):
        result = i * i


if __name__ == "__main__":
    threads = []
    num_threads = os.cpu_count()

    # create threads and asign a function for each thread
    for i in range(num_threads):
        thread = Thread(target=square_numbers)
        threads.append(thread)

    # start all threads
    for thread in threads:
        thread.start()

    # wait for all threads to finish
    # block the main thread until these threads are finished
    for thread in threads:
        thread.join()

print('end main')