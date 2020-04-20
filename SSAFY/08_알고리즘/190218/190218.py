arr = [[9, 20, 2, 18, 11],
        [19, 1, 25, 3, 21],
        [8, 24, 10, 17, 7],
        [15, 4, 16, 5, 6],
        [12, 13, 22, 23, 14]]

Sum = 0
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if i == 0 and j in (0, len(arr[0])-1):
            if j == 0:
                Sum += abs(arr[i][j+1] - arr[i][j]) + abs(arr[i+1][j] - arr[i][j])
            elif j == len(arr[0])-1:
                Sum += abs(arr[i][j-1] - arr[i][j]) + abs(arr[i+1][j] - arr[i][j])
            else:
                Sum += abs(arr[i][j+1] - arr[i][j]) + abs(arr[i+1][j] - arr[i][j]) + abs(arr[i][j-1] - arr[i][j])
            
        elif i == (len(arr)-1) and j in (0, len(arr[0])-1):
            if j == 0:
                Sum += abs(arr[i-1][j] - arr[i][j]) + abs(arr[i][j+1] - arr[i][j])
            elif j == len(arr[0])-1:
                Sum += abs(arr[i][j-1] - arr[i][j]) + abs(arr[i-1][j] - arr[i][j])
            else:
                Sum += abs(arr[i-1][j] - arr[i][j]) + abs(arr[i][j+1] - arr[i][j]) + abs(arr[i][j-1] - arr[i][j])

        else:
            Sum += abs(arr[i-1][j] - arr[i][j]) + abs(arr[i][j+1] - arr[i][j]) + abs(arr[i+1][j] - arr[i][j]) + abs(arr[i][j-1] - arr[i][j])
print(Sum)
