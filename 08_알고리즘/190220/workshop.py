import sys
sys.stdin = open("workshop.txt", "r")

for _ in range(int(input())):
    chardict = {"ZRO":0, "ONE":0, "TWO":0, "THR":0, "FOR":0, "FIV":0, "SIX":0, "SVN":0, "EGT":0, "NIN":0}
    test_case, num_len = input().split()
    input_num = list(map(str, input().split()))
    
    for char in input_num:
        chardict[char] += 1
    
    print(test_case)
    for key, value in chardict.items():
        for i in range(value):
            print(key, end=" ")
    print()