# 练习1: 学生类

## 问题描述

编写一个`Student`类，包含姓名、年龄、学号等属性，以及学习、考试等方法。

## 输入输出示例

输入：
```python
student = Student("张三", 18, "2023001")
print(student)
student.study("Python")
student.exam("数学", 95)
```

输出：
```
Student(name='张三', age=18, student_id='2023001')
张三正在学习Python
张三数学考试得分：95
```

## 提示

- 使用`class`关键字定义类
- 在`__init__`方法中初始化属性
- 定义`study`和`exam`方法
- 定义`__str__`方法以友好的方式显示对象信息

## 参考解答

```python
class Student:
    """学生类"""
    def __init__(self, name, age, student_id):
        """初始化学生信息"""
        self.name = name
        self.age = age
        self.student_id = student_id
    
    def study(self, subject):
        """学习方法"""
        print(f"{self.name}正在学习{subject}")
    
    def exam(self, subject, score):
        """考试方法"""
        print(f"{self.name}{subject}考试得分：{score}")
    
    def __str__(self):
        """字符串表示"""
        return f"Student(name='{self.name}', age={self.age}, student_id='{self.student_id}')"

# 测试
student = Student("张三", 18, "2023001")
print(student)
student.study("Python")
student.exam("数学", 95)
```

# 练习2: 圆形类

## 问题描述

编写一个`Circle`类，继承自`Shape`抽象基类，实现面积和周长的计算。

## 输入输出示例

输入：
```python
circle = Circle(5)
print(f"半径: {circle.radius}")
print(f"面积: {circle.area():.2f}")
print(f"周长: {circle.perimeter():.2f}")
```

输出：
```
半径: 5
面积: 78.54
周长: 31.42
```

## 提示

- 从`abc`模块导入`ABC`和`abstractmethod`
- 定义`Shape`抽象基类，包含`area`和`perimeter`抽象方法
- 定义`Circle`类，继承自`Shape`
- 在`Circle`类中实现`area`和`perimeter`方法
- 使用`math`模块计算圆的面积和周长

## 参考解答

```python
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """形状抽象基类"""
    @abstractmethod
    def area(self):
        """计算面积"""
        pass
    
    @abstractmethod
    def perimeter(self):
        """计算周长"""
        pass

class Circle(Shape):
    """圆形类"""
    def __init__(self, radius):
        """初始化圆形"""
        self.radius = radius
    
    def area(self):
        """计算面积"""
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        """计算周长"""
        return 2 * math.pi * self.radius

# 测试
circle = Circle(5)
print(f"半径: {circle.radius}")
print(f"面积: {circle.area():.2f}")
print(f"周长: {circle.perimeter():.2f}")
```

# 练习3: 银行账户类

## 问题描述

编写一个`BankAccount`类，包含余额属性，以及存款、取款、查询余额等方法。

## 输入输出示例

输入：
```python
account = BankAccount("张三", 1000)
print(account.get_balance())
account.deposit(500)
print(account.get_balance())
account.withdraw(300)
print(account.get_balance())
```

输出：
```
张三的账户余额: 1000
存款成功，存入500
张三的账户余额: 1500
取款成功，取出300
张三的账户余额: 1200
```

## 提示

- 定义`BankAccount`类，包含姓名和余额属性
- 定义`get_balance`方法查询余额
- 定义`deposit`方法存款
- 定义`withdraw`方法取款，注意检查余额是否足够

## 参考解答

```python
class BankAccount:
    """银行账户类"""
    def __init__(self, name, balance=0):
        """初始化账户"""
        self.name = name
        self._balance = balance  # 保护属性
    
    def get_balance(self):
        """查询余额"""
        return f"{self.name}的账户余额: {self._balance}"
    
    def deposit(self, amount):
        """存款"""
        if amount > 0:
            self._balance += amount
            print(f"存款成功，存入{amount}")
        else:
            print("存款金额必须大于0")
    
    def withdraw(self, amount):
        """取款"""
        if amount > 0:
            if amount <= self._balance:
                self._balance -= amount
                print(f"取款成功，取出{amount}")
            else:
                print("余额不足")
        else:
            print("取款金额必须大于0")

# 测试
account = BankAccount("张三", 1000)
print(account.get_balance())
account.deposit(500)
print(account.get_balance())
account.withdraw(300)
print(account.get_balance())
```

# 练习4: 员工类

## 问题描述

编写一个`Employee`类，包含姓名、工号、工资等属性，以及计算奖金、打印信息等方法。

## 输入输出示例

输入：
```python
employee = Employee("李四", "E001", 8000)
employee.print_info()
bonus = employee.calculate_bonus(0.1)
print(f"奖金: {bonus}")
```

输出：
```
姓名: 李四
工号: E001
工资: 8000
奖金: 800.0
```

## 提示

- 定义`Employee`类，包含姓名、工号和工资属性
- 定义`print_info`方法打印员工信息
- 定义`calculate_bonus`方法计算奖金，参数为奖金比例

## 参考解答

```python
class Employee:
    """员工类"""
    def __init__(self, name, emp_id, salary):
        """初始化员工信息"""
        self.name = name
        self.emp_id = emp_id
        self.salary = salary
    
    def print_info(self):
        """打印员工信息"""
        print(f"姓名: {self.name}")
        print(f"工号: {self.emp_id}")
        print(f"工资: {self.salary}")
    
    def calculate_bonus(self, rate):
        """计算奖金"""
        return self.salary * rate

# 测试
employee = Employee("李四", "E001", 8000)
employee.print_info()
bonus = employee.calculate_bonus(0.1)
print(f"奖金: {bonus}")
```

# 练习5: 图书馆类

## 问题描述

编写一个`Library`类，包含书籍列表，以及添加书籍、删除书籍、查找书籍等方法。

## 输入输出示例

输入：
```python
library = Library()
library.add_book("Python编程", "张三")
library.add_book("Java编程", "李四")
library.add_book("C++编程", "王五")
print("所有书籍:")
library.list_books()
print("\n查找Python编程:")
book = library.find_book("Python编程")
if book:
    print(f"找到书籍: {book['title']} - {book['author']}")
print("\n删除Java编程:")
library.remove_book("Java编程")
print("\n所有书籍:")
library.list_books()
```

输出：
```
所有书籍:
1. Python编程 - 张三
2. Java编程 - 李四
3. C++编程 - 王五

查找Python编程:
找到书籍: Python编程 - 张三

删除Java编程:

所有书籍:
1. Python编程 - 张三
2. C++编程 - 王五
```

## 提示

- 定义`Library`类，包含书籍列表属性
- 定义`add_book`方法添加书籍
- 定义`remove_book`方法删除书籍
- 定义`find_book`方法查找书籍
- 定义`list_books`方法列出所有书籍

## 参考解答

```python
class Library:
    """图书馆类"""
    def __init__(self):
        """初始化图书馆"""
        self.books = []
    
    def add_book(self, title, author):
        """添加书籍"""
        book = {"title": title, "author": author}
        self.books.append(book)
        print(f"添加书籍成功: {title} - {author}")
    
    def remove_book(self, title):
        """删除书籍"""
        for book in self.books:
            if book["title"] == title:
                self.books.remove(book)
                print(f"删除书籍成功: {title}")
                return
        print(f"未找到书籍: {title}")
    
    def find_book(self, title):
        """查找书籍"""
        for book in self.books:
            if book["title"] == title:
                return book
        return None
    
    def list_books(self):
        """列出所有书籍"""
        if not self.books:
            print("图书馆为空")
            return
        for i, book in enumerate(self.books, 1):
            print(f"{i}. {book['title']} - {book['author']}")

# 测试
library = Library()
library.add_book("Python编程", "张三")
library.add_book("Java编程", "李四")
library.add_book("C++编程", "王五")
print("所有书籍:")
library.list_books()
print("\n查找Python编程:")
book = library.find_book("Python编程")
if book:
    print(f"找到书籍: {book['title']} - {book['author']}")
print("\n删除Java编程:")
library.remove_book("Java编程")
print("\n所有书籍:")
library.list_books()
```

# 练习6: 继承与多态

## 问题描述

编写一个`Vehicle`基类，以及`Car`和`Bicycle`子类，演示继承和多态。

## 输入输出示例

输入：
```python
car = Car("特斯拉", "Model 3", 4)
bicycle = Bicycle("捷安特", "ATX777", 2)

print(car)
car.drive()

print(bicycle)
bicycle.drive()

# 多态
vehicles = [car, bicycle]
for vehicle in vehicles:
    vehicle.drive()
```

输出：
```
Car(brand='特斯拉', model='Model 3', wheels=4)
特斯拉 Model 3 正在行驶
Bicycle(brand='捷安特', model='ATX777', wheels=2)
捷安特 ATX777 正在骑行
特斯拉 Model 3 正在行驶
捷安特 ATX777 正在骑行
```

## 提示

- 定义`Vehicle`基类，包含品牌、型号等属性
- 定义`Car`和`Bicycle`子类，继承自`Vehicle`
- 在子类中重写`drive`方法
- 演示多态，使用统一的接口调用不同子类的方法

## 参考解答

```python
class Vehicle:
    """交通工具基类"""
    def __init__(self, brand, model):
        """初始化交通工具"""
        self.brand = brand
        self.model = model
    
    def drive(self):
        """行驶方法"""
        print(f"{self.brand} {self.model} 正在行驶")

class Car(Vehicle):
    """汽车类"""
    def __init__(self, brand, model, wheels):
        """初始化汽车"""
        super().__init__(brand, model)
        self.wheels = wheels
    
    def drive(self):
        """重写行驶方法"""
        print(f"{self.brand} {self.model} 正在行驶")
    
    def __str__(self):
        """字符串表示"""
        return f"Car(brand='{self.brand}', model='{self.model}', wheels={self.wheels})"

class Bicycle(Vehicle):
    """自行车类"""
    def __init__(self, brand, model, wheels):
        """初始化自行车"""
        super().__init__(brand, model)
        self.wheels = wheels
    
    def drive(self):
        """重写行驶方法"""
        print(f"{self.brand} {self.model} 正在骑行")
    
    def __str__(self):
        """字符串表示"""
        return f"Bicycle(brand='{self.brand}', model='{self.model}', wheels={self.wheels})"

# 测试
car = Car("特斯拉", "Model 3", 4)
bicycle = Bicycle("捷安特", "ATX777", 2)

print(car)
car.drive()

print(bicycle)
bicycle.drive()

# 多态
vehicles = [car, bicycle]
print("\n多态演示:")
for vehicle in vehicles:
    vehicle.drive()
```