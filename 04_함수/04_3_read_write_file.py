#파일 생성
f = open("새파일.txt","w")
f.close()
f = open("/Users/hyewon/Desktop/딥러닝/파이썬/python-practice/04_함수/새파일.txt","w")
f.close()


# 파일 쓰기모드
f = open("/Users/hyewon/Desktop/딥러닝/파이썬/python-practice/04_함수/새파일.txt","w")
for i in range(1,11):
    data = "%d번째 줄입니다.\n" %i
    f.write(data)
f.close()


# readline 함수
f = open("/Users/hyewon/Desktop/딥러닝/파이썬/python-practice/04_함수/새파일.txt","r")
line = f.readline()
print(line)
f.close()

f = open("/Users/hyewon/Desktop/딥러닝/파이썬/python-practice/04_함수/새파일.txt","r")

while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()


# readlines 함수 : 파일의 모든 줄을 읽어서 각각의 줄을 요소를 가지는 리스트를 리턴
f = open("/Users/hyewon/Desktop/딥러닝/파이썬/python-practice/04_함수/새파일.txt","r")
lines = f.readlines()
for line in lines:
    print(line)
f.close()


# read 함수 : 파일의 내용 전체를 문자열로 리턴
f = open("/Users/hyewon/Desktop/딥러닝/파이썬/python-practice/04_함수/새파일.txt","r")
data = f.read()
print(data)
f.close()


# 새로운 내용 추가하기
f = open("/Users/hyewon/Desktop/딥러닝/파이썬/python-practice/04_함수/새파일.txt","a")
for i in range(11,20):
    data = "%d번째 줄입니다.\n" %i
    f.write(data)
f.close()


# with 문과 함께 사용하기
f = open("foo.txt",'w')
f.write("Life is too short, you need python")
f.close()

with open("foo.txt",'w') as f:
    f.write("Life is too short, you need python")