# Pokemon 기본 설정
import random

class Pokemon():
    def __init__(self, name, level, speed, ptype=0):
        self.name = name
        self.level = level
        self.hp = int(level * 8.7)
        self.speed = speed
    
    def heal(self):
        self.hp += random.choice(range(10, 50))
    
    def status(self):
        print(f"{self.name}의 현재 레벨은 {self.level}이며, 남은 체력은 {self.hp}입니다.")
        
    def status_all(self):
        print(f"이름: {self.name} 속성: {self.type.pop(0) if 0 in self.type else self.type}\n레벨: {self.level} 체력: {self.hp} 스피드: {self.speed}")
