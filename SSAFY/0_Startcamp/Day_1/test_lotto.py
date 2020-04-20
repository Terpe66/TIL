li = [-2, -3, 5, 6]

# 양수만 반환하는 리스트
def ft(li):
    result = []
    for e in li:
        if e > 0:
            result.append(e)
        else:
            pass
    return result


# filter 함수 사용시
def positive(x):
  return x > 0

list(filter(positive, li))

# filter + lambda 함수 사용시
list(filter(lambda x: x > 0, li))
