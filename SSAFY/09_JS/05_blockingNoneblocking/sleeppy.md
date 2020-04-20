```python
from time import sleep

# Blocking 한 함수들로 구성.
#1) sleep_3s() 정의
#2) print("ZzZz") 실행
#3) sleep_3s() 실행, 3초 sleep
#4) sleep_3s() 내부 print("Wake up!") 실행
#5) print("End Game...") 실행

def sleep_3s():
    sleep(3)
    print("Wake up!")
    
print("ZzZz")
sleep_3s()
print("End Game...")

```

