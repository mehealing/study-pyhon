# 变量和数据类型

## 变量

### 什么是变量？

变量是用来存储数据的容器。在Python中，变量不需要声明类型，直接赋值即可。

### 变量的命名规则

1. 变量名只能包含字母、数字和下划线
2. 变量名不能以数字开头
3. 变量名区分大小写
4. 变量名不能是Python的关键字

### 变量的赋值

使用等号`=`进行变量赋值：

```python
# 赋值一个整数
age = 20

# 赋值一个字符串
name = "张三"

# 赋值一个浮点数
height = 1.75

# 赋值一个布尔值
is_student = True
```

### 多个变量赋值

可以同时为多个变量赋值：

```python
# 多个变量赋相同的值
a = b = c = 10

# 多个变量赋不同的值
x, y, z = 1, 2, 3
```

### 变量的使用

可以在表达式中使用变量：

```python
# 计算两个变量的和
a = 10
b = 20
sum = a + b
print(sum)  # 输出: 30
```

## 数据类型

Python支持多种数据类型，主要包括：

### 数值类型

#### 整数 (int)

整数是没有小数部分的数字，可以是正数、负数或零。

```python
# 整数
x = 10
y = -5
z = 0
```

#### 浮点数 (float)

浮点数是带有小数部分的数字。

```python
# 浮点数
x = 3.14
y = -2.5
z = 0.0
```

#### 复数 (complex)

复数由实部和虚部组成，虚部以`j`或`J`结尾。

```python
# 复数
x = 1 + 2j
y = 3j
z = -2 + 4j
```

### 字符串 (str)

字符串是由字符组成的序列，使用单引号、双引号或三引号表示。

```python
# 单引号字符串
name = '张三'

# 双引号字符串
message = "Hello, World!"

# 三引号字符串（可以换行）
description = '''这是一个
多行字符串'''  # 或者使用"""
```

### 布尔值 (bool)

布尔值只有两个值：`True`和`False`。

```python
# 布尔值
is_true = True
is_false = False
```

### 列表 (list)

列表是有序的可变序列，可以包含不同类型的元素。

```python
# 列表
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "apple", True, 3.14]
```

### 元组 (tuple)

元组是有序的不可变序列，可以包含不同类型的元素。

```python
# 元组
fruits = ("apple", "banana", "cherry")
numbers = (1, 2, 3, 4, 5)
```

### 字典 (dict)

字典是无序的键值对集合，键必须是唯一的。

```python
# 字典
person = {"name": "张三", "age": 20, "city": "北京"}
```

### 集合 (set)

集合是无序的唯一元素集合。

```python
# 集合
fruits = {"apple", "banana", "cherry"}
numbers = {1, 2, 3, 4, 5}
```

### 空值 (None)

`None`表示空值，是一个特殊的常量。

```python
# 空值
x = None
```

## 类型转换

### 隐式类型转换

Python会自动进行一些类型转换：

```python
# 整数和浮点数相加，结果为浮点数
x = 10  # 整数
y = 3.14  # 浮点数
z = x + y  # 结果为13.14，浮点数
print(type(z))  # 输出: <class 'float'>
```

### 显式类型转换

可以使用内置函数进行类型转换：

```python
# 转换为整数
x = int(3.14)  # 结果为3
y = int("10")  # 结果为10

# 转换为浮点数
x = float(10)  # 结果为10.0
y = float("3.14")  # 结果为3.14

# 转换为字符串
x = str(10)  # 结果为"10"
y = str(3.14)  # 结果为"3.14"

# 转换为列表
x = list("hello")  # 结果为["h", "e", "l", "l", "o"]
y = list((1, 2, 3))  # 结果为[1, 2, 3]

# 转换为元组
x = tuple([1, 2, 3])  # 结果为(1, 2, 3)
y = tuple("hello")  # 结果为("h", "e", "l", "l", "o")

# 转换为集合
x = set([1, 2, 3, 3])  # 结果为{1, 2, 3}
y = set("hello")  # 结果为{'h', 'e', 'l', 'o'}

# 转换为字典
x = dict([("name", "张三"), ("age", 20)])  # 结果为{"name": "张三", "age": 20}
```

## 类型检查

使用`type()`函数可以检查变量的类型：

```python
x = 10
print(type(x))  # 输出: <class 'int'>

y = "hello"
print(type(y))  # 输出: <class 'str'>

z = [1, 2, 3]
print(type(z))  # 输出: <class 'list'>
```

使用`isinstance()`函数可以检查变量是否为指定类型：

```python
x = 10
print(isinstance(x, int))  # 输出: True
print(isinstance(x, float))  # 输出: False

y = [1, 2, 3]
print(isinstance(y, list))  # 输出: True
print(isinstance(y, (list, tuple)))  # 输出: True（检查是否为列表或元组）
```

## 练习

1. 定义一个变量存储你的姓名，另一个变量存储你的年龄，然后打印出"我的名字是XXX，今年XX岁"。
2. 定义一个列表，包含5个不同的水果名称，然后打印出列表的长度。
3. 定义一个字典，包含你的姓名、年龄和所在城市，然后打印出字典的所有键和值。

## 参考资料

- [Python官方文档 - 数据类型](https://docs.python.org/zh-cn/3/library/stdtypes.html)
- [Python教程 - 菜鸟教程](https://www.runoob.com/python/python-variable-types.html)