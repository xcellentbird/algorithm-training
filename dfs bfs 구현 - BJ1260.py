N, M, V = map(int, input().split())
line = [list(map(int, input().split())) for _ in range(M)]
lines = [[] for _ in range(N)]
for l in line:
    lines[l[0]-1].append(l[1]-1)
    lines[l[1]-1].append(l[0]-1)

for l in lines:
    l.sort()

def dfs(start, gone, turn, lines):
    gone[start] = True
    turn.append(start+1)
    for can_go in lines[start]:
        if not gone[can_go]:
            cur = can_go
            dfs(cur, gone, turn, lines)
    return turn

def bfs(start, gone, turn, lines):
    if True not in gone:
        gone[start] = True
        turn.append(start+1)
    togo = []
    for can_go in lines[start]:
        if not gone[can_go]:
            gone[can_go] = True
            turn.append(can_go+1)
            togo.append(can_go)
    for can_go in togo:
        bfs(can_go, gone, turn, lines)
    return turn
            
cur = V - 1
gone = [False for _ in range(N)]
turn = []        

print(dfs(cur, gone, turn, lines))

cur = V - 1
gone = [False for _ in range(N)]
turn = []

print(bfs(cur, gone, turn, lines))
