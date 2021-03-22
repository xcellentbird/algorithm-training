from itertools import product
def solution(n, money):    
    cases = {i:[] for i in range(n+1)}
    cases[0].append([])
    
    for case, m in product(range(1, n+1), money):
        gap = case - m
        if gap >= 0 and gap in cases:
            for c in cases[gap]:
                get = sorted(c + [m])
                if get not in cases[case]:
                    cases[case].append(get)

    return len(cases[n])
