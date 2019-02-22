import sys
sys.stdin = open("workshop.txt", "r")

for _ in range(10):
    t = int(input())

    ladder = []
    for x in range(100):
        ladder.append(list(map(int, input().split())))

    startpoint = []
    for x in range(100):
        if ladder[99][x] == 2:
            startpoint.append(x)

    for sp in startpoint:
        row, col = 99, sp
        while row > 0:
            if row == 0:
                while ladder[row][col + 1] == 0:
                    row -= 1
                    # print(row, col)
                while ladder[row][col + 1] == 1:
                    col += 1
                    # print(row, col)
                row -= 1
                # print(row, col)
            
            elif col == 100:
                while ladder[row][col - 1] == 0:
                    row -= 1
                    # print(row, col)
                while ladder[row][col - 1] == 1:
                    col -= 1
                    # print(row, col)

            else:
                while row > 0 and col < 99 and not ladder[row][col + 1] and not ladder[row][col - 1]:
                    row -= 1
                    # print(row, col)
                if row < 99 and ladder[row][col + 1]:
                    while col < 99 and ladder[row][col + 1]:
                        col += 1
                        # print(row, col)
                    row -= 1
                    # print(row, col)
                elif ladder[row][col - 1]:
                    while col > 0 and ladder[row][col - 1]:
                        col -= 1
                        # print(row, col)
                    row -= 1
                    # print(row, col)
        break
    print("#{} {}".format(t, col))
