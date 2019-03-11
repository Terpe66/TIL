import sys
sys.stdin = open("5110.txt")

for t in range(int(input())):
    length, suyul = map(int, input().split())
    S = []

    for _ in range(suyul):
        S.append(list(map(int, input().split())))
    ans = S.pop(0) + [0] * length * (suyul - 1)
    idx = length * suyul
    for s in S:
        for a in range(idx):
            if ans[a] >= s[0] or ans[a+1] == 0:
                for n in range(a, idx):
                    if ans[n] == 0:
                        break

                for an in range(n, a+1, -1):
                    ans[an+3] = ans[an-1]

                for na in range(4):
                    ans[a+1+na] = s[na]
                break
        else:
            for n in range(idx):
                if ans[n] == 0:
                    break

            for an in range(1, n):
                ans[n] = ans[n-1]

            for na in range(4):
                ans[na] = s[na]

    print(f"#{t+1}", end=" ")
    for i in range(idx, idx-10, -1):
        print(ans[i], end=" ")
    print()