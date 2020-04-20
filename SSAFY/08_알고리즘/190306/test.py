def inorder(v):
    if v == 0:
        return 0

    l = inorder(L[v])
    r = inorder(R[v])
    return l + r + 1

V, E = map(int, input().split())
arr = list(map(int, input().split()))
L = [0] * (V + 1)
R = [0] * (V + 1)

