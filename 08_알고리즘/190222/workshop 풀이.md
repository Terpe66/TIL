



사다리타기는 총 7가지 경우가 있다.

- 올라갈 때 : 올라가기, 왼쪽, 오른쪽
- 오른쪽으로 갈 때 : 오른쪽으로 가기, 올라가기
- 왼쪽으로 갈 때 : 왼쪽으로 가기, 올라가기





```python
for test_case in range(1, 11):
    N = input()
    arr = []
    for i in range(100):
        arr.append(list(map(int, input().split())))
        
    # 출발점 찾기
    x = y = 0 # x: 행, y: 열
    for i in range(100):
        if arr[99][i] == 2:
            x, y = 99, i
            break

    dir = 0 # 0: 위, 1: 왼쪽, 2: 오른쪽
    while x != 0:
        # 진행 방향이 위쪽 and 현재 위치가 맨 왼쪽이 아님 and 바로 왼쪽이 0이 아닐 때
        if dir == 0 and y - 1 >= 0 and arr[x][y - 1]:
            y, dir = y - 1, 1 # 위치를 바로 왼쪽으로 이동, 진행 방향을 왼쪽으로 설정
        
        # 진행 방향이 위쪽 and 현재 위치가 맨 오른쪽이 아님 and 바로 오른쪽이 0이 아닐 때
        elif dir == 0 and y + 1 < 100 and arr[x][y + 1]:
            y, dir = y + 1, 2 # 위치를 바로 오른쪽으로 이동, 진행 방향을 오른쪽으로 설정
        
        # 진행 방향이 왼쪽 and 현재 위치가 맨 왼쪽이 아님 and 바로 왼쪽이 0이 아닐 때
        elif dir == 1 and y - 1 >= 0 and arr[x][y - 1]:
            y = y - 1 # 위치를 바로 왼쪽으로 이동해서 왼쪽으로 쭉 진행되게
        
        # 진행 방향이 오른쪽 and 현재 위치가 맨 오른쪽이 아님 and 바로 왼쪽이 0이 아닐 때
        elif dir == 2 and y + 1 < 100 and arr[x][y + 1]:
            y = y + 1 # 위치를 바로 오른쪽으로 이동해서 오른쪽으로 쭉 진행되게
        
        # 진행 방향이 위쪽이고 양쪽에 1이 없을 때(양쪽이 0이라 위로 올라가야 할 때)
        else:
            x, dir = x - 1, 0 # 행을 -1 한 칸 위로 이동, 진행 방향은 위쪽으로
    print(y)
    
    
    # 코드 줄이기
    dir = 0 # 0: 위, 1: 왼쪽, 2: 오른쪽
    while x != 0:
        # 진행 방향이 오른쪽이 아님 and 현재 위치가 맨 왼쪽이 아님 and 바로 왼쪽이 0이 아닐 때
        if dir != 2 and y - 1 >= 0 and arr[x][y - 1]:
            y, dir = y - 1, 1 # 위치를 바로 왼쪽으로 이동, 진행 방향을 왼쪽으로 설정
        
        # 진행 방향이 왼쪽이 아님 and 현재 위치가 맨 오른쪽이 아님 and 바로 오른쪽이 0이 아닐 때
        elif dir != 1 and y + 1 < 100 and arr[x][y + 1]:
            y, dir = y + 1, 2 # 위치를 바로 오른쪽으로 이동, 진행 방향을 오른쪽으로 설정
        
        # 진행 방향이 위쪽이고 양쪽에 1이 없을 때(양쪽이 0이라 위로 올라가야 할 때)
        else:
            x, dir = x - 1, 0 # 행을 -1 한 칸 위로 이동, 진행 방향은 위쪽으로
    print(y)
    
    # 다른 방법(왼쪽, 오른쪽으로 한 칸씩 이동이 아니라 한 번에 이동하고 한 칸 올리기)
    while x != 0:
        # 
        if y - 1 >= 0 and arr[x][y - 1]:
            while y - 1 >= 0 and arr[x][y - 1]:
                y -= 1
            x -= 1
        elif y + 1 < 100 and arr[x][y + 1]:
            while y + 1 < 100 and arr[x][y + 1]:
                y += 1
            x -= 1
        else:
            x -= 1
    print(y)
    

# 재귀 함수    
def DFS(x, y):
    if x == 0:
        return y
    arr[x][y] = 0
    if y - 1 >= 0 and arr[x][y - 1]:
        return DFS(x, y - 1)
    elif y + 1 < 100 and arr[x][y + 1]:
        return DFS(x, y + 1)
    else:
        return DFS(x - 1, y)
    
for test_case in range(1, 11):
    N = input()
    arr = []
    for i in range(100):
        arr.append(list(map(int, input().split())))
        
    # 출발점 찾기
    x = y = 0 # x: 행, y: 열
    for i in range(100):
        if arr[99][i] == 2:
            x, y = 99, i
            break    
```

