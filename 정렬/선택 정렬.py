"""
선택 정렬
목록에서 가장 큰 데이터를 선택해
맨 뒤의 데이터와 자리를 맞바꾸는 식으로 정렬
"""

import random
# timeit 모듈에서 default_timer 클래스를 timer이름으로 불러온다
from timeit import default_timer as timer

# random.sample(범위, 개수)
x = random.sample(range(10000), 100)

def selection_sort(A):
    for last in range(len(A)-1, 0, -1): # len(A)-1부터 1까지 -1해가며
        largest = 0 # 가장 큰 원소의 index
        for i in range(1, last+1): # 1부터 last까지
            if A[i] > A[largest]:
                largest=i
        x[largest],x[last] = x[last],[largest] # switch data

