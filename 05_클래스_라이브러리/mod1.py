def add(a, b):
    return a + b


def sub(a, b):
    return a - b


if __name__ == '__main__': # 외부에서 import 해서 수행할 때는 출력이 안되도록
    print(add(1, 2))
    print(sub(1, 4))
