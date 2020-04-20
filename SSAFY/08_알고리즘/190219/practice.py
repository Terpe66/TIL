arr = [[9, 20, 2, 18, 11],
        [19, 1, 25, 3, 21], 
        [8, 24, 10, 17, 7], 
        [15, 4, 16, 5, 6], 
        [12, 13, 22, 23, 14]]

arr1 = []

for i in range(len(arr)):
    for j in range(len(arr[0])):
        arr1.append(arr[i][j])
    
for i in range(len(arr1)-1):
    for j in range(len(arr1)-1):
        if arr1[j] > arr1[j+1]:
            arr1[j], arr1[j+1] = arr1[j+1], arr1[j]

cnt = 5

while cnt > 0:
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            
        cnt -= 1