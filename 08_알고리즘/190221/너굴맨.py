# 안에서부터 밖으로 뻗어나감 (?)

for t in range(10):
    box = []
    quest = input()
    for h in range(100):
        dummy = [x for x in input()]
        box += [dummy]
    max_len = 0
    for i in range(100):
        for j in range(100):
            cnt_xo = 1
            cnt_xe = 0
            cnt_yo = 1
            cnt_ye = 0
            kxo = 1
            while j - kxo >= 0 and j + kxo < 100:
                if box[i][j - kxo] == box[i][j + kxo]:
                    cnt_xo += 2
                    kxo += 1
                    if cnt_xo > max_len:
                        max_len = cnt_xo
                else:
                    cnt_xo = 0
                    break
            kyo = 1
            while j - kyo >= 0 and j + kyo < 100:
                if box[j - kyo][i] == box[j + kyo][i]:
                    cnt_yo += 2
                    kyo += 1
                    if cnt_yo > max_len:
                        max_len = cnt_yo
                else:
                    cnt_yo = 0
                    break
            kxe = 0
            while j - kxe >= 0 and j + kxe < 99:
                if box[i][j - kxe] == box[i][j + kxe + 1]:
                    cnt_xe += 2
                    kxe += 1
                    if cnt_xe > max_len:
                        max_len = cnt_xe
                else:
                    cnt_xe = 0
                    break
            kye = 0
            while j - kye >= 0 and j + kye < 99:
                if box[j - kye][i] == box[j + kye + 1][i]:
                    cnt_ye += 2
                    kye += 1
                    if cnt_ye > max_len:
                        max_len = cnt_ye
                else:
                    cnt_ye = 0
                    break
    print(f'#{t + 1} {max_len}')


# 선생님이 수정(?)

for t in range(10):
    quest = input()
    arr = []
    for h in range(100):
        arr.append(input())

    max_len = 0
    for i in range(100):
        for j in range(100):
            # 길이가 짝수
            L, R = j, j + 1
            cnt = 0
            while L >= 0 and R < 100:
                if arr[i][L] == arr[i][R]:
                    cnt += 2
                    L, R = L - 1, R + 1
                else:
                    break
            max_len = max(max_len, cnt)
            
            # 길이가 홀수
            L, R = j, j + 1
            cnt = 0
            while L >= 0 and R < 100:
                if arr[L][i] == arr[R][i]:
                    cnt += 2
                    L, R = L - 1, R + 1
                else:
                    break
            max_len = max(max_len, cnt)
            
            # 세로 홀수
            L, R = j, j + 1
            cnt = 1
            while L >= 0 and R < 100:
                if arr[L][i] == arr[R][i]:
                    cnt += 2
                    L, R = L - 1, R + 1
                else:
                    break
            max_len = max(max_len, cnt)
            # ???
    print(max_len)

# 선생님 수정 2
for t in range(10):
    quest = input()
    arr = []
    for h in range(100):
        arr.append(input())

    max_len = 0
    for row in range(100): # 모든 행에 반복되는 내용
        for start in range(100): # 한 행에 반복되는 내용
            for end in range(99, start, -1):
                L = end - start + 1
                if max_len > L:
                    break
                cnt = L // 2
                i = 0
                while i < cnt:
                    if arr[row][start + i] != arr[row][end - i]:
                        # 같지 않으면 빠져나감
                        break
                    i += 1
                if i == cnt:
                    max_len = L