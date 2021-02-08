import heapq

def solution(scoville, K):
    answer = 0
    scoville.sort()
    for i, food in enumerate(scoville):
        if food > K:
            scoville = scoville[:i+1]
            break
            
    heapq.heapify(scoville)
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        answer+=1
        new_food = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        heapq.heappush(scoville, new_food)
        
    return answer
