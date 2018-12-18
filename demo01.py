import math
import random


# 类型转换

n01 = 5.8
print(int(n01))  # 一个整数  5

n02 = 9
print(float(n02))  # 一个浮点数   9.0

n03 = 8
print(complex(n03))  # 一个复数 (8+0j)

n04 = 4
print(str(n04))  # 字符串 4

n05 = 5
print(repr(n05))  # 表达式字符串 5

n06 = 6
print(eval('n06 + 9'))  # 有个坑,要写成字符串格式    15

n07 = '7'
print(list(n07))  # 列表 ['7']

n08 = '8'
print(tuple(n08))  # 元组 ('8',)

##################

# 数学函数

print(abs(-6))  # 6    返回数字的绝对值，如abs(-10) 返回 10

print(math.ceil(4.1))  # 5  返回数字的上入整数，如math.ceil(4.1) 返回 5
print(math.ceil(-4.1))  # -4

print(math.floor(4.9))  # 4     	返回数字的下舍整数，如math.floor(4.9)返回 4
print(math.floor(-4.9))  # -5

print(max(12, 23, 34, 45, 89, 56, 67))  # 89 返回给定参数的最大值，参数可以为序列。

print(min(12, 23, 34, 45, 89, 56, 67))  # 12 返回给定参数的最小值，参数可以为序列。

print(
    math.modf(5.6)
)  # (0.5999999999999996, 5.0)      modf() 方法返回x的整数部分与小数部分，
# 两部分的数值符号与x相同，整数部分以浮点型表示

print(round(5.1234, 2))  # 5.12   返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。

print(math.sqrt(8))  # 2.8284271247461903 	返回数字x的平方根

#

# 随机数函数

print(random.choice([1, 2, 3, 5, 9]))  # 随机返回里面任何一个数

print(random.random())  # 0.16025643216140517     返回随机生成的一个实数，它在[0,1)范围内。

list = [20, 16, 10, 5]
# print(random.shuffle([1,2,3,4,5,6])) # 返回none
random.shuffle(list)
print(list)  # [10, 5, 20, 16]  直接修改原来对象 将序列的所有元素随机排序。

print(random.uniform(
    2, 9))  # 8.60313162562255  方法将随机生成下一个实数，它在 [x, y) 范围内。   大于等于2  小于9
