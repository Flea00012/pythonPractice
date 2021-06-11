import time
from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor(max_workers=3)


def wait_and_return(msg):
    time.sleep(1)
    return msg


executor.submit(wait_and_return, "Hello. executor")
