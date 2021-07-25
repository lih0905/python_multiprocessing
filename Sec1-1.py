import logging
import time
import threading

logging.basicConfig(
    format='%(asctime)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO
)

def thread_func(name):
    logging.info(f"Sub-thread: starting : {name}")
    time.sleep(3)
    logging.info(f"Sub-thread: finishing : {name}")
    
    
if __name__ == '__main__':
    
    logging.info(f"Main-thread: before creating thread")
    thread = threading.Thread(target=thread_func, args=('first',))
    logging.info(f"Main-thread: before running thread")
    
    thread.start()
#     thread.join()
    logging.info(f"Main-thread: wait for the thread to finish") # join()을 쓰지 않으면 메인쓰레드가 먼저 종료됨    
    
    logging.info(f"Main-thread: finishing") # join()을 쓰지 않으면 메인쓰레드가 먼저 종료됨
    
