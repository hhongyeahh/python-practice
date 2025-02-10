money = 2000
if money >= 3000:
    print("택시를 타고 가라")
else:
        print("걸어가라")

# and, or, not
money = 2000
card = True
if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어가라")

# in, not in
print( 1 in [1,2,3])
print( 1 not in [1,2,3])
print('a' in ('a','b','c'))
print('j' not in 'python')

pocket = ['paper','cellphone','money']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어가라")

card = True
if 'pencil' in pocket:
    pass # 아무 행동도 하지 않도록
elif card:
    print("택시를 타고 가라")
else:
    print("카드를 꺼내라")

# 조건부 표현식
score = 70
message = "success" if score >= 60 else "failure"