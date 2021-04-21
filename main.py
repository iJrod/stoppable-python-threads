import time
import threading

def monitor(id, stop):
    print(f"This is a started thread. Thread ID: {id}")
    while True:
        print(f"This thread - ID: {id} - is currently running")
        if stop():
            print("\tExiting loop.")
            break
    print(f"Thread - ID: {id} - STOPPING...")

def initialiseThreads():
    stop_threads = False
    threads = []
    sites = ["zero,","one","two","three"]
    for id in enumerate(sites):
        tmp = threading.Thread(target=monitor, args=(id, lambda: stop_threads))
        threads.append(tmp)
        tmp.start()
    time.sleep(5)
    print('>> 5 second sleep finished; stopping all threads...')
    stop_threads = True
    for thread in threads:
        thread.join()
    print('>> All threads stopped')

if __name__ == '__main__':
    initialiseThreads()
