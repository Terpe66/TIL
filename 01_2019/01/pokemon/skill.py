# Pokemon 타입별 설정
# 노말 = 바위 0.5 고스트 0
# 불꽃 = 불꽃 물 바위 드래곤 0.5 풀 얼음 벌레 2
# 물 = 물 풀 드래곤 0.5 불꽃 땅 바위 2
# 전기 = 물 비행 2 드래곤 전기 풀 0.5 땅 0
# 풀 = 불꽃 풀 독 비행 벌레 드래곤 0.5 물 땅 바위 2
# 얼음 = 불꽃 물 얼음 0.5 풀 땅 비행 드래곤 2
# 격투 = 노말 얼음 바위 2 독 비행 에스퍼 벌레 0.5 고스트 0
# 독 = 풀 2 독 땅 바위 고스트 0.5
# 땅 = 불꽃 전기 독 바위 2 풀 벌레 0.5 비행 0
# 비행 = 풀 격투 벌레 2 전기 바위 0.5
# 에스퍼 = 격투 독 2 에스퍼 0.5
# 벌레 = 불꽃 격투 독 비행 고스트 0.5 풀 에스퍼 2
# 바위 = 불꽃 얼음 비행 벌레 2 격투 땅 0.5
# 고스트 = 노말 0 에스퍼 고스트 2
# 드래곤 = 드래곤 2

# 딜 공식 = 데미지 + 레벨 * 0.3 (크리티컬 시 2배)

# class Normal():
#     ptype = "노말"

#     def body_attack(self):
#         damage = 35
#         aim = 95
#         if random.choice(range(100)) in range(aim)
#             if "바위" in enemy.ptype:
#                 if random.choice(range(16)) == 1:
#                     enemy.hp -= (damage * 0.5 + self.level * 0.3) * 2
#                     print(f"{enemy.name}은 {(damage * 0.5 + self.level * 0.3) * 2}의 피해를 입었다!")
#                 else:
#                     enemy.hp -= damage * 0.5 + self.level * 0.3
#                     print(f"{enemy.name}은 {damage * 0.5 + self.level * 0.3}의 피해를 입었다!")
            
#             elif "고스트" in enemy.ptype:
#                 print(f"효과가 없는 것 같다...")
            
#             else:
#                 if random.choice(range(16)) == 1:
#                     enemy.hp -= (damage * 0.5 + self.level * 0.3) * 2
#                     print(f"{enemy.name}은 {(damage * 0.5 + self.level * 0.3) * 2}의 피해를 입었다!")
#                 else:
#                     enemy.hp -= damage + self.level * 0.3
#                     print(f"{enemy.name}은 {damage + self.level * 0.3}의 피해를 입었다!")
#         else:
#             print(f"")
    

class Skill():
    normal = [
        ("몸통박치기", 35, 95, 0, ("바위"), ("고스트")),
        ("괴력", 80, 100, 0, ("바위"), ("고스트")),
        ("연속펀치", 36, 85, 0, ("바위"), ("고스트")),
        ("스피드스타", 60, 100, 0, ("바위"), ("고스트")),
        ("파괴광선", 160, 90, 0, ("바위"), ("고스트")),
        ("튀어오르기", 0, 0, 0, ("바위"), ("고스트")),
        ("더블어택", 70, 90, 0, ("바위"), ("고스트")),
        ("메가톤펀치", 80, 85, 0, ("바위"), ("고스트")),
        ("메가톤킥", 120, 75, 0, ("바위"), ("고스트")),
        ("잼잼펀치", 70, 100, 0, ("바위"), ("고스트")),
        ("이판사판태클", 120, 100, 0, ("바위"), ("고스트")),
        ("누르기", 85, 100, 0, ("바위"), ("고스트"))
    ]

    fire = [
        ("니트로차지", 50, 100, ("풀", "얼음", "벌레"), ("불꽃", "물", "바위", "드래곤"), 0),
        ("성스러운불꽃", 100, 95, ("풀", "얼음", "벌레"), ("불꽃", "물", "바위", "드래곤"), 0),
        ("화염자동차", 60, 100, ("풀", "얼음", "벌레"), ("불꽃", "물", "바위", "드래곤"), 0),
        ("불꽃펀치", 75, 100, ("풀", "얼음", "벌레"), ("불꽃", "물", "바위", "드래곤"), 0),
        ("불꽃세례", 40, 100, ("풀", "얼음", "벌레"), ("불꽃", "물", "바위", "드래곤"), 0),
        ("오버히트", 140, 90, ("풀", "얼음", "벌레"), ("불꽃", "물", "바위", "드래곤"), 0),
        ("화염방사", 95, 100, ("풀", "얼음", "벌레"), ("불꽃", "물", "바위", "드래곤"), 0),
        ("불대문자", 120, 85, ("풀", "얼음", "벌레"), ("불꽃", "물", "바위", "드래곤"), 0),
        ("회오리불꽃", 35, 85, ("풀", "얼음", "벌레"), ("불꽃", "물", "바위", "드래곤"), 0),
        ("불태우기", 60, 100, ("풀", "얼음", "벌레"), ("불꽃", "물", "바위", "드래곤"), 0),
        ("연옥", 100, 50, ("풀", "얼음", "벌레"), ("불꽃", "물", "바위", "드래곤"), 0),
        ("불꽃튀기기", 70, 100, ("풀", "얼음", "벌레"), ("불꽃", "물", "바위", "드래곤"), 0)
    ]

    water = [
        ("물대포", 40, 100, ("불꽃", "땅", "바위"), ("물", "풀", "드래곤"), 0),
        ("물수리검", 15, 100, ("불꽃", "땅", "바위"), ("물", "풀", "드래곤"), 0),
        ("아쿠아테일", 90, 90, ("불꽃", "땅", "바위"), ("물", "풀", "드래곤"), 0),
        ("아쿠아브레이크", 85, 100, ("불꽃", "땅", "바위"), ("물", "풀", "드래곤"), 0),
        ("소금물", 65, 100, ("불꽃", "땅", "바위"), ("물", "풀", "드래곤"), 0),
        ("물의파동", 60, 100, ("불꽃", "땅", "바위"), ("물", "풀", "드래곤"), 0),
        ("바다회오리", 35, 85, ("불꽃", "땅", "바위"), ("물", "풀", "드래곤"), 0),
        ("하이드로펌프", 120, 80, ("불꽃", "땅", "바위"), ("물", "풀", "드래곤"), 0),
        ("파도타기", 95, 100, ("불꽃", "땅", "바위"), ("물", "풀", "드래곤"), 0),
        ("하이드로캐논", 150, 90, ("불꽃", "땅", "바위"), ("물", "풀", "드래곤"), 0),
        ("거품광선", 65, 100, ("불꽃", "땅", "바위"), ("물", "풀", "드래곤"), 0),
        ("거품", 40, 100, ("불꽃", "땅", "바위"), ("물", "풀", "드래곤"), 0)
    ]

    electric = [
        ("뇌격", 130, 85, ("물", "비행"), ("드래곤", "전기", "풀"), ("땅")),
        ("번개펀치", 75, 100, ("물", "비행"), ("드래곤", "전기", "풀"), ("땅")),
        ("볼트태클", 120, 100, ("물", "비행"), ("드래곤", "전기", "풀"), ("땅")),
        ("스파크", 65, 100, ("물", "비행"), ("드래곤", "전기", "풀"), ("땅")),
        ("찌리리따끔따끔", 80, 100, ("물", "비행"), ("드래곤", "전기", "풀"), ("땅")),
        ("10만볼트", 95, 100, ("물", "비행"), ("드래곤", "전기", "풀"), ("땅")),
        ("번개", 120, 70, ("물", "비행"), ("드래곤", "전기", "풀"), ("땅")),
        ("전기쇼크", 40, 100, ("물", "비행"), ("드래곤", "전기", "풀"), ("땅")),
        ("전자포", 100, 50,("물", "비행"), ("드래곤", "전기", "풀"), ("땅")),
        ("방전", 80, 100, ("물", "비행"), ("드래곤", "전기", "풀"), ("땅")),
        ("와일드볼트", 90, 100, ("물", "비행"), ("드래곤", "전기", "풀"), ("땅")),
        ("일렉트릭네트", 55, 95, ("물", "비행"), ("드래곤", "전기", "풀"), ("땅"))
    ]

    grass = [
        ("꽃보라", 90, 100, ("물", "땅", "바위"), ("불꽃", "풀", "독", "비행", "벌레", "드래곤"), 0),
        ("덩굴채찍", 35, 100, ("물", "땅", "바위"), ("불꽃", "풀", "독", "비행", "벌레", "드래곤"), 0),
        ("씨폭탄", 80, 100, ("물", "땅", "바위"), ("불꽃", "풀", "독", "비행", "벌레", "드래곤"), 0),
        ("잎날가르기", 55, 95, ("물", "땅", "바위"), ("불꽃", "풀", "독", "비행", "벌레", "드래곤"), 0),
        ("파워휩", 120, 85, ("물", "땅", "바위"), ("불꽃", "풀", "독", "비행", "벌레", "드래곤"), 0),
        ("꽃잎댄스", 120, 100, ("물", "땅", "바위"), ("불꽃", "풀", "독", "비행", "벌레", "드래곤"), 0),
        ("리프스톰", 140, 90, ("물", "땅", "바위"), ("불꽃", "풀", "독", "비행", "벌레", "드래곤"), 0),
        ("솔라빔", 120, 100, ("물", "땅", "바위"), ("불꽃", "풀", "독", "비행", "벌레", "드래곤"), 0),
        ("에너지볼", 80, 100, ("물", "땅", "바위"), ("불꽃", "풀", "독", "비행", "벌레", "드래곤"), 0),
        ("하드플랜트", 150, 90, ("물", "땅", "바위"), ("불꽃", "풀", "독", "비행", "벌레", "드래곤"), 0),
        ("메지컬리프", 60, 100, ("물", "땅", "바위"), ("불꽃", "풀", "독", "비행", "벌레", "드래곤"), 0),
        ("우드호른", 75, 100, ("물", "땅", "바위"), ("불꽃", "풀", "독", "비행", "벌레", "드래곤"), 0),
        ("우드해머", 120, 100, ("물", "땅", "바위"), ("불꽃", "풀", "독", "비행", "벌레", "드래곤"), 0),
        ("리프블레이드", 90, 100, ("물", "땅", "바위"), ("불꽃", "풀", "독", "비행", "벌레", "드래곤"), 0)
    ]

    ice = [
        ("냉동펀치", 75, 100, ("풀", "땅", "비행", "드래곤"), ("불꽃", "물", "얼음"), 0),
        ("냉동빔", 95, 100, ("풀", "땅", "비행", "드래곤"), ("불꽃", "물", "얼음"), 0),
        ("눈보라", 110, 70, ("풀", "땅", "비행", "드래곤"), ("불꽃", "물", "얼음"), 0),
        ("얼음숨결", 80, 90, ("풀", "땅", "비행", "드래곤"), ("불꽃", "물", "얼음"), 0),
        ("얼다바람", 55, 95, ("풀", "땅", "비행", "드래곤"), ("불꽃", "물", "얼음"), 0),
        ("눈싸라기", 40, 100, ("풀", "땅", "비행", "드래곤"), ("불꽃", "물", "얼음"), 0),
        ("얼음뭉치", 40, 100, ("풀", "땅", "비행", "드래곤"), ("불꽃", "물", "얼음"), 0),
        ("아이스해머", 100, 90, ("풀", "땅", "비행", "드래곤"), ("불꽃", "물", "얼음"), 0),
        ("고드름떨구기", 85, 90, ("풀", "땅", "비행", "드래곤"), ("불꽃", "물", "얼음"), 0),
        ("고드름침", 50, 100, ("풀", "땅", "비행", "드래곤"), ("불꽃", "물", "얼음"), 0),
        ("아이스볼", 30, 90, ("풀", "땅", "비행", "드래곤"), ("불꽃", "물", "얼음"), 0),
        ("얼다세계", 65, 95, ("풀", "땅", "비행", "드래곤"), ("불꽃", "물", "얼음"), 0),
        ("프리즈드라이", 70, 100, ("풀", "땅", "비행", "드래곤"), ("불꽃", "물", "얼음"), 0)
    ]

    fight = [
        ("기합구슬", 120, 70, ("노말", "얼음", "바위"), ("독", "비행", "에스퍼", "벌레"), ("고스트")),
        ("파동탄", 90, 100, ("노말", "얼음", "바위"), ("독", "비행", "에스퍼", "벌레"), ("고스트")),
        ("폭발펀치", 100, 50, ("노말", "얼음", "바위"), ("독", "비행", "에스퍼", "벌레"), ("고스트")),
        ("태권당수", 50, 100, ("노말", "얼음", "바위"), ("독", "비행", "에스퍼", "벌레"), ("고스트")),
        ("인파이트", 120, 100, ("노말", "얼음", "바위"), ("독", "비행", "에스퍼", "벌레"), ("고스트")),
        ("마하펀치", 40, 100, ("노말", "얼음", "바위"), ("독", "비행", "에스퍼", "벌레"), ("고스트")),
        ("무릎차기", 85, 90, ("노말", "얼음", "바위"), ("독", "비행", "에스퍼", "벌레"), ("고스트")),
        ("돌려차기", 60, 85, ("노말", "얼음", "바위"), ("독", "비행", "에스퍼", "벌레"), ("고스트")),
        ("로킥", 60, 100, ("노말", "얼음", "바위"), ("독", "비행", "에스퍼", "벌레"), ("고스트")),
        ("받아던지기", 70, 100, ("노말", "얼음", "바위"), ("독", "비행", "에스퍼", "벌레"), ("고스트")),
        ("엄청난힘", 120, 100, ("노말", "얼음", "바위"), ("독", "비행", "에스퍼", "벌레"), ("고스트")),
        ("지옥의바퀴", 80, 80, ("노말", "얼음", "바위"), ("독", "비행", "에스퍼", "벌레"), ("고스트"))
    ]

    poison = [
        ("더스트슈트", 120, 70, ("풀"), ("독", "땅", "바위", "고스트"), 0),
        ("독엄니", 50, 100, ("풀"), ("독", "땅", "바위", "고스트"), 0),
        ("독찌르기", 80, 100, ("풀"), ("독", "땅", "바위", "고스트"), 0),
        ("독침", 15, 100, ("풀"), ("독", "땅", "바위", "고스트"), 0),
        ("크로스포이즌", 70, 100, ("풀"), ("독", "땅", "바위", "고스트"), 0),
        ("포이즌테일", 50, 100, ("풀"), ("독", "땅", "바위", "고스트"), 0),
        ("베놈쇼크", 65, 100, ("풀"), ("독", "땅", "바위", "고스트"), 0),
        ("스모그", 20, 70, ("풀"), ("독", "땅", "바위", "고스트"), 0),
        ("애시드봄", 40, 100, ("풀"), ("독", "땅", "바위", "고스트"), 0),
        ("오물공격", 65, 100, ("풀"), ("독", "땅", "바위", "고스트"), 0),
        ("오물웨이브", 95, 100, ("풀"), ("독", "땅", "바위", "고스트"), 0),
        ("오물폭탄", 90, 100, ("풀"), ("독", "땅", "바위", "고스트"), 0),
        ("용해액", 40, 100, ("풀"), ("독", "땅", "바위", "고스트"), 0),
        ("클리어스모그", 50, 100, ("풀"), ("독", "땅", "바위", "고스트"), 0),
        ("트림", 120, 90, ("풀"), ("독", "땅", "바위", "고스트"), 0)
    ]

    ground = [
        ("대지의힘", 90, 100, ("불꽃", "전기", "독", "바위"), ("풀", "벌레"), ("비행")),
        ("진흙뿌리기", 20, 100, ("불꽃", "전기", "독", "바위"), ("풀", "벌레"), ("비행")),
        ("10만마력", 95, 95, ("불꽃", "전기", "독", "바위"), ("풀", "벌레"), ("비행")),
        ("뼈다귀부메랑", 50, 90, ("불꽃", "전기", "독", "바위"), ("풀", "벌레"), ("비행")),
        ("뼈다귀치기", 65, 85, ("불꽃", "전기", "독", "바위"), ("풀", "벌레"), ("비행")),
        ("모래지옥", 35, 85, ("불꽃", "전기", "독", "바위"), ("풀", "벌레"), ("비행")),
        ("그라운드포스", 90, 100, ("불꽃", "전기", "독", "바위"), ("풀", "벌레"), ("비행")),
        ("지진", 100, 100, ("불꽃", "전기", "독", "바위"), ("풀", "벌레"), ("비행")),
        ("사우전드웨이브", 90, 100, ("불꽃", "전기", "독", "바위"), ("풀", "벌레"), ("비행")),
        ("분함의발구르기", 75, 100, ("불꽃", "전기", "독", "바위"), ("풀", "벌레"), ("비행")),
        ("매그니튜드", 50, 100, ("불꽃", "전기", "독", "바위"), ("풀", "벌레"), ("비행")),
        ("드릴라이너", 80, 95, ("불꽃", "전기", "독", "바위"), ("풀", "벌레"), ("비행")),
        ("구멍파기", 80, 100, ("불꽃", "전기", "독", "바위"), ("풀", "벌레"), ("비행")),
        ("모래지옥", 35, 85, ("불꽃", "전기", "독", "바위"), ("풀", "벌레"), ("비행"))
    ]

    fly = [
        ("공중날기", 75, 95, ("풀", "격투", "벌레"), ("전기", "바위"), 0),
        ("쪼기", 35, 100, ("풀", "격투", "벌레"), ("전기", "바위"), 0),
        ("날개치기", 60, 100, ("풀", "격투", "벌레"), ("전기", "바위"), 0),
        ("불새", 140, 90, ("풀", "격투", "벌레"), ("전기", "바위"), 0),
        ("브레이브버드", 120, 100, ("풀", "격투", "벌레"), ("전기", "바위"), 0),
        ("쪼아대기", 60, 100, ("풀", "격투", "벌레"), ("전기", "바위"), 0),
        ("화룡점정", 120, 100, ("풀", "격투", "벌레"), ("전기", "바위"), 0),
        ("회전부리", 80, 100, ("풀", "격투", "벌레"), ("전기", "바위"), 0),
        ("에어로블라스트", 100, 95, ("풀", "격투", "벌레"), ("전기", "바위"), 0),
        ("에어슬래시", 75, 95, ("풀", "격투", "벌레"), ("전기", "바위"), 0),
        ("에어컷터", 60, 95, ("풀", "격투", "벌레"), ("전기", "바위"), 0),
        ("폭풍", 110, 70, ("풀", "격투", "벌레"), ("전기", "바위"), 0),
        ("데스윙", 80, 100, ("풀", "격투", "벌레"), ("전기", "바위"), 0)
    ]

    esper = [
        ("사념의박치기", 80, 90, ("격투", "독"), ("에스퍼"), 0),
        ("사이코커터", 70, 100, ("격투", "독"), ("에스퍼"), 0),
        ("사이코팽", 85, 100, ("격투", "독"), ("에스퍼"), 0),
        ("사이코브레이크", 100, 100, ("격투", "독"), ("에스퍼"), 0),
        ("사이코쇼크", 80, 100, ("격투", "독"), ("에스퍼"), 0),
        ("사이코웨이브", 50, 100, ("격투", "독"), ("에스퍼"), 0),
        ("사이코키네시스", 90, 100, ("격투", "독"), ("에스퍼"), 0),
        ("염동력", 50, 100, ("격투", "독"), ("에스퍼"), 0),
        ("환상빔", 65, 100, ("격투", "독"), ("에스퍼"), 0),
        ("싱크로노이즈", 120, 100, ("격투", "독"), ("에스퍼"), 0),
        ("어시스트파워", 20, 100, ("격투", "독"), ("에스퍼"), 0),
        ("포톤가이저", 100, 100, ("격투", "독"), ("에스퍼"), 0),
        ("프리즘레이저", 160, 100, ("격투", "독"), ("에스퍼"), 0)
    ]

    bug = [
        ("벌레의야단법석", 90, 100, ("풀", "에스퍼"), ("불꽃", "격투", "독", "비행", "고스트"), 0),
        ("벌레의저항", 30, 100, ("풀", "에스퍼"), ("불꽃", "격투", "독", "비행", "고스트"), 0),
        ("은빛바람", 60, 100, ("풀", "에스퍼"), ("불꽃", "격투", "독", "비행", "고스트"), 0),
        ("엉겨붙기", 20, 100, ("풀", "에스퍼"), ("불꽃", "격투", "독", "비행", "고스트"), 0),
        ("시그널빔", 75, 100, ("풀", "에스퍼"), ("불꽃", "격투", "독", "비행", "고스트"), 0),
        ("연속자르기", 40, 95, ("풀", "에스퍼"), ("불꽃", "격투", "독", "비행", "고스트"), 0),
        ("시저크로스", 80, 100, ("풀", "에스퍼"), ("불꽃", "격투", "독", "비행", "고스트"), 0),
        ("벌레먹음", 60, 100, ("풀", "에스퍼"), ("불꽃", "격투", "독", "비행", "고스트"), 0),
        ("바늘미사일", 25, 95, ("풀", "에스퍼"), ("불꽃", "격투", "독", "비행", "고스트"), 0),
        ("마지막일침", 50, 100, ("풀", "에스퍼"), ("불꽃", "격투", "독", "비행", "고스트"), 0),
        ("메가폰", 120, 85, ("풀", "에스퍼"), ("불꽃", "격투", "독", "비행", "고스트"), 0),
        ("만나자마자", 90, 100, ("풀", "에스퍼"), ("불꽃", "격투", "독", "비행", "고스트"), 0),
        ("더블니들", 25, 100, ("풀", "에스퍼"), ("불꽃", "격투", "독", "비행", "고스트"), 0),
        ("공격지령", 90, 100, ("풀", "에스퍼"), ("불꽃", "격투", "독", "비행", "고스트"), 0),
        ("하드롤러", 65, 100, ("풀", "에스퍼"), ("불꽃", "격투", "독", "비행", "고스트"), 0),
        ("유턴", 70, 100, ("풀", "에스퍼"), ("불꽃", "격투", "독", "비행", "고스트"), 0)
    ]

    rock = [
        ("구르기", 30, 90, ("불꽃", "얼음", "비행", "벌레"), ("격투", "땅"), 0),
        ("다이아스톰", 100, 95, ("불꽃", "얼음", "비행", "벌레"), ("격투", "땅"), 0),
        ("돌떨구기", 50, 90, ("불꽃", "얼음", "비행", "벌레"), ("격투", "땅"), 0),
        ("떨어뜨리기", 50, 100, ("불꽃", "얼음", "비행", "벌레"), ("격투", "땅"), 0),
        ("락블레스트", 50, 90, ("불꽃", "얼음", "비행", "벌레"), ("격투", "땅"), 0),
        ("액셀록", 40, 100, ("불꽃", "얼음", "비행", "벌레"), ("격투", "땅"), 0),
        ("암석포", 150, 90, ("불꽃", "얼음", "비행", "벌레"), ("격투", "땅"), 0),
        ("암석봉인", 50, 80, ("불꽃", "얼음", "비행", "벌레"), ("격투", "땅"), 0),
        ("스톤에지", 100, 80, ("불꽃", "얼음", "비행", "벌레"), ("격투", "땅"), 0),
        ("스톤샤워", 75, 90, ("불꽃", "얼음", "비행", "벌레"), ("격투", "땅"), 0),
        ("양날박치기", 150, 80, ("불꽃", "얼음", "비행", "벌레"), ("격투", "땅"), 0),
        ("원시의힘", 60, 100, ("불꽃", "얼음", "비행", "벌레"), ("격투", "땅"), 0),
        ("파워젬", 70, 100, ("불꽃", "얼음", "비행", "벌레"), ("격투", "땅"), 0)
    ]

    ghost = [
        ("고스트다이브", 90, 100, ("에스퍼", "고스트"), 0, ("노말")),
        ("그림자꿰매기", 80, 100, ("에스퍼", "고스트"), 0, ("노말")),
        ("놀래키기", 30, 100, ("에스퍼", "고스트"), 0, ("노말")),
        ("섀도다이브", 120, 100, ("에스퍼", "고스트"), 0, ("노말")),
        ("섀도본", 85, 100, ("에스퍼", "고스트"), 0, ("노말")),
        ("섀도스틸", 90, 100, ("에스퍼", "고스트"), 0, ("노말")),
        ("섀도크루", 70, 100, ("에스퍼", "고스트"), 0, ("노말")),
        ("섀도펀치", 60, 100, ("에스퍼", "고스트"), 0, ("노말")),
        ("야습", 40, 100, ("에스퍼", "고스트"), 0, ("노말")),
        ("핥기", 30, 100, ("에스퍼", "고스트"), 0, ("노말")),
        ("괴상한바람", 60, 100, ("에스퍼", "고스트"), 0, ("노말")),
        ("나이트헤드", 80, 100, ("에스퍼", "고스트"), 0, 0),
        ("병상첨병", 65, 100, ("에스퍼", "고스트"), 0, ("노말")),
        ("섀도레이", 100, 100, ("에스퍼", "고스트"), 0, ("노말")),
        ("섀도볼", 80, 100, ("에스퍼", "고스트"), 0, ("노말"))
    ]

    dragon = [
        ("더블촙", 40, 90, ("드래곤"), 0, 0),
        ("드래곤다이브", 100, 75, ("드래곤"), 0, 0),
        ("드래곤크루", 80, 100, ("드래곤"), 0, 0),
        ("드래곤테일", 60, 90, ("드래곤"), 0, 0),
        ("드래곤해머", 90, 100, ("드래곤"), 0, 0),
        ("역린", 120, 100, ("드래곤"), 0, 0),
        ("용의숨결", 60, 100, ("드래곤"), 0, 0),
        ("용성군", 140, 90, ("드래곤"), 0, 0),
        ("시간의포효", 150, 90, ("드래곤"), 0, 0),
        ("스케일노이즈", 110, 100, ("드래곤"), 0, 0),
        ("공간절단", 100, 95, ("드래곤"), 0, 0),
        ("용의파동", 90, 100, ("드래곤"), 0, 0),
        ("코어퍼니셔", 100, 100, ("드래곤"), 0, 0),
        ("회오리", 40, 100, ("드래곤"), 0, 0)
    ]