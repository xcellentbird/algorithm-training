def solution(num):
    answer = 0
    while answer < 500:
        answer += 1
        if not num%2:
            num = num // 2
        else:
            num = num * 3 + 1
        if num == 1:
            break
    if answer == 500:
        return -1
    return answer
