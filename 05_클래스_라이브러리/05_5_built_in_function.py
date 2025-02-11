# abs : 절대값 리턴
print(abs(3))
print(abs(-3))


# all : 입력받은 요소들이 모두 참이면 True else False
print(all([1, 2, 3]))
print(all([]))
print(all([0, 1, 2]))


# any : 입력 받은 요소들 중 하나라도 참이면 True else False
print(any([0, 0, 0, 1]))
print(any([0, 0, 0]))


# chr : 유니코드 입력 받아 해당 문자 반환
print(chr(97))


# dir : 객체가 지닌 변수나 함수를 보여줌
print(dir([1, 2, 3]))


# divmod : 숫자 2개를 입력 받아 몫 나머지 반환
print(divmod(7, 3))


# enumerate : 순서가 있는 데이터(리스트, 튜플, 문자열) 입력 받아 인덱스 값 포함하는 enumerate 객체 반환
for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)


# eval : 문자열로 구성된 표현식 입력 받아 해당 문자열 실행한 결괏값 리턴
print(eval('1+2'))  # 3
print(eval("'hi'+'a'"))  # hia
print(eval('divmod(4,3)'))  # (1,1)


# filter


# hex : 정수 입력 받아 16진수 문자열로 변환 반환
print(hex(234))


# id : 객체 입력받아 고유 주솟값 반환
a = 3
print(id(3))


# input : 사용자 입력 받는 함수
a = input()
print(a)
b = input("Enter: ")
print(b)


# int : 문자열 형태의 숫자, 소수점 있는 실수를 정수로 반환
print(int('3'))
print(int(3.4))


# isinstance(object,class) : object 가 해당 class 의 instance 인지 판단
class Person: pass
a = Person()
isinstance(a, Person)  # true
b = 3
isinstance(b, Person)  # false


# len : 입력값의 길이 반환
print(len("python"))


# list : 반복 가능한 데이터 입력 받아 리스트로 만들어 반환
a = list("python")
print(a)  # ['p', 'y', 't', 'h', 'o', 'n']
b = list((1, 2, 3))
print(b)  # [1, 2, 3]
a = [1, 2, 3]
b = list(a)  # 리스트를 복사 반환
print(b)  # [1, 2, 3]


# map(f, interable) : 입력받은 데이터의 각 요소에 함수 f 를 적용한 결과 반환
def two_times(x):
    return x * 2
list(map(two_times, [1, 2, 3]))  # [2, 4, 6, 8]
list(map(lambda x: x * 2, [1, 2, 3]))  # [2, 4, 6, 8]


# max, min
print(max([1, 2, 3]))
print(min([1, 2, 3]))


# oct : 정소를 8진수로 바꾸어 반환
print(oct(34))


# open(filename, [model]) : 파일 이름과 읽기 방법을 입력받아 파일 객체를 반환
f = open("binary_file", 'rb')


# ord : 문자의 유니코드 숫자 반환
print(ord('a'))


# pow(x,y) : x를 y제곱
print(pow(2, 4))


# range([start],stop,[step]) : 입력 받은 숫자에 해당 하는 벙위 값을 반복 가능한 객체로 만들어 반환
a = list(range(5))  # [0, 1, 2, 3, 4]
print(a)
a = list(range(5, 10))  # [5, 6, 7, 8, 9]
print(a)
a = list(range(1, 10, 2))  # [1, 3, 5, 7, 9]
print(a)
list(range(0, -10, -1))  # [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
print(a)


# round(number[,ndigits]) : 반올림 반환
print(round(4.6))  # 5
print(round(5.678, 2))  # 5.68


# sorted(iterable) : 입력 데이터 정렬 후 리스트로 반환
sorted([3, 1, 2])  # [1, 2, 3]
sorted(['a', 'c', 'b'])  # ['a,','b','c']
sorted(['zero'])  # ['e', 'o', 'r', 'z']
sorted((3, 2, 1))  # [1, 2, 3]


# str : 문자열 형태로 객체를 변환하여 반환
str(3)  # '3'
str('hi')  # 'hi'


# sum(iterable) : 입력 데이터의 합을 리턴
sum([1, 2, 3])  # 6
sum((4, 5, 6))  # 15


# tuple(iterable) : 튜플로 변환하여 반환
tuple("abc")  # ('a', 'b', 'c')
tuple([1, 2, 3])  # (1, 2, 3)
tuple((1, 2, 3))  # (1, 2, 3)


# type : 입력값의 자료형 반환
type("abe")  # <class 'str'>


# list(*iterable) : 동일한 개수로 이루어진 데이터들을 묶어서 반환
list(zip([1, 2, 3], [4, 5, 6]))  # [(1,4),(2,5),(3,6)]
list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9]))  # [(1,4,7),(2,5,8),(3,6,9)]
list(zip("abc", "def"))  # [('a','d'),('b','e'),('c','f')]
