import random

print("====포켓몬 리스트====")
for num in range(1, 149, 3):
    print(f"{num}. {mon_list[num - 1][0]}    {num + 1}. {mon_list[num][0]}    {num + 2}. {mon_list[num + 1][0]}")
print("====================")


class Trainer():
    def __init__(self):
        self.Tname = input(f"플레이어의 이름을 입력해주세요 : \n")
        self.mon_set = []
        
        mon_count = 0
        while mon_count != 6:
            mon_set = int(input(f"{mon_count + 1}번째 포켓몬을 입력하세요. (0은 랜덤 선택) : "))
            if mon_set == 0:
                poke_mon = class_list[random.choice(range(0, 151))]()
                # poke_class = Pokemon(poke_mon[0], poke_mon[1], poke_mon[2], poke_mon[3])
                self.mon_set.append(poke_mon)
                mon_count += 1
            else:
                poke_mon = class_list[mon_set - 1]()
                # poke_class = Pokemon(poke_mon[0], poke_mon[1], poke_mon[2], poke_mon[3])
                self.mon_set.append(poke_mon)
                mon_count += 1
        print(f"\n{self.Tname}의 포켓몬은 {self.mon_set[0].name}, {self.mon_set[1].name}, {self.mon_set[2].name}, {self.mon_set[3].name}, {self.mon_set[4].name}, {self.mon_set[5].name}입니다.\n")

    def status(self):
        stat_count = 1
        print(f"{self.Tname}의")
        for mon in self.mon_set:
            print(f"{stat_count}번째 포켓몬 : lv. {mon.level} {mon.name} | 체력 : {mon.hp} | 스피드 : {mon.speed} | 타입 : {mon.ptype}")
            stat_count += 1
        print("====================")


player1 = Trainer()
player2 = Trainer()