def add(a, b):
    return a + b  # a,b 매개변수
print(add(3, 4))  # 3,4 인수


# 입력값이 없는 함수
def say():
    return 'Hi'
a = say()
print(a)


# 리턴값이 없는 함수
def add(a, b):
    print("%d, %d의 합은 %d입니다." % (a, b, a + b))
add(3, 4)
a = add(3, 4)
print(a)  # none 출력 -> return 값이 없기 때문에


# 입력값도 리턴값도 없는 함수
def say():
    print('Hi')
say()


# 매개변수 지정 호출
def sub(a, b):
    return a - b
result = sub(a=7, b=3)
print(result)
result = sub(b=5,a=3) # 지정하면 순서를 바꿔도 가능
print(result)


# 여러개의 입력값 받는 함수
def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result
result = add_many(1,2,3,4,5,6,7,8,9,10)
print(result)

def add_mul(choice, *args):
    if choice == 'add':
        result = 0
        for i in args:
            result = result + i
    elif choice == 'mul':
        result = 1
        for i in args:
            result = result * i
    return result
result = add_mul('add', 1,2,3,4,5)
print(result)
result = add_mul('mul',1,2,3,4,5)
print(result)


# 키워드 매개변수, kwargs : 매개변수 앞에 **를 붙이면 딕셔너리
def print_kwargs(**kwargs):
    print(kwargs)
print_kwargs(a=1)
print_kwargs(name='foo',age=3)


# 함수의 리턴값은 언제나 하나
def add_and_mul(a,b):
    return a+b, a*b
result = add_and_mul(3,4)
print(result) # 튜플값 하나인 (a+b, a*b) 로 리턴됨
result1, result2 = add_and_mul(3,4)
print(result1, result2) # 튜플 값을 2개로 분리하여 받고 싶다면 이렇게 호출


# 매개변수 초깃값 미리 설정
def say_myself(name,age,man=True):
    print("나의 이름은 %s입니다." %name)
    print("나이는 %d살입니다." %age)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")
say_myself("김도록",27)
say_myself("김혜원",27,False)


# 변수의 효력 범위
a = 1
def vartest(a):
    a = a + 1
vartest(a)
print(a) # a : 1

a = 1
def vartest(a):
    a = a + 1
    return a # return
a = vartest(a)
print(a)

g = 1
def vartest():
    global g # 전역변수
    g = g + 1
vartest()
print(g)


# lambda 예약어
add = lambda a,b:a+b # 함수이름 = lambda 매개변수 ... : 매개변수를 이용한 표현식
result = add(3,5)
print(result)
