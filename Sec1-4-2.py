import logging
from concurrent.futures import ThreadPoolExecutor
import time
import threading

class FakeDataStore:
    # 공유 변수(value)
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()
        
    # 변수 업데이트 함수
    def update(self, n):
        logging.info(f"Thread {n}: starting update")
        
        # Mutex & Lock 등 동기화(thread syncronization 필요)
        
#         # Lock 획득 (방법1)
#         self._lock.acquire() # 먼저 들어온 사람이 열쇠 획득
#         logging.info(f'Thread {n} has lock')
        
#         local_copy = self.value # local_copy의 stack 영역에 0 저장
#         local_copy += 1
#         time.sleep(0.1)
#         self.value = local_copy
        
#         # Lock 반환
#         logging.info(f'Thread {n} about to release lock')
#         self._lock.release()
        
        # Lock 획득 (방법2)
        with self._lock:
            logging.info(f'Thread {n} has lock')

            local_copy = self.value # local_copy의 stack 영역에 0 저장
            local_copy += 1
            time.sleep(0.1)
            self.value = local_copy

            # Lock 반환
            logging.info(f'Thread {n} about to release lock')            
    
        logging.info(f"Thread {n}: finishing update")

if __name__ == "__main__":
    fmt="%(asctime)s: %(message)s"
    logging.basicConfig(format=fmt, level=logging.INFO, datefmt='%H:%M:%S')

    # 클래스 인스턴스화
    store = FakeDataStore()
    
    logging.info(f"Testing update. Starting value is {store.value}")
    
    # with context 시작
    with ThreadPoolExecutor(max_workers=6) as executor:
        for n in ['First', 'Second', 'Third', 'Four']:
            executor.submit(store.update, n)
            
    logging.info(f"Testing update. Ending value is {store.value}")
    # 그냥 이렇게만 하면 2로 출력되는데, 이는 self.value 접속하는 속도가 너무 빨라서
    # 업데이트 전에 참조해버리기 때문
    