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



### 데이터 타입 (Data type)

- container에는 Sequence(ordered)와 Unordered가 있음



#### immutable : `string`, `list`, `tuple`, `range()`

- 변할 수 있는 친구들
- 순서가 있기 때문에 index로 접근이 가능

#### mutable : : `set`, `dict`

- 변할 수 없는 친구들
- 순서가 없기 때문에 index로 접근하지 못함

#### method에 값을 바꾸는 게 있으면 mutable, 없으면 immutable

- string에 replace가 있지만 원본이 파괴되지 않기 때문에 immutable
- python 3.7.x부터는 `dict`에 확실한 순서가 생김
  - index 접근은 안 되지만, 뒤에 붙는 경우에 반드시 뒤에 붙음
  - 삽입 순서의 보존으로 순서만 기억하고 돌릴 때 그 순서로 돈다는 것



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






# 04 Recursive function

- 팩토리얼, 치킨쿠폰, 피보나치, 업&다운, 제곱근 구하기 풀 수 있는 정도면 됨
  - 그게 어려워서 그렇지
  - for문 쓰는 건 완전한 재귀 함수는 아님
  - 업&다운은 problem set, 제곱근 문제는 workshop 06번 참고





# 05 Data structure

### 문자열 (String)

`.upper()` / `.lower()` : 전부 대문자 / 소문자로 만듦

`.capitalize()` : 맨 첫 글자만 대문자

`.title()` : `'`나 공백 이후의 첫 글자를 대문자로 만듦

`.swapcase()` : 대소문자를 바꿈

```python
String = "i'm Fine thank You"

String.upper() == "I'M FINE THANK YOU"
String.lower() == "i'm fine thank you"

String.capitalize() == "I'm fine thank you"
String.title() == "I'M Fine Thank You"
String.swapcase() == "I'M fINE THANK yOU"
```

`"넣을 문자열".join(iterable)` : `()` 안의 내용물(?) 사이에 문자열을 넣어서 반환

★ iterable : `list`, `dict`, `set`, `str`, `bytes`, `tuple`, `range`처럼 순서대로 빼낼 수 있는 친구들

- `for`문과 진행 방식이 같다고 생각하면 편함

`.replace(바꿀 글자, 바뀔 글자, 바꿀 갯수)` : 순서는 입력하지 않아도 됨

`.strip("지울 글자")` : `()`는 공백을 제거, `.lstrip()`, `.rstrip()`은 좌, 우 제거 중간 글자는 못 지움

`.split("나눌 기준 문자")` : `()`은 공백이 기준, 기준이 되는 문자로 단어를 나누어 리스트로 반환 

- 기준 문자가 문자열 마지막에도 있으면 리스트의 맨 마지막에 공백이 반환됨

`.find(x)` : x가 있는 첫 번째 위치를 반환(index), 없으면 `-1`

`.index(x)` : find와 같은 역할인데 없으면 오류

```python
String = "A_B_C_D_E_F_G"
Test = ["A", "B", "C"]

"??".join(Test) == "A??B??C??"
Test의 "A"가 먼저 들어가고 뒤에 "??"가 붙고 "B"가 들어가고 "??"가 붙는 식

String.replace("_", "?") == "A?B?C?D?E?F?G"
String.replace("_", "?", 2) == "A?B?C_D_E_F_G"

String.strip("_") == "A_B_C_D_E_F_G"
String.strip("A") == "_B_C_D_E_F_G"

String.split("_") == ["A", "B", "C", "D", "E", "F", "G"]

String.find("_") == 1
String.find("?") == -1
String.index("_") == 1
String.index("?") == 에러에러에러에렁레ㅓㅇ레얼에레ㅓ
```



### 리스트 (List)

#### 값의 추가 제거

`.append(추가할 값)` : `list` 맨 뒤에 값을 추가

`.insert(위치, 값)` : 위치(index)에 값을 추가, 기존에 값이 있는 index라면 기존 값은 하나 뒤로 이동

`.extend(iterable)` : `list` 맨 뒤에 값을 추가, `append`는 하나만 추가 가능하지만 `extend`는 여러 개도 가능

- iterable이 들어가기 때문에 `for`, `.join()`처럼 하나의 index씩 진행됨
- `string`을 넣으면 `string`의 한 글자씩 나뉘어서 `list`에 추가됨
- 하나의 `string`이 들어있는 `tuple`은 `string`으로 인식하니 주의, 단, `list`일 경우엔 [string] 형태로 추가됨

`.remove(지울 값)` : 지울 값을 1번 지움, 없으면 에러

`.pop(위치)` : 위치(index)의 값을 지움, 입력한 index가 `list`의 index범위를 벗어난 경우 에러

```python
Test = [1, 2, 3, 4, 5]

Test.append(6) == [1, 2, 3, 4, 5, 6]
Test.insert(1, 5) == [1, 5, 2, 3, 4, 5, 6]

Test.extend([4, 3]) == [1, 2, 3, 4, 5, 4, 3]
Test.extend("이렇게됨") == [1, 2, 3, 4, 5, "이", "렇", "게", "됨"]
Test.extend(("이것도")) == [1, 2, 3, 4, 5, "이", "것", "도"]
Test.extend([4]) == [1, 2, 3, 4, 5, [4]]

Test.remove(1) == [2, 3, 4, 5]
Test.pop(1) == [1, 3, 4, 5]
```

`.index(찾을 값)` : 찾을 값의 가장 첫 번째 index를 반환

`.count(찾을 값)` : 찾을 값의 갯수를 반환

`.sort()` : 값을 순서대로 정렬, `sorted(list)`는 원본 파괴가 아니지만 `.sort()`는 원본 파괴

`.reverse()` : 현재 `list`의 값을 반대로 뒤집음

`.clear()` : `list` 비우기

```python
Test = [2, 3, 4, 5, 1]

Test.insert(1) == 4
Test.count(1) == 1
Test.sort() == [1, 2, 3, 4, 5]
Test.reverse() == [1, 5, 4, 3, 2]
Test.clear() == []
```

#### List Comprehension

```python
Test = [ 넣을 값 for t in range(1, 6)]
# 넣을 값이 t라면 Test == [1, 2, 3, 4, 5]
# t * 2라면 Test == [2, 4, 6, 8, 10]
```

#### 피타고라스 정리(List Comprehension)

```python
# x < y < z < 50의 범위에 있는 피타고라스 정리
test = [ (x, y, z) for x in range(1, 50) for y in range(x, 50) for z in range(y, 50) if x ** 2 + y ** 2 == z ** 2]

# 여러 개의 for문을 겹칠 수도 있고, if문을 달 수 있음
test = []
for x in range(1, 50):
    for y in range(x, 50):
        for z in range(y, 50):
            if x ** 2 + y ** 2 = z ** 2:
                test.append((x, y, z))

# 위의 코드와 같은 결과
```



### 딕셔너리 (Dictionary)

`.pop(key, 반환할 값)` : `key`가 `dict`에 있으면 제거하고 `value`를 반환, `dict`에 입력한 `key`가 없을 경우 반환할 값을 반환

`.update()` : `key`에 해당하는 `value`를 덮어쓸 수 있음





















# 06 OOP_intro

- Class : 설계도, 틀의 느낌. 정의하는 역할만 함
- Instance : Class와 Object의 관계. 수행하는 역할만 함
  - Object는 Instance와 같지만 메모리나 코드 상에 실존하는 것
- Method : Class 안에 있는 행위