def solution(N, road, K):
    answer = 1
    
    road_map = {n:[] for n in range(1,N+1)}
    for r in road:
        for i, rm in enumerate(road_map[r[0]]):
            if rm[0] == r[1]:
                if rm[1] > r[2]:
                    road_map[r[0]][i][1] = r[2]
                break
        else:
            road_map[r[0]].append([r[1], r[2]])
            
        for i, rm in enumerate(road_map[r[1]]):
            if rm[0] == r[0]:
                if rm[1] > r[2]:
                    road_map[r[1]][i][1] = r[2]
                break
        else:
            road_map[r[1]].append([r[0], r[2]])
    
    for goal in range(2,N+1):
        good = False
        now = 1
        route = {now:[]}
        order = [now]
        while True:
            for r in road_map[now]:
                if r[0] not in route:
                    route[now].append(r[0])
            
            if not route[now]:
                for o in reversed(order):
                    if not route[o]:
                        del route[o]
                        order.pop()
                    else:
                        now = route[o].pop()
                        break

            else:
                now = route[now].pop()

            while route:
                route[now] = []
                order.append(now)
                if now == goal:

                    score = 0
                    start = 1
                    for arrive in order[1:]:
                        for A in road_map[start]:
                            if A[0] == arrive:
                                score+= A[1]
                                start = arrive
                    if score <= K:
                        good = True
                        break
                    
                    order.pop()
                    del route[now]
                    for o in reversed(order):
                        if not route[o]:
                            del route[o]
                            order.pop()
                        else:
                            now = route[o].pop()
                            
                            break
                else:
                    break
            
            if good:
                answer+=1
                break
            
            
            stop = True
            for i in route:
                if i:
                    stop = False
                    break
            if stop or not route:
                break
    return answer
