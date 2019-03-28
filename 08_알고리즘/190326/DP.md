# 190326 DP-1



```python
w = [5, 4, 6, 3] 	# 1 ~ n번 물건의 무게
v = [10, 40, 30, 50]	# 물건의 가치
N = len(v)			#물건의 수
maxW, maxV = 10, 0 # 배낭의 용량, 최대 가지

def knapsack(k, W, curV):
    global maxV
    if k == N: # 배낭에 물건을 넣는 한 가지 방법
        maxV = max(maxV, curV)
        return
    
    if W >= w[k]:
    	knapsack(k + 1, W - w[k], curV + v[k]) # k번째 물건을 넣는다
    knapsack(k + 1, W, curV)
```

```python
# 뭔가 틀림
w = [0, 5, 4, 6, 3] 	# 1 ~ n번 물건의 무게
v = [0, 10, 40, 30, 50]	# 물건의 가치
N = len(v)			#물건의 수
maxW, maxV = 10, 0 # 배낭의 용량, 최대 가지

def knapsack(k, W, curV):
    global maxV
    if k == 0: # 배낭에 물건을 넣는 한 가지 방법
        maxV = max(maxV, curV)
        return
    
    if W >= w[k]:
    	knapsack(k - 1, W - w[k], curV + v[k]) # k번째 물건을 넣는다
    knapsack(k - 1, W, curV)
```

```python
w = [0, 5, 4, 6, 3] 	# 1 ~ n번 물건의 무게
v = [0, 10, 40, 30, 50]	# 물건의 가치
N = len(v) - 1			#물건의 수
maxW, maxV = 10, 0 # 배낭의 용량, 최대 가지

def knapsack(k, W, curV):
    if k == 0 or w == 0:
        return 0
    if memo[k][w] != -1:
        return memo[k][w]
    case1 = case2 = 0
    if w >=w[k]:
        case1 = knapsack(k - 1, W - w[k]) + v[k]
       case2 = knapsack(k - 1, W)
    
    return case1 if case1 > case2 else case2

print(knapsack(N, maxW))
```

branch and bound... BNB... 크레이지 아케이드...

