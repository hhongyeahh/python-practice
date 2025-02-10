test_list = ['one','two','three']
for i in test_list:
    print(i)

a = [(1,2),(3,4),(5,6)]
for(first,last) in a :
    print(first,last)

marks = [90,25,67,45,80]
number = 0
for mark in marks:
    number = number + 1
    if mark < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." % number)

# range
a = range(10) # 0,1,2,3,4,5,6,7,8,9
print(a)

a = range(1,11) # 1,2,3,4,5,6,7,8,9,10
print(a)

add = 0
for i in range(1,11):
    print("i:%d" %i)
    add = add + i
    print("add:%d" %add)
print("result add:%d" %add)

marks=[90,25,67,45,80]
for number in range(len(marks)):
    if marks[number] < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." %(number+1))

for i in range(2,10):
    for j in range(1,10):
        print(i*j, end=" ")
    print('')

# list comprehension
a = [1,2,3,4]
result = []
for num in a:
    result.append(num*3)
print(result)

a = [1,2,3,4]
result = [num*3 for num in a]
print(result)

a = [1,2,3,4]
result = [num*3 for num in a if num%2 == 0]
print(result)

result = [x*y for x in range(2,10)
          for y in range(1,10)]
print(result)
