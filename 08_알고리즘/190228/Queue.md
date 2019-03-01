# 190228 Queue

### 큐의 특성

- 스택처럼 삽입 삭제의 위치가 제한적인 자료 구조
  - 스택은 뒤로 넣고 뒤로 빼는 방식, 큐는 뒤로 넣고 앞으로 빼는 방식
  - 선입선출구조(FIFO : First In First Out)
- 큐의 꼬리(Rear, Tail) == 스택의 Top, 머리(Front) == 스택의 Head
- front와 rear가 -1이 아니면서, 같은 곳을 point하면 큐가 비어있는 걸 알 수 있음!



```python
QSIZE = 100
Q = [0] * QSIZE
front = rear = -1
def push(item):
    global rear
    rear += 1
    Q[rear] = item

def pop():
    global front
    front += 1
    return Q[front]

def empty(): # 스펙이나 큐에서 꺼낼 때 꼭 empty인지 아닌지 체크하고 꺼낼 것
    return front == rear

for i in range(5):
    push(i)

while not empty():
    print(pop())

```



```python
from collections import deque

Q = deque()
for i in range(5):
    Q.append(i)
    
while len(Q) > 0:
    print(Q.popleft())
    
test = [() for _ in range(5)]
test[0] = (0, 0)
test[1] = (1, 1)
a = (3, 3)
test[3] = a
print(test)

```

#### 선형 큐 이용시 문제

- 잘못된 포화 상태 인식 : 원소를 계속 삭제하면서 front가 뒤로 밀려 rear와 같아질 경우, 실제로는 공간이 있지만 인식하지 못해서 큐를 사용하지 못할 때
- 해결 방법
  - 삭제할 때마다 원소를 앞으로 이동시킨다(원소를 이동시키는 데 시간이 소요됨)
  - 1차원 배열을 사용하지만 논리적으로는 처음과 끝이 이어진 원형 형태 큐를 사용

#### 원형 큐 index 순환

- front와 rear의 위치가 배열의 마지막 index인 n-1을 가리킨 후엔 논리적 순환으오 다시 맨 처음 index인 0으로 이동(나머지 연산자 mod를 사용)

```python
QSIZE = 100
Q = [0] * QSIZE
front = rear = -1
def full():
    if (rear + 1) % QSIZE = front:
        return True
    return False

def push(item):
    global rear
    rear =  (rear + 1) % QSIZE
    Q[rear] = item

def pop():
    global front
    front = (front + 1) % len(Q)
    return Q[front]

def empty(): # 스펙이나 큐에서 꺼낼 때 꼭 empty인지 아닌지 체크하고 꺼낼 것
    return front == rear

for i in range(5):
    push(i)

while not empty():
    print(pop())
```



D[]: 최단거리

P[]: 최단경로 트리

현재 정점 v, 인접 정점 w

v에서 w로 가는 것

D[w] = D[v] + 1

v에서 w로 갈 때 하나 차이라 +1

D[v]에는 최단경로?

P[w] = v

P[w] 바로 이전에 방문한 정점

|      |  1   |  2   |  3   |  4   |  5   |  6   |  7   |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  D   |  0   |  1   |  1   |  2   |  2   |  3   |  2   |
|  P   |  1   |  1   |  1   |  2   |  2   |  4   |  3   |



```python
#1) 1을 방문, Q에 1을 집어 넣음, D에 0, P에 1
#2) Q에서 1을 꺼내고 인접 정점 2, 3을 본다(?)
#3) 2에 방문, Q에 2, 3을 집어 넣음 D값을 1로 바꾸고, 1번 거쳐 가서 P에 1을 집어 넣음
#4) ...
# D는 시작에서부터 이동한 거리, P는 바로 이전 정점
# 모두 방문하면 끗?

```

```python
# DFS는 하나 발견하고 빠지는데 BFS는 다 돌아본다
from queue import Queue
def BFS(s, G):
    visit = [False] * (V + 1)
    D = [0] * (V + 1) # 정점의 수 만큼
    P = [0] * (V + 1)

    Q = Queue() # 
    Q.put(s)		# 시작점 큐에 삽입
    visit[s] = True	# 시작점 방문 표시
    print(s, end=" ")
    while not Q.empty():	# 빈 큐가 아닐 동안
        v = Q.get()			# 큐에서 가져온다
        for w in G[v]:
            if not visit[w]:
                D[w] = D[v] + 1
                # P[w] = v DFS일 때?
                Q.put(W)
                print(w, end=" ")


import sys
sys.stdin = open("BFS_input.txt")
V, E = map(int, input().split())
G = [[] for _ in range(V + 1)]

for i in range(E):
```



