# Pokemon 기본 설정
import random

class Pokemon(Skill):
    def __init__(self, name, level, speed, ptype):
        self.name = name
        # 1, 2, 3은 3단계 진화 포켓몬
        # 4, 5는 2단계 진화 포켓몬
        # 6은 진화 없는 포켓몬
        # 7은 전설의 포켓몬
        # 8, 9, 0은 진화가 빠른 벌레 포켓몬
        if level == 1:
            self.level = random.choice(range(5, 18))
        elif level == 2:
            self.level = random.choice(range(18, 36))
        elif level == 3:
            self.level = random.choice(range(36, 51))
        elif level == 4:
            self.level = random.choice(range(5, 20))
        elif level == 5:
            self.level = random.choice(range(20, 41))
        elif level == 6:
            self.level = random.choice(range(30, 51))
        elif level == 7:
            self.level = random.choice(range(50, 71))
        elif level == 8:
            self.level = random.choice(range(5, 7))
        elif level == 9:
            self.level = random.choice(range(7, 10))
        elif level == 0:
            self.level = random.choice(range(10, 30))

        self.hp = int(level * 11.7)
        self.speed = speed
        self.ptype = ptype

        skill_list = []
        nor_count = 0
        fir_count = 0
        wat_count = 0
        ele_count = 0
        gra_count = 0
        ice_count = 0
        fig_count = 0
        poi_count = 0
        gro_count = 0
        fly_count = 0
        esp_count = 0
        bug_count = 0
        roc_count = 0
        gho_count = 0
        dra_count = 0
        while len(skill_list) < 4:
            if type(self.ptype) == str:
                if "노말" in self.ptype:
                    in_skill = random.choice(Skill.normal)
                    if in_skill not in skill_list:
                        skill_list.append(in_skill)
                if "불꽃" in self.ptype:
                    in_skill = random.choice(Skill.fire)
                    if in_skill not in skill_list:
                        skill_list.append(in_skill)
                if "물" in self.ptype:
                    in_skill = random.choice(Skill.water)
                    if in_skill not in skill_list:
                        skill_list.append(in_skill)
                if "전기" in self.ptype:
                    in_skill = random.choice(Skill.electric)
                    if in_skill not in skill_list:
                        skill_list.append(in_skill)
                if "풀" in self.ptype:
                    in_skill = random.choice(Skill.grass)
                    if in_skill not in skill_list:
                        skill_list.append(in_skill)
                if "얼음" in self.ptype:
                    in_skill = random.choice(Skill.ice)
                    if in_skill not in skill_list:
                        skill_list.append(in_skill)
                if "격투" in self.ptype:
                    in_skill = random.choice(Skill.fight)
                    if in_skill not in skill_list:
                        skill_list.append(in_skill)
                if "독" in self.ptype:
                    in_skill = random.choice(Skill.poison)
                    if in_skill not in skill_list:
                        skill_list.append(in_skill)
                if "땅" in self.ptype:
                    in_skill = random.choice(Skill.ground)
                    if in_skill not in skill_list:
                        skill_list.append(in_skill)
                if "비행" in self.ptype:
                    in_skill = random.choice(Skill.fly)
                    if in_skill not in skill_list:
                        skill_list.append(in_skill)
                if "에스퍼" in self.ptype:
                    in_skill = random.choice(Skill.esper)
                    if in_skill not in skill_list:
                        skill_list.append(in_skill)
                if "벌레" in self.ptype:
                    in_skill = random.choice(Skill.bug)
                    if in_skill not in skill_list:
                        skill_list.append(in_skill)
                if "바위" in self.ptype:
                    in_skill = random.choice(Skill.rock)
                    if in_skill not in skill_list:
                        skill_list.append(in_skill)
                if "고스트" in self.ptype:
                    in_skill = random.choice(Skill.ghost)
                    if in_skill not in skill_list:
                        skill_list.append(in_skill)
                if "드래곤" in self.ptype:
                    in_skill = random.choice(Skill.dragon)
                    if in_skill not in skill_list:
                        skill_list.append(in_skill)

            if type(self.ptype) == tuple:
                if "노말" in self.ptype and nor_count < 3:
                    in_skill = random.choice(Skill.normal)
                    if in_skill not in skill_list:
                        skill_list.append(in_skill)
                        nor_count += 1
                if "불꽃" in self.ptype and fir_count < 3:
                    in_skill = random.choice(Skill.fire)
                    if in_skill not in skill_list:
                        skill_list.append(in_skill)
                        fir_count += 1
                if "물" in self.ptype and wat_count < 3:
                    in_skill = random.choice(Skill.water)
                    if in_skill not in skill_list:
                        skill_list.append(in_skill)
                        wat_count += 1
                if "전기" in self.ptype and ele_count < 3:
                    in_skill = random.choice(Skill.electric)
                    if in_skill not in skill_list:
                        skill_list.append(in_skill)
                        ele_count += 1
                if "풀" in self.ptype and gra_count < 3:
                    in_skill = random.choice(Skill.grass)
                    if in_skill not in skill_list:
                        skill_list.append(in_skill)
                        gra_count += 1
                if "얼음" in self.ptype and ice_count < 3:
                    in_skill = random.choice(Skill.ice)
                    if in_skill not in skill_list:
                        skill_list.append(in_skill)
                        ice_count += 1
                if "격투" in self.ptype and fig_count < 3:
                    in_skill = random.choice(Skill.fight)
                    if in_skill not in skill_list:
                        skill_list.append(in_skill)
                        fig_count += 1
                if "독" in self.ptype and poi_count < 3:
                    in_skill = random.choice(Skill.poison)
                    if in_skill not in skill_list:
                        skill_list.append(in_skill)
                        poi_count += 1
                if "땅" in self.ptype and gro_count < 3:
                    in_skill = random.choice(Skill.ground)
                    if in_skill not in skill_list:
                        skill_list.append(in_skill)
                        gro_count += 1
                if "비행" in self.ptype and fly_count < 3:
                    in_skill = random.choice(Skill.fly)
                    if in_skill not in skill_list:
                        skill_list.append(in_skill)
                        fly_count += 1
                if "에스퍼" in self.ptype and esp_count < 3:
                    in_skill = random.choice(Skill.esper)
                    if in_skill not in skill_list:
                        skill_list.append(in_skill)
                        esp_count += 1
                if "벌레" in self.ptype and bug_count < 3:
                    in_skill = random.choice(Skill.bug)
                    if in_skill not in skill_list:
                        skill_list.append(in_skill)
                        bug_count += 1
                if "바위" in self.ptype and roc_count < 3:
                    in_skill = random.choice(Skill.rock)
                    if in_skill not in skill_list:
                        skill_list.append(in_skill)
                        roc_count += 1
                if "고스트" in self.ptype and gho_count < 3:
                    in_skill = random.choice(Skill.ghost)
                    if in_skill not in skill_list:
                        skill_list.append(in_skill)
                        gho_count += 1
                if "드래곤" in self.ptype and dra_count < 3:
                    in_skill = random.choice(Skill.dragon)
                    if in_skill not in skill_list:
                        skill_list.append(in_skill)
                        dra_count += 1
        
        self.skill_list = skill_list