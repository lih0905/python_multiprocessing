import logging
import time
from concurrent.futures import ThreadPoolExecutor

def thread_func(name, d):
    logging.info(f"Sub-thread {name} starting")
    res = 0
    for i in range(d):
        res += i
    logging.info(f"Sub-thread {name} finishing : {res}")
    return res

logging.basicConfig(
    format='%(asctime)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO
)

if __name__ == '__main__':
    logging.info("Main-thread starting")
    
    # First method
#     executor = ThreadPoolExecutor(max_workers=3)
#     x = executor.submit(thread_func, 'first', 2000000)
#     y = executor.submit(thread_func, 'second', 1000000)
#     print(x.result(), y.result())

    # Second method
    with ThreadPoolExecutor(max_workers=3) as executor:
        res = executor.map(thread_func, ('first', 'second',), (10000000,1000,))
        print(list(res))
    
    logging.info("Main-thread finishing")
