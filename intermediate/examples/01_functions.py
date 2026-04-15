#!/usr/bin/env python3
"""
函数示例
功能：演示Python中的函数定义和使用
"""

# 基本函数定义和调用
print("\n=== 基本函数定义和调用 ===")

def greet(name):
    """问候函数"""
    return f"Hello, {name}!"

# 调用函数
message = greet("张三")
print(f"函数调用结果: {message}")

# 函数参数
print("\n=== 函数参数 ===")

# 位置参数
def add(a, b):
    """计算两个数的和"""
    return a + b

result = add(1, 2)
print(f"位置参数: add(1, 2) = {result}")

# 关键字参数
def describe_person(name, age):
    """描述一个人"""
    return f"{name} is {age} years old"

result = describe_person(age=30, name="张三")
print(f"关键字参数: describe_person(age=30, name='张三') = {result}")

# 默认参数
def greet_with_default(name, greeting="Hello"):
    """带有默认参数的问候函数"""
    return f"{greeting}, {name}!"

result1 = greet_with_default("张三")
result2 = greet_with_default("张三", "Hi")
print(f"默认参数: greet_with_default('张三') = {result1}")
print(f"覆盖默认参数: greet_with_default('张三', 'Hi') = {result2}")

# 可变参数
print("\n=== 可变参数 ===")

# *args - 可变位置参数
def sum_numbers(*args):
    """计算任意数量数字的和"""
    return sum(args)

result = sum_numbers(1, 2, 3, 4, 5)
print(f"可变位置参数: sum_numbers(1, 2, 3, 4, 5) = {result}")

# **kwargs - 可变关键字参数
def print_info(**kwargs):
    """打印任意关键字参数"""
    print("可变关键字参数:")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

print_info(name="张三", age=30, city="北京")

# 混合使用参数
print("\n=== 混合使用参数 ===")

def mixed_params(a, b, *args, c=10, **kwargs):
    """混合使用不同类型的参数"""
    print(f"位置参数: a={a}, b={b}")
    print(f"可变位置参数: args={args}")
    print(f"默认参数: c={c}")
    print(f"可变关键字参数: kwargs={kwargs}")

mixed_params(1, 2, 3, 4, 5, c=20, name="张三", age=30)

# 函数返回值
print("\n=== 函数返回值 ===")

# 返回单个值
def square(x):
    """计算平方"""
    return x ** 2

result = square(5)
print(f"返回单个值: square(5) = {result}")

# 返回多个值
def get_name_and_age():
    """返回姓名和年龄"""
    return "张三", 30

name, age = get_name_and_age()
print(f"返回多个值: get_name_and_age() = 姓名: {name}, 年龄: {age}")

# 无返回值
def print_hello():
    """打印Hello"""
    print("Hello")

result = print_hello()
print(f"无返回值: print_hello() = {result}")

# 函数文档字符串
print("\n=== 函数文档字符串 ===")

def add_with_doc(a, b):
    """计算两个数的和
    
    Args:
        a: 第一个数
        b: 第二个数
    
    Returns:
        两个数的和
    """
    return a + b

# 查看函数文档
print("函数文档:")
help(add_with_doc)

# 作用域
print("\n=== 作用域 ===")

# 局部作用域
print("局部作用域:")
def test_local():
    x = 10  # 局部变量
    print(f"  函数内部: x = {x}")

test_local()
# print(f"  函数外部: x = {x}")  # 错误: NameError: name 'x' is not defined

# 全局作用域
print("\n全局作用域:")
global_x = 10  # 全局变量

def test_global():
    print(f"  函数内部访问全局变量: global_x = {global_x}")

test_global()
print(f"  函数外部: global_x = {global_x}")

# global关键字
print("\nglobal关键字:")
global_y = 10  # 全局变量

def test_global_modify():
    global global_y  # 声明global_y是全局变量
    global_y = 20  # 修改全局变量
    print(f"  函数内部修改全局变量: global_y = {global_y}")

test_global_modify()
print(f"  函数外部: global_y = {global_y}")

# nonlocal关键字
print("\nnonlocal关键字:")
def outer():
    x = 10  # 外层函数的变量
    
    def inner():
        nonlocal x  # 声明x是外层函数的变量
        x = 20  # 修改外层函数的变量
        print(f"  内层函数: x = {x}")
    
    inner()
    print(f"  外层函数: x = {x}")

outer()

# 嵌套函数
print("\n=== 嵌套函数 ===")

def outer_function():
    print("  外层函数开始")
    
    def inner_function():
        print("  内层函数执行")
    
    inner_function()  # 调用嵌套函数
    print("  外层函数结束")

outer_function()

# 递归函数
print("\n=== 递归函数 ===")

def factorial(n):
    """计算阶乘"""
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(5)
print(f"递归函数: factorial(5) = {result}")

# 匿名函数
print("\n=== 匿名函数 ===")

# 定义匿名函数
square = lambda x: x ** 2

# 调用匿名函数
result = square(5)
print(f"匿名函数: square(5) = {result}")

# 在函数中使用匿名函数
def apply_function(func, x):
    return func(x)

result = apply_function(lambda x: x * 2, 10)
print(f"在函数中使用匿名函数: apply_function(lambda x: x * 2, 10) = {result}")

# 高阶函数
print("\n=== 高阶函数 ===")

# 接收函数作为参数
def apply_function(func, x):
    return func(x)

result = apply_function(lambda x: x ** 2, 5)
print(f"接收函数作为参数: apply_function(lambda x: x ** 2, 5) = {result}")

# 返回函数
def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)

print(f"返回函数 - double(5) = {double(5)}")
print(f"返回函数 - triple(5) = {triple(5)}")