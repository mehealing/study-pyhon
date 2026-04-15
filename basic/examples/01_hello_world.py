#!/usr/bin/env python3
"""
第一个Python程序
功能：打印Hello, World!和自定义消息
"""

# 打印Hello, World!
# print()函数用于将内容输出到控制台
print("Hello, World!")

# 打印自定义消息
# 使用变量存储名字
name = "Python"
# 使用f-string格式化字符串，将变量值插入到字符串中
print(f"Hello, {name}!")

# 打印多条消息
# 可以在print()函数中使用逗号分隔多个参数
print("Hello", "from", "Python")

# 打印空行
print()

# 打印带有特殊字符的消息
# 使用转义字符\n表示换行
print("Hello\nWorld")

# 打印带有引号的消息
# 使用单引号和双引号嵌套，或者使用转义字符\"
print('He said, "Hello!"')
print("He said, \"Hello!\"")

# 打印数字
# print()函数可以直接打印数字
print(42)
print(3.14)

# 打印表达式结果
# print()函数可以打印表达式的计算结果
print(1 + 2)
print("1 + 2 =", 1 + 2)