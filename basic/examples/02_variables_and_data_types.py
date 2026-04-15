#!/usr/bin/env python3
"""
变量和数据类型示例
功能：演示Python中的变量定义和各种数据类型
"""

# 变量定义和赋值
# 整数
age = 20
print(f"年龄: {age}, 类型: {type(age)}")

# 浮点数
height = 1.75
print(f"身高: {height}, 类型: {type(height)}")

# 字符串
name = "张三"
print(f"姓名: {name}, 类型: {type(name)}")

# 布尔值
is_student = True
print(f"是否是学生: {is_student}, 类型: {type(is_student)}")

# 多个变量赋值
# 多个变量赋相同的值
a = b = c = 10
print(f"a: {a}, b: {b}, c: {c}")

# 多个变量赋不同的值
x, y, z = 1, 2, 3
print(f"x: {x}, y: {y}, z: {z}")

# 数值类型
print("\n=== 数值类型 ===")

# 整数
int_num = 100
print(f"整数: {int_num}, 类型: {type(int_num)}")

# 浮点数
float_num = 3.14159
print(f"浮点数: {float_num}, 类型: {type(float_num)}")

# 复数
complex_num = 1 + 2j
print(f"复数: {complex_num}, 类型: {type(complex_num)}")

# 字符串
print("\n=== 字符串 ===")

# 单引号字符串
single_quote = 'Hello'
print(f"单引号字符串: {single_quote}")

# 双引号字符串
double_quote = "World"
print(f"双引号字符串: {double_quote}")

# 三引号字符串（多行）
multi_line = '''这是一个
多行字符串'''
print(f"多行字符串: {multi_line}")

# 字符串拼接
full_name = "张" + "三"
print(f"字符串拼接: {full_name}")

# 字符串重复
repeated = "Hello" * 3
print(f"字符串重复: {repeated}")

# 布尔值
print("\n=== 布尔值 ===")

# 布尔值运算
print(f"True and False: {True and False}")
print(f"True or False: {True or False}")
print(f"not True: {not True}")

# 列表
print("\n=== 列表 ===")

# 创建列表
fruits = ["apple", "banana", "cherry"]
print(f"列表: {fruits}")

# 访问列表元素
print(f"第一个元素: {fruits[0]}")
print(f"最后一个元素: {fruits[-1]}")

# 修改列表元素
fruits[1] = "orange"
print(f"修改后的列表: {fruits}")

# 添加元素
fruits.append("grape")
print(f"添加元素后的列表: {fruits}")

# 列表长度
print(f"列表长度: {len(fruits)}")

# 元组
print("\n=== 元组 ===")

# 创建元组
colors = ("red", "green", "blue")
print(f"元组: {colors}")

# 访问元组元素
print(f"第一个元素: {colors[0]}")

# 元组长度
print(f"元组长度: {len(colors)}")

# 字典
print("\n=== 字典 ===")

# 创建字典
person = {"name": "张三", "age": 20, "city": "北京"}
print(f"字典: {person}")

# 访问字典值
print(f"姓名: {person['name']}")
print(f"年龄: {person.get('age')}")

# 修改字典值
person["age"] = 21
print(f"修改后的字典: {person}")

# 添加键值对
person["job"] = "学生"
print(f"添加键值对后的字典: {person}")

# 字典键
print(f"字典键: {list(person.keys())}")

# 字典值
print(f"字典值: {list(person.values())}")

# 集合
print("\n=== 集合 ===")

# 创建集合
numbers = {1, 2, 3, 4, 5, 3, 2}  # 重复元素会被自动去重
print(f"集合: {numbers}")

# 添加元素
numbers.add(6)
print(f"添加元素后的集合: {numbers}")

# 移除元素
numbers.remove(3)
print(f"移除元素后的集合: {numbers}")

# 空值
print("\n=== 空值 ===")

# 空值
empty = None
print(f"空值: {empty}, 类型: {type(empty)}")

# 类型转换
print("\n=== 类型转换 ===")

# 整数转浮点数
int_to_float = float(10)
print(f"整数转浮点数: {int_to_float}, 类型: {type(int_to_float)}")

# 浮点数转整数
float_to_int = int(3.999)
print(f"浮点数转整数: {float_to_int}, 类型: {type(float_to_int)}")

# 整数转字符串
int_to_str = str(42)
print(f"整数转字符串: {int_to_str}, 类型: {type(int_to_str)}")

# 字符串转整数
str_to_int = int("123")
print(f"字符串转整数: {str_to_int}, 类型: {type(str_to_int)}")

# 列表转元组
list_to_tuple = tuple([1, 2, 3])
print(f"列表转元组: {list_to_tuple}, 类型: {type(list_to_tuple)}")

# 元组转列表
tuple_to_list = list((4, 5, 6))
print(f"元组转列表: {tuple_to_list}, 类型: {type(tuple_to_list)}")

# 类型检查
print("\n=== 类型检查 ===")

# 使用type()函数
num = 10
print(f"num的类型: {type(num)}")

# 使用isinstance()函数
print(f"num是否是整数: {isinstance(num, int)}")
print(f"num是否是浮点数: {isinstance(num, float)}")

# 检查是否为多个类型之一
print(f"num是否是整数或浮点数: {isinstance(num, (int, float))}")