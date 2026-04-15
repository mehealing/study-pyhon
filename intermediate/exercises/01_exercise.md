# 练习1: 计算乘积

## 问题描述

编写一个函数，计算两个数的乘积。

## 输入输出示例

输入：
```
3, 5
```

输出：
```
15
```

## 提示

- 使用`def`关键字定义函数
- 函数接收两个参数
- 使用乘法运算符`*`计算乘积
- 使用`return`语句返回结果

## 参考解答

```python
def multiply(a, b):
    """计算两个数的乘积"""
    return a * b

# 测试函数
result = multiply(3, 5)
print(result)  # 输出: 15
```

# 练习2: 判断质数

## 问题描述

编写一个函数，判断一个数是否为质数。

## 输入输出示例

输入：
```
17
```

输出：
```
True
```

输入：
```
4
```

输出：
```
False
```

## 提示

- 质数是大于1的自然数，除了1和它本身之外没有其他因数
- 使用`def`关键字定义函数
- 函数接收一个参数
- 使用循环检查从2到该数的平方根之间的所有数
- 如果能被任何数整除，则不是质数
- 使用`return`语句返回布尔值

## 参考解答

```python
import math

def is_prime(n):
    """判断一个数是否为质数"""
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# 测试函数
print(is_prime(17))  # 输出: True
print(is_prime(4))   # 输出: False
```

# 练习3: 计算斐波那契数列

## 问题描述

编写一个函数，计算斐波那契数列的第n项。

## 输入输出示例

输入：
```
6
```

输出：
```
8
```

## 提示

- 斐波那契数列的前两项是0和1，之后的每一项都是前两项的和
- 可以使用递归或迭代的方法实现
- 使用`def`关键字定义函数
- 函数接收一个参数n
- 使用`return`语句返回第n项的值

## 参考解答

```python
# 递归方法
def fibonacci_recursive(n):
    """使用递归计算斐波那契数列的第n项"""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# 迭代方法
def fibonacci_iterative(n):
    """使用迭代计算斐波那契数列的第n项"""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b

# 测试函数
print(fibonacci_recursive(6))  # 输出: 8
print(fibonacci_iterative(6))  # 输出: 8
```

# 练习4: 高阶函数

## 问题描述

编写一个高阶函数，接收一个函数和一个列表，返回该函数应用于列表中每个元素的结果。

## 输入输出示例

输入：
```
lambda x: x ** 2, [1, 2, 3, 4, 5]
```

输出：
```
[1, 4, 9, 16, 25]
```

## 提示

- 高阶函数是接收函数作为参数的函数
- 使用`def`关键字定义函数
- 函数接收两个参数：一个函数和一个列表
- 使用列表推导式或循环将函数应用于列表中的每个元素
- 使用`return`语句返回结果列表

## 参考解答

```python
def apply_function_to_list(func, lst):
    """将函数应用于列表中的每个元素"""
    return [func(item) for item in lst]

# 测试函数
result = apply_function_to_list(lambda x: x ** 2, [1, 2, 3, 4, 5])
print(result)  # 输出: [1, 4, 9, 16, 25]
```

# 练习5: 嵌套函数

## 问题描述

编写一个嵌套函数，计算一个数的平方和立方。

## 输入输出示例

输入：
```
5
```

输出：
```
平方: 25, 立方: 125
```

## 提示

- 嵌套函数是在函数内部定义的函数
- 使用`def`关键字定义外层函数
- 在外层函数内部定义内层函数
- 外层函数返回内层函数的调用结果
- 使用`return`语句返回多个值

## 参考解答

```python
def calculate_power(n):
    """计算一个数的平方和立方"""
    def square(x):
        """计算平方"""
        return x ** 2
    
    def cube(x):
        """计算立方"""
        return x ** 3
    
    return square(n), cube(n)

# 测试函数
square_result, cube_result = calculate_power(5)
print(f"平方: {square_result}, 立方: {cube_result}")  # 输出: 平方: 25, 立方: 125
```

# 练习6: 函数文档字符串

## 问题描述

编写一个函数，计算两个数的商，并添加详细的文档字符串。

## 输入输出示例

输入：
```
10, 2
```

输出：
```
5.0
```

## 提示

- 使用`def`关键字定义函数
- 在函数定义后添加文档字符串，描述函数的功能、参数和返回值
- 处理除数为0的情况
- 使用`return`语句返回结果

## 参考解答

```python
def divide(a, b):
    """计算两个数的商
    
    Args:
        a: 被除数
        b: 除数
    
    Returns:
        两个数的商
    
    Raises:
        ZeroDivisionError: 如果除数为0
    """
    if b == 0:
        raise ZeroDivisionError("除数不能为0")
    return a / b

# 测试函数
print(divide(10, 2))  # 输出: 5.0
# print(divide(10, 0))  # 会引发ZeroDivisionError

# 查看函数文档
help(divide)
```