import random
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

        self.hp = int(self.level * random.choice([7.9, 8.7, 9.3, 10.7]))
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
            

class Bulbasaur(Pokemon):
    def __init__(self):
        super().__init__("이상해씨", 1, 45, ("풀", "독"))        
        pass

class Ivysaur(Pokemon):
    def __init__(self):
        super().__init__("이상해풀", 2, 60, ("풀", "독"))
        pass

class Venusaur(Pokemon):
    def __init__(self):
        super().__init__("이상해꽃", 3, 80, ("풀", "독"))
        pass

class Charmander(Pokemon):
    def __init__(self):
        super().__init__("파이리", 1, 65, ("불꽃"))
        pass

class Charmeleon(Pokemon):
    def __init__(self):
        super().__init__("리자드", 2, 80, ("불꽃"))
        pass

class Charizard(Pokemon):
    def __init__(self):
        super().__init__("리자몽", 3, 100, ("불꽃", "비행"))
        pass

class Squirtle(Pokemon):
    def __init__(self):
        super().__init__("꼬부기", 1, 43, ("물"))
        pass

class Wartortle(Pokemon):
    def __init__(self):
        super().__init__("어니부기", 2, 58, ("물"))
        pass

class Blastoise(Pokemon):
    def __init__(self):
        super().__init__("거북왕", 3, 78, ("물"))
        pass

class Caterpie(Pokemon):
    def __init__(self):
        super().__init__("캐터피", 8, 45, ("벌레"))
        pass

class Metapod(Pokemon):
    def __init__(self):
        super().__init__("단데기", 9, 30, ("벌레"))
        pass

class Butterfree(Pokemon):
    def __init__(self):
        super().__init__("버터플", 0, 70, ("벌레", "비행"))
        pass

class Weedle(Pokemon):
    def __init__(self):
        super().__init__("뿔충이", 8, 50, ("벌레", "독"))
        pass

class Kakuna(Pokemon):
    def __init__(self):
        super().__init__("딱충이", 9, 35, ("벌레", "독"))
        pass

class Beedrill(Pokemon):
    def __init__(self):
        super().__init__("독침붕", 0, 75, ("벌레", "독"))
        pass

class Pidgey(Pokemon):
    def __init__(self):
        super().__init__("구구", 1, 56, ("노말", "비행"))
        pass

class Pidgeotto(Pokemon):
    def __init__(self):
        super().__init__("피죤", 2, 71, ("노말", "비행"))
        pass

class Pidgeot(Pokemon):
    def __init__(self):
        super().__init__("피죤투", 3, 91, ("노말", "비행"))
        pass

class Rattata(Pokemon):
    def __init__(self):
        super().__init__("꼬렛", 4, 72, ("노말"))
        pass

class Raticate(Pokemon):
    def __init__(self):
        super().__init__("레트라", 5, 97, ("노말"))
        pass

class Spearow(Pokemon):
    def __init__(self):
        super().__init__("깨비참", 4, 70, ("노말", "비행"))
        pass

class Fearow(Pokemon):
    def __init__(self):
        super().__init__("깨비드릴조", 5, 100, ("노말", "비행"))
        pass

class Ekans(Pokemon):
    def __init__(self):
        super().__init__("아보", 4, 55, ("독"))
        pass

class Arbok(Pokemon):
    def __init__(self):
        super().__init__("아보크", 5, 80, ("독"))
        pass

class Pikachu(Pokemon):
    def __init__(self):
        super().__init__("피카츄", 4, 90, ("전기"))
        pass

class Raichu(Pokemon):
    def __init__(self):
        super().__init__("라이츄", 5, 100, ("전기"))
        pass

class Sandshrew(Pokemon):
    def __init__(self):
        super().__init__("모래두지", 4, 40, ("땅"))
        pass

class Sandslash(Pokemon):
    def __init__(self):
        super().__init__("고지", 5, 55, ("땅"))
        pass

class Nidoranf(Pokemon):
    def __init__(self):
        super().__init__("니드런f", 1, 41, ("독"))
        pass

class Nidorina(Pokemon):
    def __init__(self):
        super().__init__("니드리나", 2, 56, ("독"))
        pass

class Nidoqueen(Pokemon):
    def __init__(self):
        super().__init__("니드퀸", 3, 76, ("독", "땅"))
        pass

class Nidoranm(Pokemon):
    def __init__(self):
        super().__init__("니드런m", 1, 50, ("독"))
        pass

class Nidorino(Pokemon):
    def __init__(self):
        super().__init__("니드리노", 2, 65, ("독"))
        pass

class Nidoking(Pokemon):
    def __init__(self):
        super().__init__("니드킹", 3, 85, ("독", "땅"))
        pass

class Clefairy(Pokemon):
    def __init__(self):
        super().__init__("삐삐", 4, 35, ("노말"))
        pass

class Clefable(Pokemon):
    def __init__(self):
        super().__init__("픽시", 5, 60, ("노말"))
        pass

class Vulpix(Pokemon):
    def __init__(self):
        super().__init__("식스테일", 4, 65, ("불꽃"))
        pass

class Ninetales(Pokemon):
    def __init__(self):
        super().__init__("나인테일", 5, 100, ("불꽃"))
        pass

class Jigglypuff(Pokemon):
    def __init__(self):
        super().__init__("푸린", 4, 20, ("노말"))
        pass

class Wigglytuff(Pokemon):
    def __init__(self):
        super().__init__("푸크린", 5, 45, ("노말"))
        pass

class Zubat(Pokemon):
    def __init__(self):
        super().__init__("주뱃", 4, 55, ("독", "비행"))
        pass

class Golbat(Pokemon):
    def __init__(self):
        super().__init__("골뱃", 5, 90, ("독", "비행"))
        pass

class Oddish(Pokemon):
    def __init__(self):
        super().__init__("뚜벅초", 4, 30, ("풀", "독"))
        pass

class Gloom(Pokemon):
    def __init__(self):
        super().__init__("냄새꼬", 5, 40, ("풀", "독"))
        pass

class Vileplume(Pokemon):
    def __init__(self):
        super().__init__("라플레시아", 6, 50, ("풀", "독"))
        pass

class Paras(Pokemon):
    def __init__(self):
        super().__init__("파라스", 4, 25, ("벌레", "풀"))
        pass

class Parasect(Pokemon):
    def __init__(self):
        super().__init__("파라섹트", 5, 30, ("벌레", "풀"))
        pass

class Venonat(Pokemon):
    def __init__(self):
        super().__init__("콘팡", 0, 45, ("벌레", "독"))
        pass

class Venomoth(Pokemon):
    def __init__(self):
        super().__init__("도나리", 6, 90, ("벌레", "독"))
        pass

class Diglett(Pokemon):
    def __init__(self):
        super().__init__("디그다", 4, 95, ("땅"))
        pass

class Dugtrio(Pokemon):
    def __init__(self):
        super().__init__("닥트리오", 5, 120, ("땅"))
        pass

class Meowth(Pokemon):
    def __init__(self):
        super().__init__("나옹", 0, 90, ("노말"))
        pass

class Persian(Pokemon):
    def __init__(self):
        super().__init__("페르시온", 6, 115, ("노말"))
        pass

class Psyduck(Pokemon):
    def __init__(self):
        super().__init__("고라파덕", 0, 55, ("물"))
        pass

class Golduck(Pokemon):
    def __init__(self):
        super().__init__("골덕", 6, 85, ("물"))
        pass

class Mankey(Pokemon):
    def __init__(self):
        super().__init__("망키", 0, 45, ("격투"))
        pass

class Primeape(Pokemon):
    def __init__(self):
        super().__init__("성원숭", 6, 95, ("격투"))
        pass

class Growlithe(Pokemon):
    def __init__(self):
        super().__init__("가디", 0, 60, ("불꽃"))
        pass

class Arcanine(Pokemon):
    def __init__(self):
        super().__init__("윈디", 6, 95, ("불꽃"))
        pass

class Poliwag(Pokemon):
    def __init__(self):
        super().__init__("발챙이", 4, 90, ("물"))
        pass

class Poliwhirl(Pokemon):
    def __init__(self):
        super().__init__("수륙챙이", 5, 90, ("물"))
        pass

class Poliwrath(Pokemon):
    def __init__(self):
        super().__init__("강챙이", 6, 70, ("물", "격투"))
        pass

class Abra(Pokemon):
    def __init__(self):
        super().__init__("캐이시", 1, 90, ("에스퍼"))
        pass

class Kadabra(Pokemon):
    def __init__(self):
        super().__init__("윤겔라", 2, 105, ("에스퍼"))
        pass

class Alakazam(Pokemon):
    def __init__(self):
        super().__init__("후딘", 3, 120, ("에스퍼"))
        pass

class Machop(Pokemon):
    def __init__(self):
        super().__init__("알통몬", 0, 35, ("격투"))
        pass

class Machoke(Pokemon):
    def __init__(self):
        super().__init__("근육몬", 5, 45, ("격투"))
        pass

class Machamp(Pokemon):
    def __init__(self):
        super().__init__("괴력몬", 6, 55, ("격투"))
        pass

class Bellsprout(Pokemon):
    def __init__(self):
        super().__init__("모다피", 4, 40, ("풀", "독"))
        pass

class Weepinbell(Pokemon):
    def __init__(self):
        super().__init__("우츠동", 5, 55, ("풀", "독"))
        pass

class Victreebel(Pokemon):
    def __init__(self):
        super().__init__("우츠보트", 6, 70, ("풀", "독"))
        pass

class Tentacool(Pokemon):
    def __init__(self):
        super().__init__("왕눈해", 0, 70, ("물", "독"))
        pass

class Tentacruel(Pokemon):
    def __init__(self):
        super().__init__("독파리", 6, 100, ("물", "독"))
        pass

class Geodude(Pokemon):
    def __init__(self):
        super().__init__("꼬마돌", 4, 20, ("바위", "땅"))
        pass

class Graveler(Pokemon):
    def __init__(self):
        super().__init__("데구리", 5, 35, ("바위", "땅"))
        pass

class Golem(Pokemon):
    def __init__(self):
        super().__init__("딱구리", 6, 45, ("바위", "땅"))
        pass

class Ponyta(Pokemon):
    def __init__(self):
        super().__init__("포니타", 0, 90, ("불꽃"))
        pass

class Rapidash(Pokemon):
    def __init__(self):
        super().__init__("날쌩마", 6, 105, ("불꽃"))
        pass

class Slowpoke(Pokemon):
    def __init__(self):
        super().__init__("야돈", 0, 15, ("물", "에스퍼"))
        pass

class Slowbro(Pokemon):
    def __init__(self):
        super().__init__("야도란", 6, 30, ("물", "에스퍼"))
        pass

class Magnemite(Pokemon):
    def __init__(self):
        super().__init__("코일", 0, 45, ("전기"))
        pass

class Magneton(Pokemon):
    def __init__(self):
        super().__init__("레어코일", 6, 70, ("전기"))
        pass

class Farfetchd(Pokemon):
    def __init__(self):
        super().__init__("파오리", 0, 60, ("노말", "비행"))
        pass

class Doduo(Pokemon):
    def __init__(self):
        super().__init__("두두", 0, 75, ("노말", "비행"))
        pass

class Dodrio(Pokemon):
    def __init__(self):
        super().__init__("두트리오", 6, 100, ("노말", "비행"))
        pass

class Seel(Pokemon):
    def __init__(self):
        super().__init__("쥬쥬", 0, 45, ("물"))
        pass

class Dewgong(Pokemon):
    def __init__(self):
        super().__init__("쥬레곤", 6, 70, ("물, 얼음"))
        pass

class Grimer(Pokemon):
    def __init__(self):
        super().__init__("질퍽이", 0, 25, ("독"))
        pass

class Muk(Pokemon):
    def __init__(self):
        super().__init__("질뻐기", 6, 50, ("독"))
        pass

class Shellder(Pokemon):
    def __init__(self):
        super().__init__("셀러", 0, 40, ("물"))
        pass

class Cloyster(Pokemon):
    def __init__(self):
        super().__init__("파르셀", 6, 70, ("물", "얼음"))
        pass

class Gastly(Pokemon):
    def __init__(self):
        super().__init__("고오스", 4, 80, ("고스트", "독"))
        pass

class Haunter(Pokemon):
    def __init__(self):
        super().__init__("고우스트", 5, 95, ("고스트", "독"))
        pass

class Gengar(Pokemon):
    def __init__(self):
        super().__init__("팬텀", 6, 110, ("고스트", "독"))
        pass

class Onix(Pokemon):
    def __init__(self):
        super().__init__("롱스톤", 0, 70, ("바위", "땅"))
        pass

class Drowzee(Pokemon):
    def __init__(self):
        super().__init__("슬리프", 4, 42, ("에스퍼"))
        pass

class Hypno(Pokemon):
    def __init__(self):
        super().__init__("슬리퍼", 5, 67, ("에스퍼"))
        pass

class Krabby(Pokemon):
    def __init__(self):
        super().__init__("크랩", 4, 50, ("물"))
        pass

class Kingler(Pokemon):
    def __init__(self):
        super().__init__("킹크랩", 5, 75, ("물"))
        pass

class Voltorb(Pokemon):
    def __init__(self):
        super().__init__("찌리리공", 0, 100, ("전기"))
        pass

class Electrode(Pokemon):
    def __init__(self):
        super().__init__("붐볼", 6, 140, ("전기"))
        pass

class Exeggcute(Pokemon):
    def __init__(self):
        super().__init__("아라리", 0, 40, ("풀", "에스퍼"))
        pass

class Exeggutor(Pokemon):
    def __init__(self):
        super().__init__("나시", 6, 55, ("물", "에스퍼"))
        pass

class Cubone(Pokemon):
    def __init__(self):
        super().__init__("탕구리", 0, 35, ("땅"))
        pass

class Marowak(Pokemon):
    def __init__(self):
        super().__init__("텅구리", 6, 45, ("땅"))
        pass

class Hitmonlee(Pokemon):
    def __init__(self):
        super().__init__("시라소몬", 6, 87, ("격투"))
        pass

class Hitmonchan(Pokemon):
    def __init__(self):
        super().__init__("홍수몬", 6, 76, ("격투"))
        pass

class Lickitung(Pokemon):
    def __init__(self):
        super().__init__("내루미", 6, 30, ("노말"))
        pass

class Koffing(Pokemon):
    def __init__(self):
        super().__init__("또가스", 0, 35, ("독"))
        pass

class Weezing(Pokemon):
    def __init__(self):
        super().__init__("또도가스", 6, 60, ("독"))
        pass

class Rhyhorn(Pokemon):
    def __init__(self):
        super().__init__("뿔카노", 0, 25, ("땅", "바위"))
        pass

class Rhydon(Pokemon):
    def __init__(self):
        super().__init__("코뿌리", 6, 40, ("땅", "바위"))
        pass

class Chansey(Pokemon):
    def __init__(self):
        super().__init__("럭키", 6, 50, ("노말"))
        pass

class Tangela(Pokemon):
    def __init__(self):
        super().__init__("덩쿠리", 5, 60, ("풀"))
        pass

class Kangaskhan(Pokemon):
    def __init__(self):
        super().__init__("캥카", 0, 90, ("노말"))
        pass

class Horsea(Pokemon):
    def __init__(self):
        super().__init__("쏘드라", 0, 60, ("물"))
        pass

class Seadra(Pokemon):
    def __init__(self):
        super().__init__("시드라", 6, 85, ("물"))
        pass

class Goldeen(Pokemon):
    def __init__(self):
        super().__init__("콘치", 0, 63, ("물"))
        pass

class Seaking(Pokemon):
    def __init__(self):
        super().__init__("왕콘치", 6, 68, ("물"))
        pass

class Staryu(Pokemon):
    def __init__(self):
        super().__init__("별가사리", 0, 85, ("물"))
        pass

class Starmie(Pokemon):
    def __init__(self):
        super().__init__("아쿠스타", 6, 115, ("물", "에스퍼"))
        pass

class Mr_Mime(Pokemon):
    def __init__(self):
        super().__init__("마임맨", 5, 90, ("에스퍼"))
        pass

class Scyther(Pokemon):
    def __init__(self):
        super().__init__("스라크", 6, 105, ("벌레", "비행"))
        pass

class Jynx(Pokemon):
    def __init__(self):
        super().__init__("루주라", 6, 95, ("얼음", "에스퍼"))
        pass

class Electabuzz(Pokemon):
    def __init__(self):
        super().__init__("에레브", 6, 105, ("전기"))
        pass

class Magmar(Pokemon):
    def __init__(self):
        super().__init__("마그마", 6, 93, ("불꽃"))
        pass

class Pinsir(Pokemon):
    def __init__(self):
        super().__init__("쁘사이저", 6, 85, ("벌레"))
        pass

class Tauros(Pokemon):
    def __init__(self):
        super().__init__("켄타로스", 6, 110, ("노말"))
        pass

class Magikarp(Pokemon):
    def __init__(self):
        super().__init__("잉어킹", 4, 80, ("노말"))
        pass

class Gyarados(Pokemon):
    def __init__(self):
        super().__init__("갸라도스", 5, 81, ("물", "비행"))
        pass

class Lapras(Pokemon):
    def __init__(self):
        super().__init__("라프라스", 6, 60, ("물", "얼음"))
        pass

class Ditto(Pokemon):
    def __init__(self):
        super().__init__("메타몽", 0, 999, ("노말"))
        pass

class Eevee(Pokemon):
    def __init__(self):
        super().__init__("이브이", 4, 55, ("노말"))
        pass

class Vaporeon(Pokemon):
    def __init__(self):
        super().__init__("샤미드", 5, 65, ("물"))
        pass

class Jolteon(Pokemon):
    def __init__(self):
        super().__init__("쥬피썬더", 5, 130, ("전기"))
        pass

class Flareon(Pokemon):
    def __init__(self):
        super().__init__("부스터", 5, 65, ("불꽃"))
        pass

class Porygon(Pokemon):
    def __init__(self):
        super().__init__("폴리곤", 0, 40, ("노말"))
        pass

class Omanyte(Pokemon):
    def __init__(self):
        super().__init__("암나이트", 0, 35, ("바위", "물"))
        pass

class Omastar(Pokemon):
    def __init__(self):
        super().__init__("암스타", 6, 55, ("바위", "물"))
        pass

class Kabuto(Pokemon):
    def __init__(self):
        super().__init__("투구", 0, 55, ("바위", "물"))
        pass

class Kabutops(Pokemon):
    def __init__(self):
        super().__init__("투구푸스", 6, 80, ("바위", "물"))
        pass

class Aerodactyl(Pokemon):
    def __init__(self):
        super().__init__("프테라", 6, 130, ("바위", "비행"))
        pass

class Snorlax(Pokemon):
    def __init__(self):
        super().__init__("잠만보", 6, 30, ("노말"))
        pass

class Articuno(Pokemon):
    def __init__(self):
        super().__init__("프리져", 7, 85, ("얼음", "비행"))
        pass

class Zapdos(Pokemon):
    def __init__(self):
        super().__init__("썬더", 7, 100, ("전기", "비행"))
        pass

class Moltres(Pokemon):
    def __init__(self):
        super().__init__("파이어", 7, 90, ("불꽃", "비행"))
        pass

class Dratini(Pokemon):
    def __init__(self):
        super().__init__("미뇽", 0, 50, ("드래곤"))
        pass

class Dragonair(Pokemon):
    def __init__(self):
        super().__init__("신뇽", 6, 70, ("드래곤"))
        pass

class Dragonite(Pokemon):
    def __init__(self):
        super().__init__("망나뇽", 7, 80, ("드래곤", "비행"))
        pass

class Mewtwo(Pokemon):
    def __init__(self):
        super().__init__("뮤츠", 7, 130, ("에스퍼"))
        pass

class Mew(Pokemon):
    def __init__(self):
        super().__init__("뮤", 7, 100, ("에스퍼"))
        pass


class_list = [
    Bulbasaur, 
    Ivysaur, 
    Venusaur, 
    Charmander, 
    Charmeleon, 
    Charizard, 
    Squirtle, 
    Wartortle, 
    Blastoise, 
    Caterpie, 
    Metapod, 
    Butterfree, 
    Weedle, 
    Kakuna, 
    Beedrill, 
    Pidgey, 
    Pidgeotto, 
    Pidgeot, 
    Rattata, 
    Raticate, 
    Spearow, 
    Fearow, 
    Ekans, 
    Arbok, 
    Pikachu, 
    Raichu, 
    Sandshrew, 
    Sandslash, 
    Nidoranf, 
    Nidorina, 
    Nidoqueen, 
    Nidoranm, 
    Nidorino, 
    Nidoking, 
    Clefairy, 
    Clefable, 
    Vulpix, 
    Ninetales, 
    Jigglypuff, 
    Wigglytuff, 
    Zubat, 
    Golbat, 
    Oddish, 
    Gloom, 
    Vileplume, 
    Paras, 
    Parasect, 
    Venonat, 
    Venomoth, 
    Diglett, 
    Dugtrio, 
    Meowth, 
    Persian, 
    Psyduck, 
    Golduck, 
    Mankey, 
    Primeape, 
    Growlithe, 
    Arcanine, 
    Poliwag, 
    Poliwhirl, 
    Poliwrath, 
    Abra, 
    Kadabra, 
    Alakazam, 
    Machop, 
    Machoke, 
    Machamp, 
    Bellsprout, 
    Weepinbell, 
    Victreebel, 
    Tentacool, 
    Tentacruel, 
    Geodude, 
    Graveler, 
    Golem, 
    Ponyta, 
    Rapidash, 
    Slowpoke, 
    Slowbro, 
    Magnemite, 
    Magneton, 
    Farfetchd, 
    Doduo, 
    Dodrio, 
    Seel, 
    Dewgong, 
    Grimer, 
    Muk, 
    Shellder, 
    Cloyster, 
    Gastly, 
    Haunter, 
    Gengar, 
    Onix, 
    Drowzee, 
    Hypno, 
    Krabby, 
    Kingler, 
    Voltorb, 
    Electrode, 
    Exeggcute, 
    Exeggutor, 
    Cubone, 
    Marowak, 
    Hitmonlee, 
    Hitmonchan, 
    Lickitung, 
    Koffing, 
    Weezing, 
    Rhyhorn, 
    Rhydon, 
    Chansey, 
    Tangela, 
    Kangaskhan, 
    Horsea, 
    Seadra, 
    Goldeen, 
    Seaking, 
    Staryu, 
    Starmie, 
    Mr_Mime, 
    Scyther, 
    Jynx, 
    Electabuzz, 
    Magmar, 
    Pinsir, 
    Tauros, 
    Magikarp, 
    Gyarados, 
    Lapras, 
    Ditto, 
    Eevee, 
    Vaporeon, 
    Jolteon, 
    Flareon, 
    Porygon, 
    Omanyte, 
    Omastar, 
    Kabuto, 
    Kabutops, 
    Aerodactyl, 
    Snorlax, 
    Articuno, 
    Zapdos, 
    Moltres, 
    Dratini, 
    Dragonair, 
    Dragonite, 
    Mewtwo, 
    Mew
]


print("====포켓몬 리스트====")
for num in range(1, 149, 3):
    print(f"{num}. {class_list[num - 1]().name}    {num + 1}. {class_list[num]().name}    {num + 2}. {class_list[num + 1]().name}")
print("====================")