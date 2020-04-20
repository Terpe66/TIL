my_list = [4, 7, 9, 1, 3, 6]

# 최대/최소
max(my_list)
min(my_list)

# 특정 요소의 인덱스, my_list 안의 3이 몇 번째에 있는지
my_list.index(3)

# 리스트를 뒤집으려면?
my_list.reverse()

dust = 100
# class : int, 위의 100은 int object라고 부름
lang = 'python'
# class : str, 위의 'python'은 str object라고 부름
samsung = ['elec', 'sds', 's1']
# class : list

samsung.index('sds')
samsung.count('sds')

lang.capitalize()
# 첫 글자를 대문자로 바꾸는데 저장은 아님

lang.replace('on', 'off')
# 문자열 바꾸기, 저장 안 됨

samsung.append('bio')
