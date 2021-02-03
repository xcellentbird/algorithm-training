def solution(s):
    answer = ''
    return str(min(map(int,s.split()))) + ' ' + str(max(map(int,s.split())))
