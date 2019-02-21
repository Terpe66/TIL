import sys
sys.stdin = open("workshop.txt", "r")

for T in range(int(input())):
    pipe = int(input())
    input_pipe = list(map(int, input().split()))
    pipes = []
    pipe_ht = []
    for p in input_pipe:
        if len(pipe_ht) < 2:
            pipe_ht.append(p)
        if len(pipe_ht) == 2:
            pipes.append(pipe_ht)
            pipe_ht = []            
    for i in range(len(pipes)):
        cnt = 0
        for j in range(len(pipes)):
            if pipes[i][0] != pipes[j][1]:
                cnt += 1
        else:
            if cnt == len(pipes):
                pipes[0], pipes[i] = pipes[i], pipes[0]
                break
    idx = 0
    for j in range(len(pipes)-1):
        for i in range(1, len(pipes)):
            if pipes[idx][1] == pipes[i][0]:
                idx += 1
                pipes_ = pipes[idx]
                pipes[idx] = pipes[i]
                pipes[i] = pipes_
            
    print("#{}".format(T+1), end=" ")
    for i in range(len(pipes)):
        print(pipes[i][0], pipes[i][1], end=" ")
    print()
        