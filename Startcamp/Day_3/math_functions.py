print(__name__)

def average(numbers):
    return sum(numbers) / len(numbers)

def cube(x):
    return x * x * x

# 다른 파일에서 불러올 때 안 나오게 함
if __name__ == '__main__':
    my_score = [79, 84, 66, 93]
    print(my_score, '의 평균은 ', average(my_score), '입니다.')
    print(cube(3))