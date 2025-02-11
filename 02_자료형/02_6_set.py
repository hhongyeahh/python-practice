s1 = set([1, 2, 3])
print(set)
s2 = set("Hello")
print(s2) # {'o', 'H', 'e', 'l'} : 중복X, 순서X

l1 = list(s1) # 리스트로 변환
print(l1)
print(l1[0])
t1 = tuple(s1) # 튜플로 변환
print(t1[0])

print(s1 & s2) # 교집합
print(s1.intersection(s2))

print(s1 | s2) # 합집합
print(s1.union(s2))

print(s1 - s2) # 차집합
print(s1.difference(s2))

s1 = set([1, 2, 3])
s1.add(4) # add : 깂 1개 추가
print(s1)

s1.update([5, 6, 7]) # update : 값 여러개 추가
print(s1)

s1.remove(2) # 특정 값 제거
print(s1)
