class Dog:
    num_of_dogs = 0
    birth_of_dogs = 0
    list_of_dogs = []
    
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        Dog.num_of_dogs += 1
        Dog.birth_of_dogs += 1
        Dog.list_of_dogs.append(self.name)
        
    def __del__(self):
        Dog.num_of_dogs -= 1
        
    def bark(self):
        return "멍멍!"
    
    @staticmethod
    # 스태틱 메소드는 self 안 넣음
    def info():
        return f"개다!"
    # 예시는 return f"총 {Dog.num_of_dogs}마리의 개가 있습니다." 였지만, 스태틱 메소드는 클래스에 접근 안 할 때 쓰는 게 좋아서 변경
    
    @classmethod
    def birth(cls):
        return f"Birth: {cls.birth_of_dogs}, Current: {cls.num_of_dogs}"
#         return f"총 {cls.birth_of_dogs}마리의 개가 태어났습니다."

d = Dog("choco", "poodle")
# instance method
print(d.bark())

# static method
print(d.info())
print(Dog.info())

# class method
print(Dog.birth())

d1 = Dog("초코", "푸들")
d1.bark()
d2 = Dog("꽁이", "말티즈")
d2.bark()
d3 = Dog("시바", "시바")
d3.bark()
print(Dog.num_of_dogs)

class Dog:
    num_of_dogs = 0
    birth_of_dogs = 0
    list_of_dogs = []
    
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        Dog.num_of_dogs += 1
        Dog.birth_of_dogs += 1
        Dog.list_of_dogs.append(self.name)
        
    def __del__(self):
        Dog.num_of_dogs -= 1
        
    def bark(self):
        return "멍멍!"
    
    @staticmethod
    # 스태틱 메소드는 self 안 넣음
    def info():
        return f"개다!"
    # 예시는 return f"총 {Dog.num_of_dogs}마리의 개가 있습니다." 였지만, 스태틱 메소드는 클래스에 접근 안 할 때 쓰는 게 좋아서 변경
    
    @classmethod
    def birth(cls):
        return f"Birth: {cls.birth_of_dogs}, Current: {cls.num_of_dogs}"
#         return f"총 {cls.birth_of_dogs}마리의 개가 태어났습니다."

d = Dog("choco", "poodle")
# instance method
print(d.bark())

# static method
print(d.info())
print(Dog.info())

# class method
print(Dog.birth())

d1 = Dog("초코", "푸들")
d1.bark()
d2 = Dog("꽁이", "말티즈")
d2.bark()
d3 = Dog("시바", "시바")
d3.bark()
print(Dog.num_of_dogs)