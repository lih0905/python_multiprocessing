import logging
import time
import threading

logging.basicConfig(
    format='%(asctime)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO
)

def thread_func(name, r):
    logging.info(f"Sub-thread: starting : {name}")
    for i in r:
        print(i)
    logging.info(f"Sub-thread: finishing : {name}")
    
    
if __name__ == '__main__':
    
    logging.info(f"Main-thread: before creating thread")
    x = threading.Thread(target=thread_func, args=('first',range(20000)), daemon=True) # 데몬쓰레드는 메인쓰레드 종료시 자동 종료됨
    y = threading.Thread(target=thread_func, args=('second',range(100)), daemon=True)
    logging.info(f"Main-thread: before running thread")
    
    x.start()
    y.start()
    
    
#     x.join()
#     y.join()


    
    logging.info(f"Main-thread: wait for the thread to finish") # join()을 쓰지 않으면 메인쓰레드가 먼저 종료됨    
    
    logging.info(f"Main-thread: finishing") # join()을 쓰지 않으면 메인쓰레드가 먼저 종료됨
    
