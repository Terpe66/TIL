print("!", __name__)

# import math_functions
# 
# math_functions.cube(5)
# math_functions.average([1, 2, 3])

from math_functions import cube, average
# 위에서 __name__을 프린트할 경우, 해당 파일에 있는 건 __main__이 나오지만, from ~ import 같은 경우엔 해당 파일명이 나옴

print(average([1, 2, 3]))

