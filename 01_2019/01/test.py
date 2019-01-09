def antant(n, H1=[], H2=[], H3=[], count=0):
    
    if n < 2:
        return n
# 1) 1번에 n 숫자 넣음    
    if H1 == [] and H2 == [] and H3 == []:
        for top in range(n):
            H1 += [top]
            
    while True:
        if len(H2) == n or len(H3) == n:
            break
    # 10) 1이 비어있을 때 2가 3보다 작으면 >>> 2를 3으로
        if H1 == []:
            if H2[0] < H3[0]:
                H3.insert(0, H2[0])
                del H2[0]
                count += 1
                return antant(n, H1, H2, H3, count)
    # 11) 1이 비어있을 때 2가 3보다 크면 >>> 2를 1로
            if H2[0] > H3[0]:
                H1.insert(0, H2[0])
                del H2[0]
                count += 1
                return antant(n, H1, H2, H3, count)
    # 2) 2가 비어있을 때 >>> 1을 2로    
        if H2 == []:
            H2.insert(0, H1[0])
            del H1[0]
            count += 1
            return antant(n, H1, H2, H3, count)
    # 3) 3이 비어있고 1이 2보다 크면 >>> 1을 3으로    
        if H3 == []:
            if H1[0] > H2[0]:
                H3.insert(0, H1[0])
                del H1[0]
                count += 1
                return antant(n, H1, H2, H3, count)
    # 4) 3이 비어있고 1이 2보다 작으면 >>> 1을 2로        
            if H1[0] < H2[0]:
                H2.insert(0, H1[0])
                del H1[0]
                count += 1
                return antant(n, H1, H2, H3, count)
    # 13 3이 비어있지 않고 1이 2보다 크고 3보다 작으면 >>> 1을 3으로
        if H3 != []:
            if H1[0] > H2[0] and H1[0] < H3[0]:
                H3.insert(0, H1[0])
                del H1[0]
                count += 1
                return antant(n, H1, H2, H3, count)
    # 5) 3이 비어있지 않고 1이 2보다 크고 2가 3보다 작으면 >>> 2를 3으로
            if H1[0] > H2[0] and H2[0] < H3[0]:
                H3.insert(0, H2[0])
                del H2[0]
                count += 1
                return antant(n, H1, H2, H3, count)
    # 6) 3이 비어있지 않고 3이 1보다 작으면 >>> 3을 1로
            if H3[0] < H1[0]:
                H1.insert(0, H3[0])
                del H3[0]
                count += 1
                return antant(n, H1, H2, H3, count)
    # 7) 3이 비어있지 않고 3이 2보다 작으면 >>> 3을 2로        
            if H3[0] < H2[0]:
                H2.insert(0, H3[0])
                del H3[0]
                count += 1
                return antant(n, H1, H2, H3, count)
    # 12) 3이 비어있지 않고 2가 1보다 크면 >>> 2를 3으로
            if H2[0] > H1[0]:
                H3.insert(0, H2[0])
                del H2[0]
                count += 1
                return antant(n, H1, H2, H3, count)
    # 9) 3이 비어있지 않고 1이 2보다 작으면 >>> 1을 2로        
            if H1[0] < H2[0]:
                H2.insert(0, H1[0])
                del H1[0]
                count += 1
                return antant(n, H1, H2, H3, count)

    # 8) 3이 비어있지 않고 2가 3보다 크고 1이 비어있으면 >>> 2를 1로
            if H2[0] > H3[0] and H1 == []:
                H1.insert(0, H2[0])
                del H2[0]
                count += 1
                return antant(n, H1, H2, H3, count)

    return count
    

antant(5)