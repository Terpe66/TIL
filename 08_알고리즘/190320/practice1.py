import sys
sys.stdin = open("test.txt")

test = input().replace(" ", "")

i, idx = 0, 7
while idx <= len(test):
    print(int(test[i:idx], 2))
    i = idx
    idx += 7

print("=======")
print(0b0000000)
print(0b1111000)
print(0b0001100)
print(0b0000111)
print(0b1001100)
print(0b0011000)
print(0b0111100)
print(0b1111001)
print(0b1111100)
print(0b1100111)
