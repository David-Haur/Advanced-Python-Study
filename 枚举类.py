# from enum import Enum, unique

# @unique # 检查枚举值是否重复，重复报错
# class Month(Enum):
#     JAN = 0
#     FEB = 2
#     MAR = 3

# Fruit = Enum('Fruit', ('apple', 'pear', 'banana'))


# print(list(Month))

from enum import Enum, unique

class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

# 测试:
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')
