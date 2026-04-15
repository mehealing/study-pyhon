# 函数

## 什么是函数？

函数是一段可重用的代码块，用于执行特定的任务。在Python中，使用`def`关键字定义函数。

## 函数的定义

```python
def function_name(parameters):
    """函数文档字符串"""
    # 函数体
    return value
```

- `def`：定义函数的关键字
- `function_name`：函数名，遵循变量命名规则
- `parameters`：函数参数，可选
- `"""函数文档字符串"""`：函数的文档字符串，用于描述函数的功能，可选
- `return value`：函数的返回值，可选

## 函数的调用

定义函数后，可以通过函数名调用函数：

```python
# 定义函数
def greet(name):
    """问候函数"""
    return f"Hello, {name}!"

# 调用函数
message = greet("张三")
print(message)  # 输出: Hello, 张三!
```

## 函数参数

### 位置参数

位置参数是最基本的参数类型，按照位置顺序传递。

```python
def add(a, b):
    """计算两个数的和"""
    return a + b

result = add(1, 2)  # a=1, b=2
print(result)  # 输出: 3
```

### 关键字参数

关键字参数通过参数名传递，可以不按照位置顺序。

```python
def describe_person(name, age):
    """描述一个人"""
    return f"{name} is {age} years old"

# 使用关键字参数
result = describe_person(age=30, name="张三")
print(result)  # 输出: 张三 is 30 years old
```

### 默认参数

默认参数在定义函数时指定默认值，调用时可以不传递该参数。

```python
def greet(name, greeting="Hello"):
    """问候函数"""
    return f"{greeting}, {name}!"

# 使用默认参数
result1 = greet("张三")  # 使用默认的greeting
print(result1)  # 输出: Hello, 张三!

# 覆盖默认参数
result2 = greet("张三", "Hi")
print(result2)  # 输出: Hi, 张三!
```

### 可变参数

#### *args - 可变位置参数

`*args`允许函数接收任意数量的位置参数，这些参数会被打包成一个元组。

```python
def sum_numbers(*args):
    """计算任意数量数字的和"""
    return sum(args)

result = sum_numbers(1, 2, 3, 4, 5)
print(result)  # 输出: 15
```

#### **kwargs - 可变关键字参数

`**kwargs`允许函数接收任意数量的关键字参数，这些参数会被打包成一个字典。

```python
def print_info(**kwargs):
    """打印任意关键字参数"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="张三", age=30, city="北京")
# 输出:
# name: 张三
# age: 30
# city: 北京
```

### 混合使用参数

可以混合使用不同类型的参数，但必须按照以下顺序：
1. 位置参数
2. `*args`
3. 默认参数
4. `**kwargs`

```python
def mixed_params(a, b, *args, c=10, **kwargs):
    """混合使用不同类型的参数"""
    print(f"a: {a}, b: {b}")
    print(f"args: {args}")
    print(f"c: {c}")
    print(f"kwargs: {kwargs}")

mixed_params(1, 2, 3, 4, 5, c=20, name="张三", age=30)
# 输出:
# a: 1, b: 2
# args: (3, 4, 5)
# c: 20
# kwargs: {'name': '张三', 'age': 30}
```

## 函数返回值

### 返回单个值

```python
def square(x):
    """计算平方"""
    return x ** 2

result = square(5)
print(result)  # 输出: 25
```

### 返回多个值

函数可以返回多个值，这些值会被打包成一个元组。

```python
def get_name_and_age():
    """返回姓名和年龄"""
    return "张三", 30

name, age = get_name_and_age()
print(f"姓名: {name}, 年龄: {age}")  # 输出: 姓名: 张三, 年龄: 30
```

### 无返回值

如果函数没有`return`语句，或者`return`语句没有返回值，则函数返回`None`。

```python
def print_hello():
    """打印Hello"""
    print("Hello")

result = print_hello()
print(result)  # 输出: None
```

## 函数文档字符串

函数文档字符串（docstring）用于描述函数的功能、参数和返回值。可以使用`help()`函数查看函数的文档字符串。

```python
def add(a, b):
    """计算两个数的和
    
    Args:
        a: 第一个数
        b: 第二个数
    
    Returns:
        两个数的和
    """
    return a + b

# 查看函数文档
help(add)
```

## 作用域

### 局部作用域

在函数内部定义的变量只在函数内部可见，称为局部变量。

```python
def test():
    x = 10  # 局部变量
    print(x)  # 输出: 10

test()
print(x)  # 错误: NameError: name 'x' is not defined
```

### 全局作用域

在函数外部定义的变量在整个程序中可见，称为全局变量。

```python
x = 10  # 全局变量

def test():
    print(x)  # 可以访问全局变量

test()  # 输出: 10
print(x)  # 输出: 10
```

### global关键字

在函数内部修改全局变量，需要使用`global`关键字。

```python
x = 10  # 全局变量

def test():
    global x  # 声明x是全局变量
    x = 20  # 修改全局变量
    print(x)  # 输出: 20

test()
print(x)  # 输出: 20
```

### nonlocal关键字

在嵌套函数中修改外层函数的变量，需要使用`nonlocal`关键字。

```python
def outer():
    x = 10  # 外层函数的变量
    
    def inner():
        nonlocal x  # 声明x是外层函数的变量
        x = 20  # 修改外层函数的变量
        print(x)  # 输出: 20
    
    inner()
    print(x)  # 输出: 20

outer()
```

## 嵌套函数

可以在一个函数内部定义另一个函数，称为嵌套函数。

```python
def outer():
    def inner():
        print("Inner function")
    
    inner()  # 调用嵌套函数

outer()  # 输出: Inner function
```

## 递归函数

递归函数是调用自身的函数。

```python
def factorial(n):
    """计算阶乘"""
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(5)
print(result)  # 输出: 120
```

## 匿名函数

匿名函数（lambda函数）是一种简短的、一次性的函数，使用`lambda`关键字定义。

```python
# 定义匿名函数
square = lambda x: x ** 2

# 调用匿名函数
result = square(5)
print(result)  # 输出: 25

# 在函数中使用匿名函数
def apply_function(func, x):
    return func(x)

result = apply_function(lambda x: x * 2, 10)
print(result)  # 输出: 20
```

## 高阶函数

高阶函数是接收函数作为参数或返回函数的函数。

```python
# 接收函数作为参数
def apply_function(func, x):
    return func(x)

result = apply_function(lambda x: x ** 2, 5)
print(result)  # 输出: 25

# 返回函数
def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))  # 输出: 10
print(triple(5))  # 输出: 15
```

## 练习

1. 编写一个函数，计算两个数的乘积。
2. 编写一个函数，判断一个数是否为质数。
3. 编写一个函数，计算斐波那契数列的第n项。
4. 编写一个高阶函数，接收一个函数和一个列表，返回该函数应用于列表中每个元素的结果。
5. 编写一个嵌套函数，计算一个数的平方和立方。

## 参考资料

- [Python官方文档 - 函数](https://docs.python.org/zh-cn/3/tutorial/controlflow.html#defining-functions)
- [Python教程 - 菜鸟教程](https://www.runoob.com/python/python-functions.html)