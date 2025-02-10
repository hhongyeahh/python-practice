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
