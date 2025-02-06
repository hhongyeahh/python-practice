a = "Life is too short, You need Python"
b = "a"
c = "123"
print(type(a))
print(type(b))
print(type(c))

# 문자열 만들기(4가지 방법)
"Hello World"
'Python is fun'
"""Life is too short, You need Python"""
'''Life is too short, You need Python'''

# 따옴표 속 따옴표
a = "'Life' is too short, You need Python"
b = '"Life" is too short, You need Python'
c = "Life\" is too short, You need Python"
d = "Life's are too short, You need Python"
e = 'Life\'s are too short, You need Python'
print(a)
print(b)
print(c)
print(d)
print(e)

# 줄바꾸기
a = "Life is too short,\nYou need Python"
print(a)

a = '''Life is too short,
You need Python
'''
print(a)

a = """Life is too short,
You need Python
"""
print(a)

# 문자열 연산하기
head = "Python"
tail = "is fun!"
print(head + tail)

a = "python"
print(a*2) # print(a*a) 불가 : 문자열과 숫자만 곱하기 가능

print("="*50)
print("My program")
print("="*50)

# 문자열 길이 구하기
a = "Life is too short"
print(len(a))

# 문자열 인덱싱(0부터 시작)
a = "Life is too short, You need Python"
print(a[3]) # 'e'

print(a[0]) #L
print(a[-1]) #n : 문자열을 뒤에서부터 읽기
print(a[-34]) #L

# 문자열 슬라이싱(끝 번호에 해당하는 문자는 포함하지 않음)
print(a[0:4])
print(a[12:17])

print(a[19:]) # 끝 번호 생략 : 시작번호에서 문자열 끝까지
print(a[:19]) # 시작 번호 생략 : 문자열 처음부터 끝 번호까지
print(a[:]) # 문자열 처음부터 끝까지
print(a[::-1]) # 문자열 거꾸로 출력 [start:stop:step]
print(a[19:-7]) # a[19] ~ a[-8]

# 슬라이싱으로 문자열 나누기
a = "20230331Rainy"
date = a[:8]
weather = a[8:]
print(date)
print(weather)

a = "Pithon" # a[1] = 'y' : 문자열은 immutable해서 불가능
b = a[:1] + 'y' + a[2:]
print(b)

# 문자열 포매팅
a = "I eat %d apples." % 3 # 숫자 바로 대입
print(a)

a = "I eat %s apples." % "five" # 문자열 바로 대입
print(a)

number = 3
a = "I eat %d apples." % number # 변수로 대입
print(a)

day = "three"
a = "I ate %d apples. so I was sick for %s days." %(number, day)
print(a)

a = "I have %s apples" % 3 # %s는 어떤 형태의 값이든 변환 가능
print(a)
a = "I have %s apples." % "three"
print(a)
a = "rate is %s" % 3.234
print(a)

a = "Error is %d%%." % 98 # %를 사용하고 싶다면, %% 두번
print(a)

a = "I eat {0} apples.".format(3) # format 힘수 사용하기
print(a)
a = "I have {0} apples.".format("five")
print(a)
a = "I have {0} apples.".format(number)
print(a)
a = "I ate {0} apples. so I was sick for {1} days.".format(number, day)
print(a)
a = "I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3)
print(a)
a = "I ate {0} apples. so I was sick for {day} days.".format(10,day=30)
print(a)

# f 문자열 포매팅
name = '홍길동'
age = 30
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')
print(f'나는 내년이면 {age+1}살이 된다.')

d = {'name':'홍길동','age':30}
print(f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.')

# 문자열 관련 함수
a = "hobby"
print(a.count('b')) # 문자 개수 세기

a = "Python is the best choice"
print(a.find('b')) # 위치 알려주기 : find
print(a.find('k')) # 존재하지 않는 경우 -1 반환

print(a.index('t')) # 위치 알려주기 : index -> 없는 문자열의 경우 오류!

print(",".join('abcd')) # 문자열 삽입
print(",".join(['a','b','c','d']))

print(a.upper())
print(a.lower())

a = "hi "
print(a.lstrip()) # 왼쪽 공백 지우기
a = " hi"
print(a.rstrip()) # 오른쪽 공백 지우기
a = " hi "
print(a.strip()) # 양쪽 공백 지우기

a = "Life is too short"
print(a.replace("Life", "Your leg")) # 문자열 바꾸기

print(a.split()) # 문자열 나누기
b = "a:b:c:d"
print(b.split(':'))



