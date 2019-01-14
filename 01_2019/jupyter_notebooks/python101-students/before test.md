# 01 Python Intro

- 단어를 자주 사용하진 않았지만 뭔지 알고 있어야 함

  - ex) 식별자

- 식별자 : 터미널에 쳤을 때 있다고 나오는 이름

  - 첫 글자는 숫자가 불가능하고, 대소문자 구분

- 인코딩 선언 : 한글 깨질 때 쓰게 되니까 알아두는 게 좋음

  ```python
  #-*- coding: utf-8 -*-
  ```

- 주석 : 기계는 못 읽고 사람은 읽음

  - `"""`로 표현하는 docstring은 변수에 할당할 수 있기 때문에 조금 특별함(프린트도 됨)

- 코드 라인 : `;`으로 이어서 작성할 수 있지만 잘 사용하지 않음

- `\`을 쓰면 엔터를 쳤어도 이어져서 읽음

- `=`을 통해 변수를 할당(저장 아님)

- `id()`로 메모리 주소를 확인할 수 있음(카피, 딥카피)

  - 1~256의 메모리 주소는 고정

- `int`는 `0o`로 8진수, `0b`로 2진수, `0x`로 16진수를 표현할 수 있다

  - 정수 자료형 오버플로우 확인(?)

    ```python
    # 파이썬은 기존 C 계열 프로그래밍 언어와 다르게 정수 자료형에서 오버플로우가 없다.
    # arbitrary-precision arithmetic를 사용하기 때문이다. 
    import sys
    max_int = sys.maxsize
    print(max_int)
    max_int = sys.maxsize * sys.maxsize
    print(max_int)
    ```

    

- `float`는 실수 표현, `0.3`이랑 `0.1 * 3`은 소수점 저 아래가 다름

  - 처리 방법

    ```python
    # 처리방법 1-1. 절대값을 비교
    a = 0.1 * 3
    b = 0.3
    
    abs(a - b) <= 1e-10 # 0.0000000001보다 차이가 적으면 진행
    
    # 처리방법 1-2. 절대값 비교를 내장된 float epsilon값과 비교
    import sys
    abs(a - b) <= sys.float_info.epsilon
    
    print(sys.float_info.epsilon)
    
    # 처리방법 2. math 모듈을 통해 근사한 값인지 비교
    # python 3.5부터는 math 모듈을 활용할 수 있다.
    import math
    math.isclose(a, b)
    ```

- `complex` 복소수는 `j`가 들어가 있으면 복소수

  - `.imag`로 허수부, `.real`로 실수부 확인할 수 있음(인스턴스 변수라서 `()` 없음)
  - `.conjugate()`로 모두 확인 가능

- `bool()`로 형태를 확인할 수 있음

  - `0`, `0.0`, `()`, `[]`, `{}`, `''`, `None`은 False

- `None`, `return`이 없는 함수는 `None`으로 표시됨

- `\n` : 줄바꿈, `\t` : 탭, `\r` : 캐리지리턴, `\0` : 널(Null), `\\` : \

  - 캐리지리턴은 찾아봐야겠다

- String interpolation

  - `%-fomatting`, `str.format()`, `f-string`

- 산술 연산자

  - `+`, `-`, `*`, `/`, `//`, `%`, `**`

- 비교 연산자

  - `>`, `<`, `>=`, `<=`, `==`, `!=`

- 논리 연산자

  - `and`, `or`, `not`
  - `&`, `|`은 비트 연산자

- 복합 연산자

  - `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`

- 기타 연산자

  - Concatenation : 숫자가 아닌 자료형은 `+`로 합칠 수 있음
  - Containment Test : `in`연산자로 속해있는지 알 수 있음
  - Identity : `is`연산자로 동일한 object인지 확인할 수 있음
  - Indexing/Slicing : `[]`를 통한 값 접근, `[:]`로 슬라이싱

- 연산자 우선순위

  ```python
  0. ()을 통한 grouping
  1. Slicing
  2. Indexing
  3. 제곱연산자 **
  4. 단항연산자 +, - (음수/양수 부호)
  5. 산술연산자 *, /, %
  6. 산술연산자 +, -
  7. 비교연산자, in, is
  8. not
  9. and
  10. or
  ```

- 기초 형변환(Type conversion, Typecasting)

  - 파이썬에서 데이터 타입은 변환 가능

- 암시적 형변환(Implicit Type Conversion)

  - 사용자가 의도하지 않았는데 파이쎤에서 변환하는 경우
  - `bool`, `Numbers(int, float, complex)`

- 명시적 형변환(Explict Type Conversion)

  - `str`을 `int`로 : 형식에 맞는 숫자만 가능

  - `int`를 `str`로 : 모두 가능

  - 암시적 형변환이 되는 모은 경우도 명시적으로 변환 가능

    ```python
    list(), int(), float(), str() 등
    ```

- 시퀀스(sequence) 자료형

  - 데이터의 순서대로 나열된 형식(정렬이 아님)

    ```python
    list, tuple, range, string
    binary는 따로 다루지는 않음
    ```

  - 튜플(tuple)

    - 수정 불가능(immutable)

  - 레인지(range)

    - `range(n)`, `range(n, m)`, `range(n, m, s)`

  - 시퀀스에서 활용할 수 있는 연산자/함수

    ```python
    in, not in, +, *, [i], [i:j], [i:j:k]
    len(), min(), max(), n.count()
    ```

  - 세트(set)

    ```python
    - 차집합, | 합집합, & 교집합, a.union(b), a.intersection(b)
    ```

  - 딕셔너리(dict)

    - `key`와 `value`가 쌍으로 이루어짐
    - `key`는 immutable한 모든 것이 가능함(`str`, `int`, `float`, `bool`, `tuple`, `range`)
    - `value`는 `list`, `dictionary`를 포함한 값이 다 가능

- Container

  - Sequence(Ordered)
    - `str`, `list`, `tuple`, `range`
  - Unordered
    - `set`, `dict`





# 02 Control of flow

- 제어문은 크게 조건문과 반복문으로 나눌 수 있음

- if <조건식>:

  - elif로 여러 조건문 사용 가능

- 조건 표현식(삼항연산자)

  ```python
  <참일 때 할 것> if <조건식> else <틀리면 할 것>
  value = num if num >= else 0
  ```

- 반복문 while <조건식>

  - 조건식이 거짓일 때까지 반복

- 반복문 for i in sequence:

  - `sequence`를 순차적으로 variable에 값을 바인딩하며 코드 블록을 시행

  - 시퀀스의 요소를 하나씩 꺼내면서 반복함

  - index와 함께 사용하기 `enumerate()`

    - 시퀀스, 이터레이터나 이터레이션을 지원하는 다른 객체여야 하고 튜플로 돌려줌

      ```python
      for index, menu in enumerate(lunch):
      ```

    - set에도 사용은 할 수 있지만 강제로 index를 주게 됨
    - index 접근이 되는 애들만 써야 한다고 생각하는 게 좋음

  - `dict`와 함께 사용하기 `.keys()`, `.values()`, `.items()`

    - 그냥 돌리면 `key`값만 나옴

  - `break`, `continue`, `else`

    ```python
    break로 바로 탈출 가능, 더 볼 필요 없을 때 사용
    continue를 만나면 밑에 있는 코드를 생략하고 다음 회차로 넘어감
    else break로 탈출하지 않고, for문이 끝까지 다 돌았을 때 실행하는 것
    ```

    


# 03 Function

- 함수 : 코드가 반복되면 함수로 만듦

  - 함수는 `return`으로 끝나야 함 없으면 None 반환
  - `def`로 시작, `:`로 끝내고 아래에 코드 블록을 만듦
  - `인자, 매개변수(parameter)`를 넘길 수 있음

- `return`은 어떤 것도 반환할 수 있다

  - `,`를 쓰면 `tuple`로 묶여버림

- 기본값 설정

  ```python
  def test(a, b=0):
  # 기본값을 준 인자 뒤에는 기본값이 없는 인자가 오면 안 됨
  ```

- 키워드 인자

  ```python
  def test(a, b=0):
  
  test(b = "A", a = "B") 가능
  한 번 키워드 인자를 사용하면 다 사용해야 함
  ```

- 가변 인자 리스트

  - `print()`가 대표적

    ```python
    def func(*args):
    # 여러 인자를 한 번에 받겠다는 뜻
    ```

- 정의되지 않은 인자 처리

  - `**kwargs`처럼 `**`을 붙여서 사용하며, `dict`로 처리됨

- `dict`를 인자로 넘기기(unpacking arguments list)

  ```python
  def sign_up(username, password, password_confirmation):
  # username이 중복되는지 확인하는 코드는 패스 cf) username in usernames
      if password == password_confirmation:
          return True
      else:
          return False
  new_account = {
      "username": "terpe",
      "password": "1q2w3e4r",
      "password_confirmation": "1q2w3e4r"
  }
  
  # sign_up(new_account) 이건 에러. new_account는 이미 dict고, signup은 3개의 인자를 받아야 하기 때문에
  ```

- 이름공간 및 스코프(Scope) 순서

  - **L**ocal scope: 정의된 함수
  - **E**nclosed scope : 상위 함수
  - **G**lobal scope : 함수 밖의 변수 혹은 import된 모듈
  - **B**uilt-in scope : 내장 함수 또는 속성

  ```python
  def print_name(name):
      print(make_greeting(name))
      
  def make_greeting(name):
      greeting = f"hello, {name}"
      return greeting
  
  print_name("SSAFY")
  
  def print_name(name):
      def make_greeting(name):
          greeting = f"hello, {name}"
          return greeting
      
      print(make_greeting(name))
      
  print_name("ssafy")
  make_greeting("ss3")
  ```

- 전자는 `make_greeting()`도 호출이 가능하지만 후자는 `print_name()`안에 들어있기 때문에 불가능하다.

  - 후자의 `make_greeting()`의 이름공간(name space)는 `print_name()`안
  - 이 경우가 **E**nclosed scope

  ```python
  def print_name(name):
        def make_greeting(name):
            return f"hi, {name}"
        
        print(make_greeting(name))
        
  print_name("ssafy")
  ```

  

- 

