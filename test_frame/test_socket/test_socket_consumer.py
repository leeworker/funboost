import sys

import time
import random
from funboost import boost, BrokerEnum, ConcurrentModeEnum


@boost('127.0.0.1:6666', broker_kind=BrokerEnum.UDP, qps=0, is_print_detail_exception=True, max_retry_times=3,log_level=20,)
def f(x):
    # time.sleep(7)
    # if x % 10 == 0 and random.random() < 0.2:
    #     raise ValueError('测试函数出错')
    if x % 1000 == 0:
        print(x)

    return x * 10


if __name__ == '__main__':
    f.consume()
    for i in range(20000):
        f.push(i)
