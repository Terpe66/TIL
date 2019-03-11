import sys
sys.stdin = open("5110.txt")

for t in range(int(input())):
    length, suyul = map(int, input().split())
    S, N = [], []
    ans = [0] * length * suyul
    for _ in range(suyul):
        S.append(list(map(int, input().split())))

    idx = 0
    for s in S:
        for n in s:
            N.append([idx, n])
            idx += 1

    cnt, i = 0, 0
    while S:
        new = S.pop(0)
        idx = length * cnt
        for i in range(idx):
            if N[i][1] > new[0]:
                break
        else:
            if i > 0:
                i += 1

        new_cnt = idx - i
        new_idx = i
        while new_cnt > 0:
            N[new_idx][0] += length
            new_idx += 1
            new_cnt -= 1

        for n in range(length):
            N[idx+n][0] = i+n

        cnt += 1

    for n in N:
        ans[n[0]] = n[1]


    print(f"#{t+1}", end=" ")
    for i in range(len(ans)-1, len(ans)-11, -1):
        print(ans[i], end=" ")
    print()





    # 시간 초과 2
    # ans = S.pop(0) + [0] * length * (suyul - 1)
    # cnt = 1
    # while S:
    #     new = S.pop(0)
    #     for i in range(length*cnt):
    #         if ans[i] > new[0]:
    #             break
    #     else:
    #         i += 1
    #
    #     re = length * cnt - i
    #     j = re + 1
    #     while re > 0:
    #         idx = length * (cnt + 1) - j + re
    #         ans[idx] = ans[idx-length]
    #         re -= 1
    #
    #     for n in range(length):
    #         ans[n+i] = new[n]
    #
    #     cnt += 1
    #
    # print(f"#{t+1}", end=" ")
    # for i in range(len(ans)-1, len(ans)-11, -1):
    #     print(ans[i], end=" ")
    # print()



    # 시간 초과
    # for s in S:
    #     a, idx = 0, len(ans)
    #     while a < idx:
    #         if ans[a] > s[0]:
    #             break
    #         a += 1
    #
    #     ans.extend([""] * length)
    #     if a >= idx:
    #         for i in range(length):
    #             ans[i+a] = s[i]
    #
    #     else:
    #         for i in range(len(ans)-1, a+length-1, -1):
    #             ans[i] = ans[i-length]
    #
    #         for i in range(length):
    #             ans[a+i] = s[i]
    #
    # print(f"#{t+1}", end=" ")
    # for i in range(len(ans)-1, len(ans)-11, -1):
    #     print(ans[i], end=" ")
    # print()



