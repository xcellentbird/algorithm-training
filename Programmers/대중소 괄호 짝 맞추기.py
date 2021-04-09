def solution(s):
    answer = False
    garo = {'(':[0,1], ')':[0,-1], '{':[1,1], '}':[1,-1], '[':[2,1], ']':[2,-1]}
    score = [0, 0, 0]
    now = 0
    for i, ss in enumerate(s):
        score[garo[ss][0]] += garo[ss][1]
        if garo[ss][1] == -1:
            if score[garo[ss][0]] < 0:
                return False
            elif not score[0] and not score[1] and score[2]:
                if s[now:i+1] != s[now:i+1:-1]:
                    print(s[now:i+1], s[now:i+1:-1])
                    return False
                now = i+1
    if not sum(score):
        return True
    return answer
