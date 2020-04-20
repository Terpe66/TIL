import sys
sys.stdin = open("workshop.txt", "r")

for _ in range(int(input())):
    chartuple = ("ZRO ", "ONE ", "TWO ", "THR ", "FOR ", "FIV ", "SIX ", "SVN ", "EGT ", "NIN ")
    numlist = [0] * 10
    test_case, num_len = input().split()
    input_num = tuple(map(str, input().split()))
    
    for char in input_num:
        numlist[chartuple.index(char)] += 1

    print(test_case)
    for i in range(10):
        print(chartuple[i] * numlist[i])
    print()