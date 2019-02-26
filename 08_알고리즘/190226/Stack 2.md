# Stack 2

### 계산기

- 문자열로 된 계산식이 주어질 때 스택을 이용해서 계산

- 문자열 수식 계산 방법

  - 중위 표기법의 수식을 후위 표기법으로 변경한다
  - 후위 표기법의 수식을 스택을 이용하여 계산한다
    - 중위 표기법(infix notation) : 연산자를 피연산자 가운데에 표기(A+B)
    - 후위 표기법(postfix notation) : 연산자를 피연산자 뒤에 표기(AB+)

- 중위 표기법을 후위 표기법으로 변경하는 방법

  - 수식의 연산자를 우선 순위에 따라 괄호를 사용해서 다시 표현한다.

  - 각 연산자를 그에 대응하는 오른쪽 괄호의 뒤로 이동시킨다.

  - 괄호를 제거한다.

    ```python
    A*B - C/D일 때
    1) ( (A*B) - (C/D) )
    2) ( (A B)* C D)/ )-
    3) AB*CD/-
    ```

- 중위 표기법에서 후위 표기법으로 변경하는 알고리즘(스택 이용)

  - 입력 받은 중위 표기식에서 토큰을 읽는다.
    - 토큰 : 의미 있는 문자열, 여기서는 연산자랑 피연산자
  - 토큰이 피연산자면 토큰을 출력한다.(저장한다고 생각하면 됨)
  - **토큰이 연산자(괄호 포함)**일 때, 토큰이 스택의 `top`에 저장된 연산자보다 **우선 순위가 높으면** 스택에 `push`, 아니면 스택의 `top` 연산자의 우선 순위가 **토큰의 우선 순위보다 낮을 때까지** 스택에서 `pop`하고 토큰을 `push`, 만약 `top`에 연산자가 없으면 `push`
  - 토큰이 오른쪽 괄호 `)`면 스택 top에 왼쪽 괄호 `(`가 올 때까지 스택에 `pop` 연산을 수행하고 `pop`한 연산자를 출력. 왼쪽 괄호를 만나면 `pop`만 하고 출력은 안 한다.
    - 여는 괄호가 나오면 무조건 스택에 `push`
  - 중위 표기식에 더 읽을 게 없으면 중지, 있으면 처음부터 반복
  - 스택에 남아 있는 연산자를 모두 `pop`해서 출력
    - 스택 밖의 여는 괄호의 우선 순위가 가장 높고 안의 여는 괄호는 가장 낮음

- 후위 표기법의 수식을 스택을 이용해서 계산

  - 피연산자를 만나면 스택에 `push`
  - 연산자를 만나면 필요한 만큼의 피연산자를 스택에서 `pop`해서 연산, 연산 결과를 다시 스택에 `push`
  - 수식이 끝나면 마지막으로 스택을 `pop`해서 출력



### 백트래킹

- 해를 찾는 도중 **==막히면==**(해가 아니면) 되돌아가서 다시 해를 찾아가는 기법
- **최적화(optimization)** 문제와 **결정(decision)** 문제를 해결할 수 있다
- 결정 문제 : 문제의 조건을 만족하는 해가 존재하는지 여부를 `yes or no`로 답하는 문제
  - 미로 찾기
  - n-Queen 문제
  - Map coloring
  - 부분 집합의 합(Subset Sum) 문제 등



#### 백트래킹 - n-Queen

~16~C~4~만큼에서 4!만큼으로 줄어듦

  행, 열

Q~1~(1, )

Q~2~(2, )

Q~3~(3, )

Q~4~(4, )

대각선 체크는 행, 열 차이로 기울기 따져서 





#### 백트래킹 - 부분집합

`n = 3`, `{A, B, C}`

- 선택지 = 2
- 선택 수 = n 

1) 포함하는 건 1, 포함하지 않는 건 0 (전부 0이면 공집합)

![1551154998738](../../../../../AppData/Roaming/Typora/typora-user-images/1551154998738.png)

2) 현재 위치를 알기 위해서 높이가 필요

3) 루트에서부터 단말 노드까지 가면 뭐요...?



```python
bits = [0] * 3 # 원소의 개수만큼 있어야 한다.
def subset(k, n):
    # 단말 노드, 모든 선택이 끝남
    if k == n:
    	print(bits)
    # 아직 선택해야 한다.
    else:
    	# 선택지(자식 노드)의 수만큼
    	for i in range(2):
            # 비트가 0일 때
            bits[k] = 0
            subset(k + 1, n)
            # 비트가 1일 때
            bits[k] = 1
            subset(k + 1, n)
        

# 0: 시작 상태, 3: 단말 노드의 높이
# 선택 수 = 0, 해야 할 선택 수 = 3
subset(0, 3)


for i range(2):
    for j in range(2):
        for k in range(2):
            print(i, j, k)
```

```python
arr = "ABC"
N = len(arr)
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        for k in range(N):
            if k == i or k == j:
                continue
            print(arr[i], arr[j], arr[k])

# 처음엔 3개 중에 하나, 다음엔 2개 중에 하나, 마지막 하나

arr = "ABC"
N = len(arr)
order = [0] * N

def perm(k, n):
    if k == n:
        # order[]에 저장된 순서를 확인
        return
    visit = [False] * N
    for i in range(k):
        visit[order[i]] = True
    for i in range(n):
        if visit[i]:
            continue
        order[k] = i
        perm(k + 1, n)


perm(0, N)
```

```python
# 비트 연산 망해라
def perm(k, n, visit):
    if k == n:
        print(order)
        return
    
    for i in range(k):
        if visit & (1 << i):
            continue
        order[k] = i
    	perm(k + 1, n, visit | (1 << i))

perm(0, N, 0)
```



### 퀵 정렬

- 분할 정렬은 두 부분으로 나누지만 퀵 정렬은 그럴 수도 있고 아닐 수도 있음

- 대신 합병처럼 후처리 작업이 없다

  ![1551161714911](../../../../../AppData/Roaming/Typora/typora-user-images/1551161714911.png)

  - L은 무조건 pivot보다 왼쪽에 있음
  - while문 안에 `a[L or R]`과 `a[pivot]`의 비교에서 한 쪽은 반드시 `=` 표시가 필요

  





