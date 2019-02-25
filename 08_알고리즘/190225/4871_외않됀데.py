import sys
sys.stdin = open("4871.txt", "r")

for t in range(int(input())):
    V, E = map(int, input().split())
    node = [[] for v in range(V + 1)]

    for _ in range(E):
        s, e = map(int, input().split())
        node[s].append(e)

    start, end = map(int, input().split())
    result = 0
    visit = []
    while len(node) > 0 and result == 0:
        if start not in visit and node[start]:
            visit.append(start)
        if node[start]:
            for m in node[start]:
                if m == end:
                    result = 1
                    break
                node[start].remove(m)
                start = m
        elif visit:
            if start in visit:
                visit.remove(start)
                if not visit:
                    break
            start = visit[-1]

    print(f"#{t+1} {result}")
