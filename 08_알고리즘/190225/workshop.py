import sys
sys.stdin = open("workshop.txt")

for t in range(10):
    V, E = map(int, input().split())
    S = []
    ans = []
    G = [[] for _ in range(V + 1)]
    visit = [[] for _ in range(V + 1)]
    empty = [[]] * (V + 1)
    g = list(map(int, input().split()))
    for i in range(0, len(g), 2):
        G[g[i]].append(g[i+1])
        visit[g[i+1]].append(g[i])

    start = 1
    print(f"#{t+1}", end=" ")
    while G != empty:
        if G[start] and not visit[start]:
            S.append(start)
            if start not in ans:
                ans.append(start)
            m = G[start][0]
            G[start].remove(m)
            visit[m].remove(start)
            start = m
            if not G[start] and not visit[start]:
                ans.append(start)
                start = S.pop()
        else:
            if start < V:
                start += 1
            else:
                start = 1

    for i in ans:
        print(i, end=" ")
    print()







