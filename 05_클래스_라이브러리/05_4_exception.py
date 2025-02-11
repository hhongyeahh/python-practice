try:
    a=[1,2]
    print(a[3])
    4 / 0
except (ZeroDivisionError, IndexError) as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
except IndexError:
    print("인덱싱할 수 없습니다.")
else:
    print("오류가 없을 경우에만 실행되는 else")
finally:
    print("예외와 관계없이 실행되는 finally")


# 오류 회피
try:
    f = open("없는파일","r")
except FileNotFoundError:
    pass # 오류가 발생해도 회피 통과


# 오류 강제 발생
class Bird:
    def fly(self):
        raise NotImplementedError # 상속받는 자식 클래스가 반드시 해당 함수를 구현하도록 강제하고 싶은 경우

class Eagle(Bird):
    pass
eagle = Eagle()
eagle.fly() # fly 함수를 구현하지 않았기 때문에 오류 발생

class Eagle2(Bird):
    def fly(self):
        print("very fast")
eagle2 = Eagle2()
eagle2.fly() # fly 함수를 구현하였기 때문에 정상


# 예외 만들기
class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별명입니다."

def say_nick(nick):
    if nick == "바보":
        raise MyError()
    print(nick)

try:
    say_nick("천사")
    say_nick("바보") # 오류 발생
except MyError:
    print("허용되지 않는 별명입니다.")
except MyError as e:
    print(e)