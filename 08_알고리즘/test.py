test_num = 1

s_len = int(input())
s_list = list(map(int, input().split()))

sight_sum = 0
for i in range(2, s_len - 2):
    sight = 0
    if s_list[i] - s_list[i-1] > 0 and s_list[i] - s_list[i-2] > 0:
        left_sight = s_list[i] - max(s_list[i-1], s_list[i-2])
        if s_list[i] - s_list[i+1] > 0 and s_list[i] - s_list[i+2] > 0:
            right_sight = s_list[i] - max(s_list[i+1], s_list[i+2])
            if left_sight > right_sight:
                sight_sum += right_sight
            else:
                sight_sum += left_sight


print(f"#{test_num} {sight_sum}")
test_num += 1


