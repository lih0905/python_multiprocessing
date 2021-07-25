import logging
from concurrent.futures import ThreadPoolExecutor
import time

class FakeDataStore:
    # 공유 변수(value)
    def __init__(self):
        self.value = 0
        
    # 변수 업데이트 함수
    def update(self, n):
        logging.info(f"Thread {n}: starting update")
        
        # Mutex & Lock 등 동기화(thread syncronization 필요)
        local_copy = self.value # local_copy의 stack 영역에 0 저장
        local_copy += 1
        time.sleep(0.1)
        self.value = local_copy
        
        logging.info(f"Thread {n}: finishing update")

if __name__ == "__main__":
    fmt="%(asctime)s: %(message)s"
    logging.basicConfig(format=fmt, level=logging.INFO, datefmt='%H:%M:%S')

    # 클래스 인스턴스화
    store = FakeDataStore()
    
    logging.info(f"Testing update. Starting value is {store.value}")
    
    # with context 시작
    with ThreadPoolExecutor(max_workers=2) as executor:
        for n in ['First', 'Second', 'Third']:
            executor.submit(store.update, n)
            
    logging.info(f"Testing update. Ending value is {store.value}")
    # 그냥 이렇게만 하면 2로 출력되는데, 이는 self.value 접속하는 속도가 너무 빨라서
    # 업데이트 전에 참조해버리기 때문
    