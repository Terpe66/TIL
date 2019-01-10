def hangman_list():
    answer = input("맞혀야 할 단어를 입력하세요. : ")
    blank = []
    answer_list = []
    for i in answer:
        blank.append(i)
        answer_list.append(i)
    print(f"총 단어의 수는 {len(answer)}개 입니다. {('_ ' * len(answer)).strip()}")
    count = 8
    
    while count != 0:
        letter = input("이 단어가 맞나요? : ")
        if letter in answer:
            for i in answer:
                if letter == i:
                    blank(insert(answer_list.index(letter), letter)
                    blank.pop(answer_list.index(letter))
                    
                else:
                    while blank.count(i) != 0:
                        blank.insert(blank.index(i), "._")
                        blank.remove(i)
                    
                    if "._" in answer_list:
                        for al in answer_list:
                            if al != "._":
                                blank.insert(answer_list.index(al), al)
                                blank.pop(answer_list.index(al)+1)
                

            print(f"단어를 맞췄습니다. 현재 상태는 {''.join(blank)}, 남은 목숨은 {count}입니다.")
            
        else:
            count -= 1
            print(f"틀렸습니다. 현재 상태는 {''.join(blank)}, 남은 목숨은 {count}입니다.")
        
        if "._" not in blank:
            print("축하합니다! 살아남았습니다!")

    print(f"망해라!!!")
        

hangman_list()