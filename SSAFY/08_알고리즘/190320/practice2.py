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
