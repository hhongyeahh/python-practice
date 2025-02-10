prompt = """
1. Add
2. Del
3. List
4. Quit

Enter number: """

number = 0
while number != 4:
    print(prompt)
    number = int(input())


# break
coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee - 1
    print("남은 커피의 양은 %d개입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break


# continue
a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0: continue
    print(a)


# 무한루프
# while True:
#      print("Ctrl+C를 눌러야 while 문을 빠져나갈 수 있습니다.")

