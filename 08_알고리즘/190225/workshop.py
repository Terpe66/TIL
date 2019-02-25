import sys
sys.stdin = open("workshop.txt")

for t in range(10):
    V, E = map(int, input().split())
    S = []
    ans = []
    G = [[] for _ in range(V + 1)]
    visit = [[] for _ in range(V + 1)]

    g = list(map(int, input().split()))
    for i in range(0, len(g), 2):
        G[g[i]].append(g[i+1])
        visit[g[i+1]].append(g[i])

    start = 1
    print(f"#{t+1}", end=" ")
    while not G == [[]] * (V+1):
        if G[start] and not visit[start]:
            S.append(start)
            for m in G[start]:
                G[start].remove(m)
                visit[m].remove(start)
                if not G[start] and not visit[start]:
                    ans.append(start)
                start = m
                break
        elif not G[start] and not visit[start] and start not in ans:
            start = S[-1]
            S.append(start)
        elif S and not G[start]:
            start = S.pop()
        else:
            if start < V:
                start += 1
            else:
                start = 0
    ans.append(start)

    for i in ans:
        print(i, end=" ")
    print()







