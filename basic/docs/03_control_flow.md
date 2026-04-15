# 控制流

## 条件语句

### if语句

`if`语句用于根据条件执行不同的代码块。

```python
# 基本if语句
age = 18
if age >= 18:
    print("成年人")
```

### if-else语句

`if-else`语句用于在条件为真时执行一个代码块，否则执行另一个代码块。

```python
# if-else语句
age = 16
if age >= 18:
    print("成年人")
else:
    print("未成年人")
```

### if-elif-else语句

`if-elif-else`语句用于检查多个条件。

```python
# if-elif-else语句
score = 85
if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")
```

### 嵌套if语句

可以在`if`语句内部嵌套另一个`if`语句。

```python
# 嵌套if语句
a = 10
b = 5
if a > 0:
    if b > 0:
        print("a和b都是正数")
    else:
        print("a是正数，b不是正数")
else:
    print("a不是正数")
```

## 循环语句

### for循环

`for`循环用于遍历序列（如列表、元组、字符串）中的元素。

```python
# 遍历列表
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 遍历字符串
for char in "Hello":
    print(char)

# 使用range()函数
for i in range(5):
    print(i)

# 使用range()函数指定起始值和结束值
for i in range(1, 6):
    print(i)

# 使用range()函数指定步长
for i in range(0, 10, 2):
    print(i)
```

### while循环

`while`循环用于在条件为真时重复执行代码块。

```python
# 基本while循环
i = 0
while i < 5:
    print(i)
    i += 1

# 带有条件判断的while循环
password = ""
while password != "123456":
    password = input("请输入密码: ")
print("密码正确！")
```

### 循环控制语句

#### break语句

`break`语句用于跳出当前循环。

```python
# 使用break语句
for i in range(10):
    if i == 5:
        break
    print(i)
```

#### continue语句

`continue`语句用于跳过当前循环的剩余部分，继续下一次循环。

```python
# 使用continue语句
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
```

#### pass语句

`pass`语句是一个空语句，用于占位。

```python
# 使用pass语句
for i in range(10):
    if i == 5:
        pass  # 暂时不做任何操作
    print(i)
```

## 循环嵌套

可以在一个循环内部嵌套另一个循环。

```python
# 嵌套循环
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")

# 打印九九乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        print(f"{j}×{i}={i*j}", end="\t")
    print()
```

## 列表推导式

列表推导式是一种简洁的创建列表的方法。

```python
# 基本列表推导式
squares = [i**2 for i in range(10)]
print(squares)  # 输出: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 带有条件的列表推导式
evens = [i for i in range(10) if i % 2 == 0]
print(evens)  # 输出: [0, 2, 4, 6, 8]

# 嵌套列表推导式
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(flattened)  # 输出: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## 字典推导式

字典推导式是一种简洁的创建字典的方法。

```python
# 基本字典推导式
squares = {i: i**2 for i in range(5)}
print(squares)  # 输出: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# 带有条件的字典推导式
even_squares = {i: i**2 for i in range(10) if i % 2 == 0}
print(even_squares)  # 输出: {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
```

## 集合推导式

集合推导式是一种简洁的创建集合的方法。

```python
# 基本集合推导式
squares = {i**2 for i in range(10)}
print(squares)  # 输出: {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}

# 带有条件的集合推导式
evens = {i for i in range(10) if i % 2 == 0}
print(evens)  # 输出: {0, 2, 4, 6, 8}
```

## 练习

1. 编写一个程序，根据用户输入的分数，输出对应的等级（优秀、良好、及格、不及格）。
2. 编写一个程序，使用for循环打印1到100之间的所有偶数。
3. 编写一个程序，使用while循环计算1到100的和。
4. 编写一个程序，打印九九乘法表。
5. 使用列表推导式创建一个包含1到100之间所有奇数的列表。

## 参考资料

- [Python官方文档 - 控制流](https://docs.python.org/zh-cn/3/tutorial/controlflow.html)
- [Python教程 - 菜鸟教程](https://www.runoob.com/python/python-if-statement.html)