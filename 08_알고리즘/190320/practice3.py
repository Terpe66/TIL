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