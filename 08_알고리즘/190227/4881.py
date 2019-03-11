import sys
sys.stdin = open("4881.txt")

def mini(row, col, sum_num=0):
    global N, min_sum
    for r in range(row):
        if c_board[r] == col:
            return

    sum_num += board[row][col]
    if sum_num > min_sum:
        return

    if row == N-1:
        if min_sum > sum_num:
            min_sum = sum_num
            return

    c_board[row] = col
    for j in range(N):
        mini(row + 1, j, sum_num)


for t in range(int(input())):
    N = int(input())

    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))

    min_sum = 10 * N
    c_board = [0] * N
    for i in range(N):
        mini(0, i)

    print(f"#{t+1} {min_sum}")

