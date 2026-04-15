# 面向对象编程

## 什么是面向对象编程？

面向对象编程（Object-Oriented Programming，简称OOP）是一种编程范式，它将数据和操作数据的方法封装在一起，形成对象。在Python中，一切皆对象。

## 类的定义

类是对象的蓝图，定义了对象的属性和方法。使用`class`关键字定义类。

```python
class ClassName:
    """类的文档字符串"""
    # 类变量
    class_variable = "value"
    
    def __init__(self, parameter1, parameter2):
        """构造方法"""
        # 实例变量
        self.instance_variable1 = parameter1
        self.instance_variable2 = parameter2
    
    def method(self):
        """实例方法"""
        # 方法体
        pass
```

- `class`：定义类的关键字
- `ClassName`：类名，遵循驼峰命名法
- `__init__`：构造方法，用于初始化对象
- `self`：表示实例本身，必须是方法的第一个参数
- `class_variable`：类变量，所有实例共享
- `instance_variable`：实例变量，每个实例独有

## 对象的创建

创建对象（实例化）是通过调用类名并传递参数来完成的。

```python
# 创建对象
obj = ClassName(argument1, argument2)

# 访问实例变量
print(obj.instance_variable1)

# 调用实例方法
obj.method()

# 访问类变量
print(ClassName.class_variable)
```

## 实例方法、类方法和静态方法

### 实例方法

实例方法是最常用的方法类型，它接收`self`作为第一个参数，表示实例本身。

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        """实例方法"""
        return f"Hello, my name is {self.name}"

# 使用
person = Person("张三", 30)
print(person.greet())  # 输出: Hello, my name is 张三
```

### 类方法

类方法接收`cls`作为第一个参数，表示类本身，使用`@classmethod`装饰器定义。

```python
class Person:
    total = 0  # 类变量
    
    def __init__(self, name):
        self.name = name
        Person.total += 1
    
    @classmethod
    def get_total(cls):
        """类方法"""
        return f"总人数: {cls.total}"

# 使用
p1 = Person("张三")
p2 = Person("李四")
print(Person.get_total())  # 输出: 总人数: 2
```

### 静态方法

静态方法不接收特殊参数，使用`@staticmethod`装饰器定义。

```python
class Math:
    @staticmethod
    def add(a, b):
        """静态方法"""
        return a + b

# 使用
print(Math.add(1, 2))  # 输出: 3
```

## 继承

继承是面向对象编程的重要特性，它允许创建一个新类（子类），继承现有类（父类）的属性和方法。

```python
# 父类
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "动物发出声音"

# 子类
class Dog(Animal):
    def speak(self):
        return "汪汪汪"

# 子类
class Cat(Animal):
    def speak(self):
        return "喵喵喵"

# 使用
dog = Dog("旺财")
print(dog.name)  # 输出: 旺财
print(dog.speak())  # 输出: 汪汪汪

cat = Cat("咪咪")
print(cat.name)  # 输出: 咪咪
print(cat.speak())  # 输出: 喵喵喵
```

### 方法重写

子类可以重写父类的方法，以提供自己的实现。

### super() 函数

`super()`函数用于调用父类的方法，通常在子类的`__init__`方法中使用。

```python
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)  # 调用父类的__init__方法
        self.breed = breed

# 使用
dog = Dog("旺财", 3, "金毛")
print(dog.name)  # 输出: 旺财
print(dog.age)  # 输出: 3
print(dog.breed)  # 输出: 金毛
```

## 多态

多态是指不同类的对象可以通过相同的接口（方法名）调用不同的实现。

```python
def make_speak(animal):
    print(animal.speak())

# 使用
dog = Dog("旺财")
cat = Cat("咪咪")

make_speak(dog)  # 输出: 汪汪汪
make_speak(cat)  # 输出: 喵喵喵
```

## 封装

封装是指将数据和操作数据的方法捆绑在一起，对外部隐藏实现细节。在Python中，通过命名约定实现封装：

- `name`：普通属性
- `_name`：保护属性（约定不要直接访问）
- `__name`：私有属性（会被名称修饰，实际上是`_ClassName__name`）

```python
class Person:
    def __init__(self, name, age):
        self.name = name  # 普通属性
        self._age = age  # 保护属性
        self.__salary = 5000  # 私有属性
    
    def get_salary(self):
        """获取工资"""
        return self.__salary
    
    def set_salary(self, salary):
        """设置工资"""
        if salary > 0:
            self.__salary = salary

# 使用
person = Person("张三", 30)
print(person.name)  # 输出: 张三
print(person._age)  # 输出: 30（可以访问，但约定不要这样做）
# print(person.__salary)  # 错误: AttributeError
print(person.get_salary())  # 输出: 5000
person.set_salary(6000)
print(person.get_salary())  # 输出: 6000
```

## 属性装饰器

Python提供了`@property`装饰器，用于将方法转换为属性访问。

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age
    
    @property
    def age(self):
        """年龄属性"""
        return self._age
    
    @age.setter
    def age(self, value):
        """设置年龄"""
        if value > 0:
            self._age = value

# 使用
person = Person("张三", 30)
print(person.age)  # 输出: 30（使用@property装饰的方法）
person.age = 31  # 使用@age.setter装饰的方法
print(person.age)  # 输出: 31
```

## 特殊方法

Python中有许多特殊方法（魔术方法），它们以双下划线开头和结尾。

### 常用特殊方法

- `__init__`：构造方法
- `__str__`：返回对象的字符串表示
- `__repr__`：返回对象的官方字符串表示
- `__len__`：返回对象的长度
- `__add__`：定义加法操作
- `__eq__`：定义相等性比较

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

# 使用
p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1)  # 输出: Point(1, 2)
p3 = p1 + p2
print(p3)  # 输出: Point(4, 6)
print(p1 == p2)  # 输出: False
```

## 抽象基类

抽象基类（Abstract Base Class，简称ABC）是不能直接实例化的类，它定义了子类必须实现的方法。使用`abc`模块创建抽象基类。

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        """计算面积"""
        pass
    
    @abstractmethod
    def perimeter(self):
        """计算周长"""
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

# 使用
rect = Rectangle(3, 4)
print(rect.area())  # 输出: 12
print(rect.perimeter())  # 输出: 14
```

## 组合

组合是一种设计模式，它允许一个类包含另一个类的实例作为其属性。

```python
class Engine:
    def start(self):
        return "引擎启动"

class Car:
    def __init__(self):
        self.engine = Engine()  # 组合
    
    def drive(self):
        return f"{self.engine.start()}, 汽车行驶"

# 使用
car = Car()
print(car.drive())  # 输出: 引擎启动, 汽车行驶
```

## 练习

1. 编写一个`Student`类，包含姓名、年龄、学号等属性，以及学习、考试等方法。
2. 编写一个`Circle`类，继承自`Shape`抽象基类，实现面积和周长的计算。
3. 编写一个`BankAccount`类，包含余额属性，以及存款、取款、查询余额等方法。
4. 编写一个`Employee`类，包含姓名、工号、工资等属性，以及计算奖金、打印信息等方法。
5. 编写一个`Library`类，包含书籍列表，以及添加书籍、删除书籍、查找书籍等方法。

## 参考资料

- [Python官方文档 - 类](https://docs.python.org/zh-cn/3/tutorial/classes.html)
- [Python面向对象编程 - 菜鸟教程](https://www.runoob.com/python/python-object.html)