a = []
b = [1,2,3]
c = ['Life','is','too','short']
d = [1,2,'Life','is']
e = [1,2,['Life','is']] # 리스트 안에는 어떠한 자료형도 포함할 수 있음
print(type(a),type(b),type(c),type(d),type(e))

# 리스트 인덱싱
a = [1,2,3]
print(a)
print(a[0])
print(a[0] + a[2]) # a = [1,'2','3'] : 문자열인 경우 a[0] + a[2] 불가능
print(a[-1])

a = [1,2,3,['a','b','c']]
print(a[0])
print(a[-1])
print(a[3])
print(a[-1][0])
print(a[3][1])

# 리스트 슬라이싱
a = [1,2,3,4,5]
print(a[0:2])
print(a[:2]) # [1, 2]
b = a[:2]
c = a[2:]
print(b, c)
print(a[1:3]) # [2, 3]

a = [1,2,3,['a','b','c'],4,5]
print(a[2:5])
print(a[3][:2])

# 리스트 연산하기
a = [1,2,3]
b = [4,5,6]
print(a+b)
print(a*3)
print(len(a))
print(a[1]+a[2]) # 5 (if) 자료형이 다른 경우 불가능 : a[1] + "hi" 불가


# 리스트 수정 삭제
a = [1,2,3]
a[2] = 4
print(a)
del a[1]
print(a)

a = [1,2,3,4,5]
del a[2:]
print(a)

# 리스트 관련 함수
a = [1,2,3]

a.append(4) # 리스트에 요소추가
a.append([5,6]) # 어떤 자료형든 추가가능
a.append("tree")
print(a)

a = [1,4,3,2]
a.sort() # 리스트 요소 정렬
print(a)
a = ['a','c','b']
a.sort()
print(a)

a.reverse()
print(a)

a = [1,2,3]
print(a.index(3)) # 리스트의 3번째 요소의 위칫값(인덱스 값) = a[2]의 위칫값이니 2
print(a.index(1)) # 리스트의 1번째 요소의 위칫값(인덱스 값) = a[0]의 위칫값이니 0

a.insert(0,4) # a[0]위치에 4삽입
print(a)
a.insert(3,5)
print(a)

a.remove(3) # 리스트 요소 제거
print(a)

a = [1,2,3,4,5]
a.pop() # 리스트 요소 끄집어 내기 : 리스트의 맨 마지막 요소를 리턴하고 그 요소 삭제
print(a)
a.pop(2) # 리스트의 x번째 요소(a[x])를 리턴하고 그 요소 삭제
print(a)

a = [1,1,2,3,4]
print(a.count(1)) # 요소 x의 개수 세기

a.extend([5,6]) # 리스트 확장
print(a)
b = [7,8]
a.extend(b)
print(a)

