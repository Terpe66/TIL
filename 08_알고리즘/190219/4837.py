import sys
sys.stdin = open("4837.txt", "r")

for t in range(int(input())):
    n_k = list(map(int, input().split()))
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    sum_list = []
    for i in range(1 << len(A)):
        SUM = 0
        cnt = 0
        for j in range(len(A)):
            if i & (1 << j) != 0 and cnt < n_k[0]:
                SUM += A[j]
                cnt += 1
        in_list = []
        if SUM == n_k[1] and cnt == n_k[0]:
            cnt = 0
            for j in range(len(A)):
                if i & (1 << j) != 0 and cnt < n_k[0]:
                    in_list.append(A[j])
                    cnt += 1
            if in_list not in sum_list:
                sum_list.append(in_list)

    print("#{} {}".format(t+1, len(sum_list)))