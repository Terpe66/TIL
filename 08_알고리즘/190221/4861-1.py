import sys
sys.stdin = open("4861.txt", "r")

for T in range(int(input())):
    line, length = map(int, input().split())
    charlist = []
    for char in range(line):
        charlist.append(input())
    minus = 0
    result = ""
    
    for row in range(line):
        col = 0
        while col + length - 1 < line:
            if result != "":
                break
            elif charlist[row][col] != charlist[row][col + length - 1 - minus]:
                col += 1
            else:
                idx = col + 1
                minus += 2
                while charlist[row][idx] == charlist[row][idx + length - 1 - minus]:
                    idx += 1
                    minus += 2
                    if idx == idx + length - 1 - minus or idx + 1 == idx + length - 1:
                        result = charlist[row][idx:idx+length]
                        break

