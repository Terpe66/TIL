import sys
sys.stdin = open("input.txt")

for test_case in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))

    ans = 0
    for i in range(2, N - 2):
        maxH = max(arr[i - 2], arr[i - 1], arr[i + 1], arr[i + 2])
        if arr[i] > maxH:
            ans = ans + (arr[i] - maxH)
    print(f"#{test_case} {ans}")

