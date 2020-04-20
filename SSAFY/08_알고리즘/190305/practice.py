import sys
sys.stdin = open("practice.txt")

def inorder(v):
    if v == 0:
        return
    # 전위
    inorder(L[v])
    # 후위
    inorder(R[v])

#1 트리 높이를 계산하는 함수
def treeHeight(root, cnt=0):
    global root_cnt
    if info[root][0] == 0 and info[root][1] == 0:
        root_cnt = cnt
    else:
        for i in range(2):
            if visited[info[root][i]] == 0 and info[root][i]:
                treeHeight(info[root][i], cnt+1)

#2 높이가 3인 노드들을 출력하시오 (7, 8, 9, 10, 11)
def sameHeight(height):
    for i in range(1, Node+1):
        if info[i][2] == 0:
            root = i
            break

    def findHeight(root, cnt=0):
        if cnt == height:
            print(root, end=" ")
            return
        else:
            for i in range(2):
                if visited[info[root][i]] == 0 and info[root][i]:
                    findHeight(info[root][i], cnt+1)
    findHeight(root)


#3 3번 노드가 루트인 트리의 전체 노드 수 (8)
#4 8번 노드와 10번 노드의 공통 조상을 출력하시오 (3)


Node, Line = map(int, input().split())
node = list(map(int, input().split()))
info = [ [0] * 3 for _ in range(Node+1) ]
visited = [0] * (Node+1)
for i in range(0, Line * 2, 2):
    u, v = node[i], node[i + 1]
    if info[u][0]:
        info[u][1] = v
    else:
        info[u][0] = v
    info[v][2] = u

root_cnt = 0
#1
treeHeight(3)
print(root_cnt)

root_height = 0
#2
sameHeight(3)