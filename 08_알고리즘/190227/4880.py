import sys
sys.stdin = open("4880.txt")

for T in range(int(input())):
    st = int(input())
    cards = input().split()
    half = (1+st)//2

    A, B = [], []
    for c in range(st):
        if c+1 <= half:
            A.append((c+1, cards[c]))
        elif c+1 > half:
            B.append((c+1, cards[c]))

    adiv, bdiv = [], []
    al, ar, bl, br = 1, half, half+1, st

    while ar - al > 2:
        ar = (al + ar) // 2
        if ar not in adiv:
            adiv.append(ar)
        if ar - al <= 2:
            al, ar = max(adiv) + 1, half
    adiv.append(half)
    adiv.sort()

    while br - bl > 2:
        br = (bl + br) // 2
        if br not in bdiv:
            bdiv.append(br)
        if br - bl <= 2:
            bl, br = max(bdiv) + 1, st
    bdiv.append(st)
    bdiv.sort()

    ii = 0
    while len(A) > 1:
        ii += 1
        print(ii)
        if adiv:
            ad = adiv.pop(0)
            a = []
            while len(A) > 0 and ad-3 < A[0][0] < ad+1:
                a.append(A.pop(0))

            while len(a) > 1:
                if len(a) >= 2:
                    if a[0][0] < a[1][0]:
                        a1, a2 = a.pop(0), a.pop(0)
                    else:
                        a2, a1 = a.pop(0), a.pop(0)

                if a1[1] == "1":
                    if a2[1] in ("1", "3"):
                        a.append(a1)
                    else:
                        a.append(a2)
                elif a1[1] == "2":
                    if a2[1] in ("2", "1"):
                        a.append(a1)
                    else:
                        a.append(a2)
                elif a1[1] == "3":
                    if a2[1] in ("3", "2"):
                        a.append(a1)
                    else:
                        a.append(a2)
                else:
                    print("hahaha")
            A.append(a.pop())
        elif not adiv:
            if A[0][0] < A[1][0]:
                a1, a2 = A.pop(0), A.pop(0)
                if a1[1] == "1":
                    if a2[1] in ("1", "3"):
                        A.append(a1)
                    else:
                        A.append(a2)
                elif a1[1] == "2":
                    if a2[1] in ("2", "1"):
                        A.append(a1)
                    else:
                        A.append(a2)
                elif a1[1] == "3":
                    if a2[1] in ("3", "2"):
                        A.append(a1)
                    else:
                        A.append(a2)
            else:
                A.append(A.pop(0))

    while len(B) > 1:
        if bdiv:
            bd = bdiv.pop(0)
            b = []
            while len(B) > 0 and bd - 3 < B[0][0] < bd + 1:
                b.append(B.pop(0))

            while len(b) > 1:
                if len(b) >= 2:
                    if b[0][0] < b[1][0]:
                        b1, b2 = b.pop(0), b.pop(0)
                    else:
                        b2, b1 = b.pop(0), b.pop(0)

                if b1[1] == "1":
                    if b2[1] in ("1", "3"):
                        b.append(b1)
                    else:
                        b.append(b2)
                elif b1[1] == "2":
                    if b2[1] in ("2", "1"):
                        b.append(b1)
                    else:
                        b.append(b2)
                elif b1[1] == "3":
                    if b2[1] in ("3", "2"):
                        b.append(b1)
                    else:
                        b.append(b2)
            B.append(b.pop())
        elif not bdiv:
            if B[0][0] < B[1][0]:
                b1, b2 = B.pop(0), B.pop(0)
                if b1[1] == "1":
                    if b2[1] in ("1", "3"):
                        B.append(b1)
                    else:
                        B.append(b2)
                elif b1[1] == "2":
                    if b2[1] in ("2", "1"):
                        B.append(b1)
                    else:
                        B.append(b2)
                elif b1[1] == "3":
                    if b2[1] in ("3", "2"):
                        B.append(b1)
                    else:
                        B.append(b2)
            else:
                B.append(B.pop(0))

    a, b = A.pop(), B.pop()
    if a[1] == "1":
        if b[1] in ("1", "3"):
            print(f"#{T+1} {a[0]}")
        else:
            print(f"#{T+1} {b[0]}")
    elif a[1] == "2":
        if b[1] in ("2", "1"):
            print(f"#{T+1} {a[0]}")
        else:
            print(f"#{T+1} {b[0]}")
    elif a[1] == "3":
        if b[1] in ("3", "2"):
            print(f"#{T+1} {a[0]}")
        else:
            print(f"#{T+1} {b[0]}")

    #
    #
    #
    #
    # d = (1+half)//2
    # while True:
    #     div.append(d)
    #     if (1+div[-1])//2 not in (2, 3)
    #
    #
    # while len(Sa) > 1:
    #     if Sa[0][0] <= half:
    #         if Sa[0][0] < Sa[1][0] <= half:
    #             A, B = Sa.pop(0), Sa.pop(0)
    #             if A[1] == "1":
    #                 if B[1] in ("1", "3"):
    #                     Sa.append(A)
    #                 else:
    #                     Sa.append(B)
    #             elif A[1] == "2":
    #                 if B[1] in ("2", "1"):
    #                     Sa.append(A)
    #                 else:
    #                     Sa.append(B)
    #             elif A[1] == "3":
    #                 if B[1] in ("3", "2"):
    #                     Sa.append(A)
    #                 else:
    #                     Sa.append(B)
    #         else:
    #             Sa.append(Sa.pop(0))
    #
    # while len(Sb) > 1:
    #     if Sb[0][0] > half:
    #         if Sb[0][0] < Sb[1][0] <= st:
    #             A, B = Sb.pop(0), Sb.pop(0)
    #             if A[1] == "1":
    #                 if B[1] in ("1", "3"):
    #                     Sb.append(A)
    #                 else:
    #                     Sb.append(B)
    #             elif A[1] == "2":
    #                 if B[1] in ("2", "1"):
    #                     Sb.append(A)
    #                 else:
    #                     Sb.append(B)
    #             elif A[1] == "3":
    #                 if B[1] in ("3", "2"):
    #                     Sb.append(A)
    #                 else:
    #                     Sb.append(B)
    #         else:
    #             Sb.append(Sb.pop(0))
    #
    # A, B = Sa.pop(), Sb.pop()
    # if A[1] == "1":
    #     if B[1] in ("1", "3"):
    #         print(f"#{T+1} {A[0]}")
    #     else:
    #         print(f"#{T+1} {B[0]}")
    # elif A[1] == "2":
    #     if B[1] in ("2", "1"):
    #         print(f"#{T+1} {A[0]}")
    #     else:
    #         print(f"#{T+1} {B[0]}")
    # elif A[1] == "3":
    #     if B[1] in ("3", "2"):
    #         print(f"#{T+1} {A[0]}")
    #     else:
    #         print(f"#{T+1} {B[0]}")
    #
    #
    #
    #




        
    # print(f"#{T+1} {ans}")

# for t in range(int(input())):
#     st = int(input())
#     cards = input().split()
#     A = []
#     B = []
    
#     for a in range(1, len(cards)//2+1, 2):
#         if cards[a-1] == "1":
#             if cards[a] == "1":
#                 A.append((a-1, "1"))
#             elif cards[a] == "2":
#                 A.append((a, "2"))
#             elif cards[a] == "3":
#                 A.append((a-1, "1"))
#         if cards[a-1] == "2":
#             if cards[a] == "2":
#                 A.append((a-1, "2"))
#             elif cards[a] == "2":
#                 A.append((a, "2"))
#             elif cards[a] == "3":
#                 A.append((a-1, "1"))
                
#     for b in range(len(cards)//2 + 1, len(cards), 2):
#         if cards[b-1] == "1":
#             if cards[b] == "1":
#                 B.append((b-1, "1"))
#             elif cards[b] == "2":
#                 B.append((b, "2"))
#             elif cards[b] == "3":
#                 B.append((b-1, "1"))
    
#     for a in A:
#         if cards[a[0]] 
                


# arr = [3, 5, 2, 7, 9, 8, 1, 2, 4]

# def getMax(lo, hi):
#     if lo == hi:
#         return arr[lo]
    
#     ret = getMax(lo, hi -1)
    
#     return ret if ret > arr[hi] else arr[hi]

# print(getMax(0, len(arr) - 1))

# def getMax(lo, hi):
#     print(lo, hi)
#     if lo == hi:
#         return arr[lo]
#     mid = (lo + hi) >> 1
#     l = getMax(lo, mid)
#     r = getMax(mid + 1, hi)
    
#     return r if r > l else L

# print(getMax(0, len(arr) - 1))
