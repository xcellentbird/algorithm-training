def solution(s):
    answer = 0
    lengths = []
    
    if len(s) == 1:
        return 1
    
    for i, center in enumerate(s):
        rng = 0
        while s[i-rng:i+1] == s[i:i+rng+1][::-1]:
            rng += 1
            #print(s[i-rng:i+1], s[i:i+rng+1][::-1])
        lengths.append(2 * rng - 1)
    return max(lengths)
