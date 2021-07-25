# Producer-Consumer Pattern
# 멀티스레드 디자인 패턴의 정석

# 파이썬 Event 객체
# Flag 초기값(0)
# set() -> 1, Clear() -> 0, Wait(1 -> 리턴, 0 -> 대기), is_set() -> 현 플래그 상태

import concurrent.futures
import logging
import queue
import random
import threading
import time

# 생산자
def producer(queue, event):
    """ 네트워크 대기 상태라 가정(서버) """
    while not event.is_set():
        message = random.randint(1, 11)
        logging.info(f"Producer made message: {message}")
        queue.put(message)
        
    logging.info("Producer sending event Exiting")
        
# 소비자
def consumer(queue, event):
    """ 응답 받고 소비하는 것으로 가정 or DB 저장 """
    while not event.is_set() or not queue.empty():
        message = queue.get()
        logging.info(f"Consumer storing message: {message} (size={queue.qsize()})")
        
        
    logging.info("Consumer receiving event Exiting")    

if __name__ == '__main__':
    fmt="%(asctime)s: %(message)s"
    logging.basicConfig(format=fmt, level=logging.INFO, datefmt='%H:%M:%S')
    
    # 사이즈 중요
    pipeline = queue.Queue(maxsize=10)
    
    # 이벤트 플래그 초기값 0
    event = threading.Event()
    
    # with context 시작
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline, event)
        executor.submit(consumer, pipeline, event)
        
        # 실행 시간 조정
        time.sleep(0.01)

        logging.info("Main: about to set event")

        # 프로그램 종료
        event.set()
    
    