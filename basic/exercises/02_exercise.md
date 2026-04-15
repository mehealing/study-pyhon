# 练习1: 打印个人信息

## 问题描述

定义一个变量存储你的姓名，另一个变量存储你的年龄，然后打印出"我的名字是XXX，今年XX岁"。

## 输入输出示例

输入：无

输出：
```
我的名字是张三，今年20岁
```

## 提示

- 使用变量存储姓名和年龄
- 使用f-string格式化字符串
- 使用print()函数打印结果

## 参考解答

```python
# 定义变量
name = "张三"
age = 20

# 打印个人信息
print(f"我的名字是{name}，今年{age}岁")
```

# 练习2: 列表操作

## 问题描述

定义一个列表，包含5个不同的水果名称，然后打印出列表的长度。

## 输入输出示例

输入：无

输出：
```
水果列表: ['apple', 'banana', 'cherry', 'orange', 'grape']
列表长度: 5
```

## 提示

- 使用方括号创建列表
- 使用len()函数获取列表长度
- 使用print()函数打印结果

## 参考解答

```python
# 定义水果列表
fruits = ["apple", "banana", "cherry", "orange", "grape"]

# 打印列表和长度
print(f"水果列表: {fruits}")
print(f"列表长度: {len(fruits)}")
```

# 练习3: 字典操作

## 问题描述

定义一个字典，包含你的姓名、年龄和所在城市，然后打印出字典的所有键和值。

## 输入输出示例

输入：无

输出：
```
个人信息: {'name': '张三', 'age': 20, 'city': '北京'}
字典键: ['name', 'age', 'city']
字典值: ['张三', 20, '北京']
```

## 提示

- 使用花括号创建字典，键值对用冒号分隔
- 使用keys()方法获取字典的键
- 使用values()方法获取字典的值
- 使用list()函数将结果转换为列表以便打印

## 参考解答

```python
# 定义个人信息字典
person = {"name": "张三", "age": 20, "city": "北京"}

# 打印字典、键和值
print(f"个人信息: {person}")
print(f"字典键: {list(person.keys())}")
print(f"字典值: {list(person.values())}")
```

# 练习4: 类型转换

## 问题描述

将字符串"123"转换为整数，将整数456转换为字符串，然后打印出转换后的值和类型。

## 输入输出示例

输入：无

输出：
```
字符串转整数: 123, 类型: <class 'int'>
整数转字符串: 456, 类型: <class 'str'>
```

## 提示

- 使用int()函数将字符串转换为整数
- 使用str()函数将整数转换为字符串
- 使用type()函数检查类型
- 使用print()函数打印结果

## 参考解答

```python
# 字符串转整数
str_num = "123"
int_num = int(str_num)
print(f"字符串转整数: {int_num}, 类型: {type(int_num)}")

# 整数转字符串
int_value = 456
str_value = str(int_value)
print(f"整数转字符串: {str_value}, 类型: {type(str_value)}")
```

# 练习5: 混合数据类型

## 问题描述

创建一个列表，包含整数、字符串、浮点数和布尔值，然后打印出列表的内容和每个元素的类型。

## 输入输出示例

输入：无

输出：
```
混合列表: [10, 'hello', 3.14, True]
元素类型:
10: <class 'int'>
hello: <class 'str'>
3.14: <class 'float'>
True: <class 'bool'>
```

## 提示

- 创建包含不同类型元素的列表
- 使用for循环遍历列表
- 使用type()函数检查每个元素的类型
- 使用print()函数打印结果

## 参考解答

```python
# 创建混合列表
mixed_list = [10, "hello", 3.14, True]

# 打印列表
print(f"混合列表: {mixed_list}")
print("元素类型:")

# 遍历列表并打印每个元素的类型
for item in mixed_list:
    print(f"{item}: {type(item)}")
```