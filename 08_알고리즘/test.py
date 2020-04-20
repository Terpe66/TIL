arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
c = 3
N = len(arr)
sum_list = []
for i in range(1 << N):
    SUM = 0
    cnt = 0
    for j in range(N):
        if i & (1 << j) != 0 and cnt < c:
            SUM += arr[j]
            cnt += 1    
    in_list = []
    if SUM == 10 and cnt == c:
        cnt = 0
        for j in range(N):
            if i & (1 << j) != 0 and cnt < c:
                in_list.append(arr[j])
                cnt += 1
        if in_list not in sum_list:
            sum_list.append(in_list)
print(sum_list)


