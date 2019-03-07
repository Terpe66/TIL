import sys
sys.stdin = open("workshop.txt")

def math(start):
    if type(node[start]) == int:
        return node[start]
    if node[start][0] == "+":
        return math(node[start][1]) + math(node[start][2])
    if node[start][0] == "-":
        return math(node[start][1]) - math(node[start][2])
    if node[start][0] == "*":
        return math(node[start][1]) * math(node[start][2])
    if node[start][0] == "/":
        return math(node[start][1]) // math(node[start][2])

for t in range(10):
    N = int(input())
    node = [0] * (N + 1)

    for i in range(N):
        inputs = list(map(str, input().split()))
        if len(inputs) > 2:
            node[int(inputs[0])] = [inputs[1], int(inputs[2]), int(inputs[3])]
        else:
            node[int(inputs[0])] = int(inputs[1])

    print(f"#{t+1} {math(1)}")