a = 1
b = 'python'
c = [1,2,3]
print(id(a)) # 변수가 가리키는 메모리 주소
b = c # 리스트 복사
print(b)
print(b is c) # True : 주소값을 넣게 됨

a = [1,2,3]
b = a[:]
print(b)
print( a is b ) # False
print( a == b) # True
b = a.copy() # copy 모듈
print(a is b) # False : 값 복사

a, b = ('python','life')
(a,b) = 'python','life' # a, b = ('python','life') 와 같은 표현 : 튜플은 괄호 생략 가능

[a,b] = ['python','life'] # 리스트로 변수 만들기
a = b = 'python'

a = 3
b = 5
a,b = b,a # a와 b의 값 바꿈
print(a,",",b)
