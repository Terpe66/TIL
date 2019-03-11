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
    visited = [False]*(Node+1)
    Q = [s]
    cnt, start = 0, 0
    while start != g:
        # start = Q.pop(0)
        # visited[start] = True
        # for i in node[start]:
        #     if not visited[i]:
        #         Q.append(i)
        # cnt += 1
        for q in range(len(Q)):
            start = Q.pop(0)
            if start == g:
                cnt -= 1
                break
            visited[start] = True
            if not node[start]:
                continue
            for i in node[start]:
                if not visited[i]:
                    Q.append(i)
        cnt += 1



    start = s
    goal = g
    visited = [ False ] * (Node + 1)

    queue = [ (start, 0) ]
    visited[start] = True

    result = 0
    while len(queue) > 0:
        pop = queue.pop(0)
        cur_node, cur_cnt  = pop[0], pop[1]

        if cur_node == goal:
            result = cur_cnt
            break

        for e in node[cur_node]:
            if visited[e] == False:
                queue.append( (e, cur_cnt + 1) )
                visited[e] = True

    print(f'#{t + 1}', result)


    # idx, ans = 1, 0
    # cnt = 0
    # Q = [[idx, ans]]
    # while Q:
    #     idx, ans = Q[0][0], Q[0][1]
    #     Q.pop(0)
    #     if idx == g:
    #         A.append(ans)
    #         continue
    #     if node[idx]:
    #         ans += 1
    #         while cnt < len(node[idx]):
    #             if [node[idx][cnt], ans] not in Q:
    #                 Q.append([node[idx][cnt], ans])
    #                 cnt += 1
    #             else:
    #                 break
    #         cnt = 0
    # ans *= 2
    # for a in A:
    #     if a < ans:
    #         ans = a

    print(f"#{t+1} {cnt}")