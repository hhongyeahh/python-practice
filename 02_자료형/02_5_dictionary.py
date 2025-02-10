# 딕셔너리 : {key : value, key2 : value2, ...}
dic = {'name' : 'pey', 'phone': '010-9999-1234','birth' : '1118'}
a = {1 : 'hi'}
a = {'a': [1,2,3]} # value에 리스트 넣을 수 있음

a = {1 : 'a'}
a[2] = 'b' # 쌍 추가
print(a)
a['name'] = 'pey' # 쌍 추가
print(a)
a[3] = [1,2,3]
print(a) # 쌍 추가

del a[1] # 쌍 삭제
print(a)

grade = {'pey' : 10, 'julliet' : 99}
print(grade['pey']) # key 로 value 얻기

a = {1:'a', 1:'b'}
print(a) # key 값이 중복된 경우, 앞의 쌍이 무시됨
# 리스트를 key로 사용할 수 없음

a = {'name':'pey', 'phone':'010-9999-1234','birth':'1118'}
print(a.keys()) # key 리스트 만들기
for k in a.keys():
        print(k)

print(list(a.keys())) #dict_keys 객체를 리스트로 변환
print(a.values()) # value 리스트 만들기
print(a.items()) # key, value 쌍 얻기
print(a.clear()) # key : value 쌍 모두 지우기

a = {'name':'pey', 'phone':'010-9999-1234','birth':'1118'}
print(a.get('name')) # key로 value 얻기
print(a.get('nokey')) # 없는 key면 None 반환, print(a['nokey']) 방식은 불가능(오류남)
print(a.get('nokey','foo')) # 디폴트 키를 설정할 수 있음
print('name' in a) # 해당 key가 dictionary 안에 있는 지 조사