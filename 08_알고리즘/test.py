for T in range(10):
    test_case = int(input())
    arr = []
    for c in range(100):
        arr_arr = list(map(int, input().split()))
        arr.append(arr_arr)

    max_sum = 0
    for i in range(len(arr)):
        SUM_T, SUM_B = 0, 0
        for j in range(len(arr[0])):
            SUM_T += arr[i][j]
            SUM_B += arr[j][i]
            if i == j:
                SUM_T += arr[i][j]
                SUM_B += arr[j][i]
                SUM_L += arr[i][j]
            elif i + j == 4:
                SUM_T += arr[i][j]
                SUM_B += arr[j][i]
                SUM_R += arr[i][j]
            elif i == j and i + j == 4:
                SUM_T += arr[i][j]
                SUM_B += arr[j][i]
                SUM_L += arr[i][j]
                SUM_R += arr[i][j]
        if max_sum < SUM_T:
            max_sum = SUM_T
        if max_sum < SUM_B:
            max_sum = SUM_B
        if max_sum < SUM_L:
            max_sum = SUM_L
        if max_sum < SUM_R:
            max_sum = SUM_R
            
    print(f"#{test_case} {max_sum}")