A = "()()((()))"
B = "((()((((()()((()())((()))))"

def pel(A):
    stack = []
    for i in range(len(A)):
        if A[i] == "(":
            stack.append(A[i])
        elif stack.pop() == "(":
            pass
    if stack:
        return False
    else:
        return True

print(pel(A))
print(pel(B))

stack = []
for i in range(len(A)):
    if A[i] == "(":
        stack.append(A[i])
    elif stack.pop() == "(":
        pass
if stack:
    print(False)
else:
    print(True)
