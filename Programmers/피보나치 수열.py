# 재귀함수로 풀 수 있지만, 함수 호출 시간도 있기 때문에 비효율적
def solution(n):
    pibo = [0,1,1]
    if n == 1 or n == 2:
        return 1
    else:
        for i in range(2,n):
            pibo.append(pibo[-1] + pibo[-2])
        return pibo[-1] % 1234567
