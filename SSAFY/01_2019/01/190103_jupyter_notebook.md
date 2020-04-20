# 01. Python Intro

### 식별자

- 영어, 숫자, _로 구성된다

  - 첫 글자에는 숫자가 올 수 없다.
  - 영어는 대소문자를 구별한다.

- 일부 예약어는 사용할 수 없다.

  - False, True, None, and, as, break, continue, def, del, if, elif, else, for, from, global, import, in, return, while, assert, class, except, finally, is, lambda, nonlocal, not, or, pass, raise, try, with, yield

  - 전체 예약어는 아래 방법으로 확인 가능

    ```python
    import keyword
    print(keyword.kwlist)
    ```

  - 사용 가능한 예약어에 변수를 입력할 경우, 이후엔 그 예약어를 실행할 수 없다.

    ```python
    cf) 예약어에 변수를 입력했을 경우
    
    str = "string"
    str(10)
    
    del str
    이렇게 변수를 제거해주면 사용 가능해진다.
    ```



### 인코딩

```python
기본적으로 utf-8로 설정되어 있으나 필요한 경우
-*- coding: utf-8 -*-을 제일 상단에 선언한다.
```



### 주석(Comment)

- 가장 앞에 #을 붙이고 사용한다.

  ```python
  # 옳은 예시
  	# 틀린 예시
  ```

- docstring은 2가지 방법으로 입력할 수 있다.

  ```python
  # """을 사용해 함수나 클래스 선언 후 설명하는 경우
  def test(a, b):
  	"""
  	이것은 docstring을 설명하는 test 함수입니다.
  	a와 b를 곱한 값을 return합니다.
  	"""
  	return a * b
  
  # __doc__ 함수를 사용해서 설명을 입력하는 경우
  test.__doc__ = "이것은 새로운 설명을 입력하는 방법입니다. 이 경우 기존에 입력한 docstring이 있더라도 사라집니다."
  test.__doc__ += "이것은 새로운 설명을 입력하는 방법입니다. 이 경우엔 기존에 입력한 docstring과 함께 입력됩니다."
  ```



### 코드 라인

- html이나 css를 하면 ;로 헷갈리지만 한 줄로 표기할 때 외에는 ;을 사용하지 않는다.

  ```python
  # 보통 ;이 아니라 :을 사용한다.
  for t in test:
  
  # "test"와 "입니다."를 같이 출력하고 싶은 경우
  print("test")
  print("입니다.")
  혹은
  print("test"); print("입니다.")
  두 가지 경우로 사용할 수 있다.
  ```

- 함수가 길어지는 등 여러 줄로 작성할 경우 \을 사용하면 내려써도 인식이 가능하다.

  ```python
  # t가 "test를 하고 있습니다."일 경우 t를 출력하는 함수
  t = "test를 하고 있습니다."
  if t \
  == "test를 하고 있습니다.":
  	print(t)
  
  # 아래의 경우엔 에러
  if t
  == "test를 하고 있습니다.":
  	print(t)
  ```
  - [list], {set}, {dict}, (tuple)을 입력할 땐 \ 없이 내려써도 인식이 가능하다. 



### 수치형(Numbers)

- 정수는 int, 실수는 float, 복소수는 complex로 표현된다.

  - 복소수 기억 안 나는데 파이썬 공부하다가 수학 공부하게 생겼다.

- 2진수는 binary 0b숫자, 8진수는 octal 0o숫자, 16진수는 hexadecimal 0x숫자로 표현한다.

  ```python
  # n진수 2, 8, 10, 16
  
  binary_number = 0b100 # 2진법
  octal_number = 0o777 # 8진법
  decimal_number = 2019
  hexadecimal_number = 0xfff # 16진법
  print(f"\
  2진수: {binary_number},\
  8진수: {octal_number},\
  10진수: {decimal_number},\
  16진수: {hexadecimal_number}")
  ```
  - 파이썬에서는 C계열 프로그래밍 언어랑 다르게 정수 자료형에서 오버플로우가 없다.

    ```python
    # 무슨 말인지는 모르겠는데 일단 써놓는다.
    # arbitrary-precision arithmetic를 사용하기 때문이다. 
    import sys
    max_int = sys.maxsize
    print(max_int)
    max_int = sys.maxsize * sys.maxsize
    print(max_int)
    # maxsize는 의미 없음
    ```

- 실수는 부동소수점을 사용하는데, 2진수로 숫자 표현을 하는 과정에서 소수점 이하 값이 달라지는 오류가 생겨서 값을 비교하는 과정에서 오류가 발생한다.

  ```python
  # 이 경우 False가 출력된다.
  a = 0.3
  b = 0.1 * 3
  a == b
  
  # 처리 방법 1, 소수점 2번째 자리로 반올림 후 비교
  a == round(b, 2)
  
  # 처리 방법 2, 비교할 값의 차이를 절대값으로 바꾼 뒤 소수점 10번째 자리와 비교
  abs(a - b) <= 1e-10
  # e는 10제곱을 의미, e-10은 10의 -10제곱인 0.0000000001이며, 비교할 두 값을 뺀 나머지의 절대값이 0.0000000001보다 작거나 같을 경우에는 True, 클 경우엔 False
  
  # 처리 방법 3, 절대값 비교를 내장된 float epsilon 값과 비교
  import sys
  abs(a - b) <= sys.float_info.epsilon
  # sys.float_info.epsilon은 2.220446049250313e-16으로, 2.220446049250313의 10의 -16승인데 그냥 소수점 저 멀리랑 비교한다. 아마도 나는 쓸 일 없을 것 같다. 기억을 못 해서.
  
  # 처리 방법 4, math 모듈로 근사값인지 확인(python 3.5부터 가능한 신문물)
  import math
  math.inclose(a, b)
  # 이게 짱 쉬워보이는데 기억할 수 있을는지는 모르겠다.
  ```

- 복소수는 허수부를 j로 표현한다.

  - 수학 공부 시간!

    ```python
    # 복소수의 허수 부분을 반환할 때
    print(a.imag)
    # 복소수의 실수 부분을 반환할 때
    print(a.real)
    # 켤레복소수를 반환할 때, 켤레복소수는 허수 부분의 부호를 바꾼 걸 말한다.
    # cf) 1-1j의 켤레복소수는 1+1j
    print(a.conjugate())
    print(a.conjugate() * a)
    ```



