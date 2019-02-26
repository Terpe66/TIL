import sys
sys.stdin = open("workshop.txt")

for t in range(10):
    side = int(input())
    square = []
    S = []
    for _ in range(side):
        square.append(input().split())

    for row in range(100):
        for col in range(100):
            if square[col][row] == "0":
                continue
            if S:
                if square[col][row] == "2" and S[-1] == "1":
                    S.append("2")
                elif square[col][row] == "1" and S[-1] == "2":
                    S.append("1")
            else:
                if square[col][row] == "1":
                    S.append("1")
        if S[-1] == "1":
            S.pop()

    print(f"#{t + 1} {S.count('2')}")
