def solution(m, n, puddles):
    answer = 1
    for x in range(1,m+1):
        for y in range(1,n+1):
            if [x+1, y] in puddles and [x, y+1] in puddles:
                print('both puddles',x,y)
                if [x-1, y] in puddles and [x, y-1] in puddles:
                    pass
                elif [x-1, y] in puddles or [x, y-1] in puddles or x==1 or y==1:
                    answer-=1
                else:
                    answer-=2
                puddles.append([x+1, y+1])
            elif [x+1, y] in puddles or [x, y+1] in puddles or [x, y] in puddles:
                if x==m or y==n:
                    answer-=1
                continue
            elif x == m or y == n:
                continue
            else:
                print(x, y)
                answer+=1
    return answer%1000000007
