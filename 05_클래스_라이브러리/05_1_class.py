class FourCal():
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def setData(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        result = self.a + self.b
        return result

    def sub(self):
        result = self.a - self.b
        return result

    def mul(self):
        result = self.a * self.b
        return result

    def div(self):
        result = self.a / self.b
        return result

# 상속
class MoreFourCal(FourCal):
    def pow(self):
        result = self.a ** self.b
        return result

a = MoreFourCal(4,2)
print(a.add(), a.mul(), a.sub(), a.div(), a.pow())


# 메서드 오버라이딩
class SafeFourCal(FourCal):
    def div(self):
        if self.b == 0:
            return 0;
        else:
            return self.a / self.b

a = SafeFourCal(4,0)
print(a.div())


# 클래스 변수
class Family:
    lastname = "김"

print(Family.lastname)
a = Family()
b = Family()
print(a.lastname, b.lastname)
a.lastname = "최"
print(a.lastname, b.lastname)
print(Family.lastname)




