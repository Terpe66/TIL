import sys
sys.stdin = open("5102.txt")

for t in range(int(input())):
    Node, Line = map(int, input().split())
    node = [[] for _ in range(Node+1)]

    for _ in range(Line):
        s, g = map(int, input().split())
        node[s].append(g)
        node[g].append(s)

    s, g = map(int, input().split())
    A = []
    idx, ans = 1, 0
    cnt = 0
    Q = [[idx, ans]]
    while Q:
        idx, ans = Q[0][0], Q[0][1]
        Q.pop(0)
        if idx == g:
            A.append(ans)
            continue
        if node[idx]:
            ans += 1
            while cnt < len(node[idx]):
                if [node[idx][cnt], ans] not in Q:
                    Q.append([node[idx][cnt], ans])
                    cnt += 1
                else:
                    break
            cnt = 0
    ans *= 2
    for a in A:
        if a < ans:
            ans = a

    print(f"#{t+1} {ans}")