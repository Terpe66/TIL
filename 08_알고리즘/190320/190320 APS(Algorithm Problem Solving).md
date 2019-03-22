# 190320 APS(Algorithm Problem Solving)

### Start

1) SW 문제 해결 : 단순한 방법에서 시작할 수 있을까?(브루트 포스)



2) 복잡도 분석

==알고리즘== : 유한한 단계를 통해 문제를 해결하기 위한 절차나 방법. 주로 컴퓨터 용어로 쓰이며, 컴퓨터가 어떤 일을 수행하기 위한 단계적 방법



- 알고리즘의 효율
  - 효율성 ↔ 복잡도(복잡도가 높을수록 효율성 저하)
- 시간 복잡도 분석 : 복잡도의 점근적 표기

|      | O(Big-O) 표기        | Ω(Big-Omega) 표기    | θ(Big-Theta) 표기            |
| ---- | -------------------- | -------------------- | ---------------------------- |
|      | 복잡도의 점근적 상한 | 복잡도의 점근적 하한 |                              |
|      | 최악의 경우          | 최소의 경우          | 평균적인 경우(동일한 증가율) |



3) 비트 연산

| 연산자 | 기능                                        |
| ------ | ------------------------------------------- |
| &      | 비트 단위로 AND 연산                        |
| \|     | 비트 단위로 OR 연산                         |
| ^      | 비트 단위로 XOR 연산(같으면 0 다르면 1)     |
| ~      | 단항 연산자로서 피연산자의 모든 비트를 반전 |
| <<     | 피연산자의 비트 열을 왼쪽으로 이동          |
| **>>** | 피연산자의 비트 열을 오른쪽으로 이동        |

**1 << n**

- 2^n^의 값, 원소가 n개일 경우의 모든 부분 집합의 수



**i & (1 << j)**

- i의 j번째 비트가 1인지 아닌지 의미



**보수**

1의 보수 : 0을 1로 바꾼다

2의 보수 : 0을 1로 바꾸고 최하위 비트에 1을 더한다



**연습문제 1**

```python
# 0000000111 1000000110 0000011110 0110000110 0001111001 1110011111 1001100111

import sys
sys.stdin = open("test.txt")

test = input().replace(" ", "")

i, idx = 0, 7
while idx <= len(test):
    print(int(test[i:idx], 2))
    i = idx
    idx += 7
```



**에디안**

```python
import sys
x = 0x01020304

print(x.to_bytes(4, byteorder = "big"))
print(x.to_bytes(4, byteorder = "little"))

print(sys.byteorder)

print(int.from_bytes(b"\x04\x03\x02\x01", byteorder = "big"))
print(int.from_bytes(b"\x04\x03\x02\x01", byteorder = "little"))

```



```python
bina = bin(1024)
octa = oct(1024)
hexa = hex(1024)
print(bina, octa, hexa)

print(type(bina))
print(type(int(bina, 2)))

print(int(bina, 2))
print(int(octa, 8))
print(int(hexa, 16))
```



**연습문제 2**

```python
import sys
sys.stdin = open("practice2.txt")

for _ in range(2):
    practice2 = input()
    binum = ""

    for b in practice2:
        output = ""
        for i in range(3, -1, -1):
            if int(b, 16) & (1 << i):
                output += "1"
            else:
                output += "0"
        binum += output

    i = 0
    ten = []
    print(f"#{_ + 1}")
    while i < len(binum):
        print(int(binum[i:i+7], 2), end=" ")
        i += 7
    print()
```



**연습문제 3**

```python
import sys
sys.stdin = open("practice3.txt")

pw = ["001101", "010011", "111011", "110001", "100011", "110111", "001011", "111101", "011001", "101111"]

for t in range(2):
    practice = input()
    lock = ""

    for b in practice:
        output = ""
        for i in range(3, -1, -1):
            if int(b, 16) & (1 << i):
                output += "1"
            else:
                output += "0"
        lock += output

    i = 0
    print(f"#{t + 1}")
    while i < len(lock):
        for p in range(10):
            if lock[i:i+6] == pw[p]:
                print(p, end=" ")
                i = i + 6
        i += 1
    print()
```

