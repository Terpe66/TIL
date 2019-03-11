import sys
sys.stdin = open("6485.txt")

for t in range(int(input())):
    N = int(input())

    BUS = []
    for _ in range(N):
        BUS.append(list(map(int, input().split())))

    P = int(input())
    C = []
    for p in range(P):
        C.append(int(input()))

    print(f"#{t+1}", end=" ")
    for c in C:
        cnt = 0
        for b in BUS:
            if b[0] <= c <= b[1]:
                cnt += 1

        print(cnt, end=" ")
    print()