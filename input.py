# 파이썬에서 입력을 받는 함수가 있습니다~~ 구글링해서 찾아보세요!

print('문제 1. 전화번호 받기')

print('조건 1. 저장할 때는 공백 문자 없이')
print('조건 2. -, ., , 등이 들어올 때 전부 제외 하고 숫자만 저장!')

tel = input("전화번호를 입력하세요").replace(' ','')
num = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
telephone = ' '.join(tel).split(' ')
tel_final = []
for element in telephone:
    if element not in num:
        del element
    else:
        tel_final.append(element)
print("".join(tel_final))

print('문제 2. 영어 이름 받기')
print('choi juwon 을 입력 받으면,')
print('first name : Choi, last name: Juwon 이 출력되게 만들기')

rough_name = input("영어 이름을 입력하세요")
name = rough_name.split(" ")
first_name = name[0]
last_name = name[1]
first_name_split = " ".join(first_name).split(" ")
last_name_split = " ".join(last_name).split(" ")
first_name_split[0] = first_name_split[0].upper()
last_name_split[0] = last_name_split[0].upper()
print("".join(first_name_split) + " " + "".join(last_name_split))