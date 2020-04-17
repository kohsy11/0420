'''
과제 1. 별찍기 (4월 20일까지)
- 아래와 같이 * 을 출력 하는 프로그램을 만들어보세요
**********
*********
********
*******
*****
****
***
**
*

과제 2. 구구단 (4월 20일까지)
- 구구단 2단을 출력해보세요!

과제 3. while 문을 활용하여 1부터 1000까지의 자연수 중 3의 배수의 합을 구해보세요. (4월 20일까지)

과제 4. for 문을 활용하여 멋사 학생들의 평균 점수를 구해보세요. (4월 20일까지)
- mutsa_scores = [90, 77, 40, 55, 90, 100, 88]

과제 5. input.py 문제 2개 풀기 (4월 20일까지)

과제 6. HTML / CSS 페이스북 모바일 클론코딩 (4월 27일까지)
- 이미지 자율
- 까먹기전에 해주세요~

'''

# 과제 1. 별찍기

a = 10
while a <= 10:
    a = a - 1
    print("*" * a)
    if a == 0:
        break


# 과제 2. 구구단

num = range(10)
for a in num:
    print("2 x", a, "=", (a * 2))

# 과제 3. while 문을 활용하여 1부터 1000까지의 자연수 중 3의 배수의 합을 구해보세요.

total = 0
three = 1
while three <= 1000:
    if three % 3 == 0:
       total = total + three
    three = three + 1

print("3의 배수의 총 합은 %d 입니다" % total)

# 과제 4. for 문을 활용하여 멋사 학생들의 평균 점수를 구해보세요. (4월 20일까지)
mutsa_scores = [90, 77, 40, 55, 90, 100, 88]
total = 0
for score in mutsa_scores:
    total = score + total
print(total/len(mutsa_scores))