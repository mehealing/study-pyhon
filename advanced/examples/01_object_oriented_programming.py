#!/usr/bin/env python3
"""
面向对象编程示例
功能：演示Python中的面向对象编程特性
"""

# 基本类定义和使用
print("\n=== 基本类定义和使用 ===")

class Person:
    """人员类"""
    # 类变量
    total = 0
    
    def __init__(self, name, age):
        """构造方法"""
        # 实例变量
        self.name = name
        self._age = age  # 保护属性
        self.__salary = 5000  # 私有属性
        Person.total += 1
    
    def greet(self):
        """实例方法"""
        return f"Hello, my name is {self.name}"
    
    @classmethod
    def get_total(cls):
        """类方法"""
        return f"总人数: {cls.total}"
    
    @staticmethod
    def is_adult(age):
        """静态方法"""
        return age >= 18
    
    # 属性装饰器
    @property
    def age(self):
        """年龄属性"""
        return self._age
    
    @age.setter
    def age(self, value):
        """设置年龄"""
        if value > 0:
            self._age = value
    
    # 特殊方法
    def __str__(self):
        return f"Person(name='{self.name}', age={self.age})"

# 使用基本类
person1 = Person("张三", 30)
person2 = Person("李四", 25)

print(f"person1: {person1}")
print(f"person1.greet(): {person1.greet()}")
print(f"person1.age: {person1.age}")

# 修改属性
person1.age = 31
print(f"修改年龄后 person1.age: {person1.age}")

# 类方法和静态方法
print(f"Person.get_total(): {Person.get_total()}")
print(f"Person.is_adult(18): {Person.is_adult(18)}")
print(f"Person.is_adult(17): {Person.is_adult(17)}")

# 继承
print("\n=== 继承 ===")

class Animal:
    """动物类"""
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "动物发出声音"

class Dog(Animal):
    """狗类"""
    def __init__(self, name, breed):
        super().__init__(name)  # 调用父类的构造方法
        self.breed = breed
    
    def speak(self):  # 方法重写
        return "汪汪汪"

class Cat(Animal):
    """猫类"""
    def speak(self):  # 方法重写
        return "喵喵喵"

# 使用继承
dog = Dog("旺财", "金毛")
cat = Cat("咪咪")

print(f"dog.name: {dog.name}")
print(f"dog.breed: {dog.breed}")
print(f"dog.speak(): {dog.speak()}")
print(f"cat.name: {cat.name}")
print(f"cat.speak(): {cat.speak()}")

# 多态
print("\n=== 多态 ===")

def make_speak(animal):
    print(f"{animal.name} says: {animal.speak()}")

make_speak(dog)
make_speak(cat)

# 特殊方法
print("\n=== 特殊方法 ===")

class Point:
    """点类"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __len__(self):
        # 这里返回点到原点的距离的整数部分
        return int((self.x ** 2 + self.y ** 2) ** 0.5)

# 使用特殊方法
p1 = Point(1, 2)
p2 = Point(3, 4)
print(f"p1: {p1}")
print(f"p2: {p2}")
p3 = p1 + p2
print(f"p1 + p2: {p3}")
print(f"p1 == p2: {p1 == p2}")
print(f"len(p1): {len(p1)}")

# 抽象基类
print("\n=== 抽象基类 ===")

from abc import ABC, abstractmethod

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

class Rectangle(Shape):
    """矩形类"""
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    """圆形类"""
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        import math
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        import math
        return 2 * math.pi * self.radius

# 使用抽象基类
rect = Rectangle(3, 4)
print(f"Rectangle area: {rect.area()}")
print(f"Rectangle perimeter: {rect.perimeter()}")

circle = Circle(5)
print(f"Circle area: {circle.area():.2f}")
print(f"Circle perimeter: {circle.perimeter():.2f}")

# 组合
print("\n=== 组合 ===")

class Engine:
    """引擎类"""
    def start(self):
        return "引擎启动"

class Car:
    """汽车类"""
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.engine = Engine()  # 组合
    
    def drive(self):
        return f"{self.brand} {self.model}: {self.engine.start()}, 汽车行驶"

# 使用组合
car = Car("特斯拉", "Model 3")
print(car.drive())

# 多重继承
print("\n=== 多重继承 ===")

class A:
    """类A"""
    def method(self):
        return "A.method()"

class B:
    """类B"""
    def method(self):
        return "B.method()"

class C(A, B):
    """类C，继承自A和B"""
    pass

# 使用多重继承
c = C()
print(f"C.method(): {c.method()}")
print(f"C.__mro__: {C.__mro__}")  # 方法解析顺序

print("\n=== 面向对象编程示例完成 ===")
