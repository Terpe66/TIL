import sys
sys.stdin = open("workshop.txt")

def read(node):
    for i in range(1, length+1):
        if len(node[i]) < 4:
            root = i
            break

    def find(root):
        if node[root][1]:
            find(node[root][1])
        print(node[root][0], end="")
        if node[root][2]:
            find(node[root][2])

    find(root)

for t in range(10):
    length = int(input())

    node = [ [] for _ in range(length+1) ]
    inputs = []
    string = [""] * (length + 1)
    for _ in range(length):
        inputs.append(input().split())

    for i in range(length):
        node[int(inputs[i][0])].append(inputs[i][1])
        if len(inputs[i]) >= 3:
            node[int(inputs[i][0])].append(int(inputs[i][2]))
            if len(inputs[i]) == 4:
                node[int(inputs[i][0])].append(int(inputs[i][3]))
            else:
                node[int(inputs[i][0])].append(0)
        else:
            node[int(inputs[i][0])].append(0)
            node[int(inputs[i][0])].append(0)

    for i in range(1, length+1):
        if node[i][1] == 0 and node[i][2] == 0:
            continue
        if node[i][1]:
            node[node[i][1]].append(i)
        if node[i][2]:
            node[node[i][2]].append(i)


    print(f"#{t+1}", end=" ")
    read(node)
    print()




