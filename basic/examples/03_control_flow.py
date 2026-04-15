#!/usr/bin/env python3
"""
控制流示例
功能：演示Python中的条件语句和循环结构
"""

# 条件语句
print("\n=== 条件语句 ===")

# 基本if语句
print("1. 基本if语句:")
age = 18
if age >= 18:
    print("成年人")

# if-else语句
print("\n2. if-else语句:")
age = 16
if age >= 18:
    print("成年人")
else:
    print("未成年人")

# if-elif-else语句
print("\n3. if-elif-else语句:")
score = 85
if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")

# 嵌套if语句
print("\n4. 嵌套if语句:")
a = 10
b = 5
if a > 0:
    if b > 0:
        print("a和b都是正数")
    else:
        print("a是正数，b不是正数")
else:
    print("a不是正数")

# 循环语句
print("\n=== 循环语句 ===")

# for循环遍历列表
print("1. for循环遍历列表:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# for循环遍历字符串
print("\n2. for循环遍历字符串:")
for char in "Hello":
    print(char)

# for循环使用range()函数
print("\n3. for循环使用range()函数:")
for i in range(5):
    print(i)

# for循环使用range()函数指定起始值和结束值
print("\n4. for循环使用range()函数指定起始值和结束值:")
for i in range(1, 6):
    print(i)

# for循环使用range()函数指定步长
print("\n5. for循环使用range()函数指定步长:")
for i in range(0, 10, 2):
    print(i)

# while循环
print("\n6. while循环:")
i = 0
while i < 5:
    print(i)
    i += 1

# 循环控制语句
print("\n=== 循环控制语句 ===")

# break语句
print("1. break语句:")
for i in range(10):
    if i == 5:
        break
    print(i)

# continue语句
print("\n2. continue语句:")
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

# pass语句
print("\n3. pass语句:")
for i in range(10):
    if i == 5:
        pass  # 暂时不做任何操作
    print(i)

# 循环嵌套
print("\n=== 循环嵌套 ===")

# 基本嵌套循环
print("1. 基本嵌套循环:")
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")

# 打印九九乘法表
print("\n2. 九九乘法表:")
for i in range(1, 10):
    for j in range(1, i+1):
        print(f"{j}×{i}={i*j}", end="\t")
    print()

# 列表推导式
print("\n=== 列表推导式 ===")

# 基本列表推导式
squares = [i**2 for i in range(10)]
print(f"1. 基本列表推导式: {squares}")

# 带有条件的列表推导式
evens = [i for i in range(10) if i % 2 == 0]
print(f"2. 带有条件的列表推导式: {evens}")

# 嵌套列表推导式
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(f"3. 嵌套列表推导式: {flattened}")

# 字典推导式
print("\n=== 字典推导式 ===")

# 基本字典推导式
squares_dict = {i: i**2 for i in range(5)}
print(f"1. 基本字典推导式: {squares_dict}")

# 带有条件的字典推导式
even_squares = {i: i**2 for i in range(10) if i % 2 == 0}
print(f"2. 带有条件的字典推导式: {even_squares}")

# 集合推导式
print("\n=== 集合推导式 ===")

# 基本集合推导式
squares_set = {i**2 for i in range(10)}
print(f"1. 基本集合推导式: {squares_set}")

# 带有条件的集合推导式
evens_set = {i for i in range(10) if i % 2 == 0}
print(f"2. 带有条件的集合推导式: {evens_set}")