from threading import Thread
import time


STOP_THREADS = False


def infiniteTask(id):
    print("Infinite task {} has started".format(id))
    count = 0
    while not STOP_THREADS:
        count += 1


def finiteTask(id):
    print("Finite task {} has started".format(id))
    count = 0
    for i in range(100):
        count += i


if __name__ == "__main__":

    # Create some threads
    numThreads = 6
    threads = []
    for i in range(numThreads):
        threads.append(Thread(target=finiteTask, args=(i+1, ), ))

    # Start them
    startTime = time.time()
    for i in range(numThreads):
        threads[i].start()

    # Wait for stop signal / test ctrl-c / check cpu-load
    # uIn = "0"
    # while uIn == "0":
    #     uIn = input("Enter anything to stop all threads: ")
    # STOP_THREADS = True

    # Threads won't join until  the functions within them are done.
    for i in range(numThreads):
        threads[i].join()

    print("All done. Execution time was: {:.4f} seconds".format(
        time.time() - startTime))
