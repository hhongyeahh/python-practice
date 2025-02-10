a = True
b = False
print(type(a))
print(type(b))
print(1 == 1)
print(2 > 1)
print(2 < 1)

a = [1,2,3,4]
while a : # a가 참인 동안 (none이 아닌 동안)
    print(a.pop()) # 리스트의 마지막 요소를 하나씩 꺼냄

if []:
    print("참")
else:
    print("거짓")

if [1,2,3]: # [1,2,3] : 요소 값이 있는 리스트이기 때문에 "참"
    print("참")
else :
    print("거짓")

print(bool('python')) # True
print(bool('')) # False : 비어있기 때문에
print(bool([1,2,3])) # True
print(bool([])) # False
print(bool(0)) # False
print(bool(3)) # True