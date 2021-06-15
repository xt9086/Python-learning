# Python2.x和Python3.x的区别

## 前言

### future模块

Python 3.x 介绍的 一些Python 2 不兼容的关键字和特性可以通过在 Python 2 的内置 `__future__` 模块导入。如果你计划让你的代码支持 Python 3.x，建议你使用 `__future__` 模块导入。例如，如果我想要 在Python 2 中表现 Python 3.x 中的整除，我们可以通过如下导入。

```python
from __future__ import division
```

### 官方参考文档

[Python 2.0 到 3.9 的全部新变化](https://docs.python.org/zh-cn/3.9/whatsnew/index.html)

## 编码

### 源码文件编码

在 python2.x 版本，python源码文件默认使用`Ascii`编码，所以无法直接显示中文。需要在源码文件头部通过声明`# -*- encoding: utf-8 -*-`来告诉解释器使用`utf-8`编码处理源文件。

而 python3.x 源码文件默认以 `UTF-8` 编码方式处理。

### 字符串编码

早期Unicode标准并未发布时，python的字符串`str`默认使用`ASCII`进行编码。后来`python2.0`提供了一种新的存储文本数据的数据类型：`Unicode` 对象，添加了对Unicode的支持。它可以用来存储和操作 `Unicode` 数据。所以python2同时有`Ascii`编码的`str`和`Unicode` 字符串。

到了python3以后，`python`删除了`Unicode` 对象类型，使字符串均由`Unicode`编码。

## 标准输入输出

### 输出

删除了 python2 的`print`语句 ，取而代之的是 `print()`函数。 Python 2.6 与 Python 2.7 **部分地**支持这种形式的 `print` 语法。在 Python 2.6 与Python 2.7 里面，以下三种形式是等价的：

```python
print "fish"
print ("fish") # 注意print后面有个空格
print("fish") # print()不能带有任何其它参数
```

如果 Python2.x 版本想使用使用 Python3.x 的 print 函数，可以导入 `__future__`包，该包禁用 Python2.x 的 `print` 语句，采用 Python3.x 的 `print` 函数

```python
from __future__ import print_function
print("fish", "panda", sep=', ')
```

### 输入

在 python2 中常用两个函数进行输入：

1. **input()**

   把用户的输入按照代码进行解释，得到解释后的值，例如：

   | 用户输入 | 得到的值                                     |
   | -------- | -------------------------------------------- |
   | name     | 识别为变量name，取变量name的值，不存在则报错 |
   | 123      | 整数123                                      |
   | 3.14     | 浮点数3.14                                   |
   | "123"    | 字符串类型的123                              |

2. **raw_input()**

   将所有的输入识别为字符串。

而 python3 只有`input()`函数且等价于 python2 的`raw_input()`函数。

## 运算符

### 除法

python2 中除法`a/b`：

* 若a、b都是整数则地板除，结果向下取整（结果为负时，取小于该结果的第一个负整数），例如\(-5/2=-3\)。
* 若a、b至少一个为浮点数，则结果也是相对精确的浮点数；对于`a//b`，无论a、b为何种数字类型结果都向下取整，只是a、b有浮点数时结果取整后以浮点数形式显示（5.0//2=2.0）。

python3 中`a/b`默认结果总为浮点数，`a//b`与python2一致。

### 不等运算符

Python2.x 中不等于有两种写法`!=`和`<>`，Python3.x中去掉了`<>`, 只有`!=`一种写法。

## 八进制的表示方式

Python2 可以用**0**开头或者**0o**开头表示八进制，python3 只能用**0o**开头表示。

## 数据类型

### 删除long类型

python3 删除了`long`类型，现在只有一种整型——`int`，但它的行为就像2.x版本的`long`。

### 新增bytes类型

python3 新增了二进制序列类型bytes。bytes 对象是由单个字节构成的不可变序列，即字符经过编码的以八位二进制为单位的序列。

另外，在 Python 2.x 系列中，允许 8 位字符串（ 2.x 所提供的最接近内置二进制数据类型的对象）与 Unicode 字符串进行各种隐式转换。 这是为了实现向下兼容的变通做法，以适应 Python 最初只支持 8 位文本而 Unicode 文本是后来才被加入这一事实。 在 Python 3.x 中，这些隐式转换已被取消 —— 8 位二进制数据与 Unicode 文本间的转换必须显式地进行，bytes 与字符串对象的比较结果将总是不相等。

### 返回迭代器

**map、filter 和 reduce**等高阶函数返回值的类型由列表改为迭代器，另外reduce函数在 Python 3.x 中已经不属于 built-in 了，被挪到 functools 模块当中。

### 返回视图对象

字典的`keys()`、`values()`、`items()`方法在python2中返回列表，在python3中返回可迭代的视图对象。

## 关于类

### 经典类与新式类

python2 允许创建一个经典类，即不继承任何类，包括`object`类。创建新式类要显式继承父类。

python3 不再支持经典类，若定义时不显式继承任何类，则默认继承`object`类。

### 特殊函数super

python2 使用`super()`在子类方法关联父类对应方法时必须要传递父类名和子类的`self`给`super()`作为参数，而在python3 可以省略`super()`的参数。

```python
class C(B):
    def method(self, arg):
        # super().父类对应方法(父类的参数)
        super().method(arg)
        # 上一句写法在Python3等价于如下语句
        # super(C, self).method(arg)
```

## 删除repr表达式

Python 2.x 中反引号&#96;&#96;相当于`repr`函数的作用，返回一个字符串对象。

Python 3.x 中去掉了这种写法，只允许使用`repr`函数。

## range与xrange

python 2.x 中`range`函数返回一个数字列表，而`xrange`函数返回xrange对象，它表示一个不可变的数字序列。xrange对象相比常规 list 或 tuple 的优势在于一个 xrange 对象总是占用固定数量的（较小）内存，不论其所表示的范围有多大（因为它只保存了 start, stop 和 step 值，并会根据需要计算具体单项或子范围的值）。这一点与生成器的惰性计算有点相似，它是可迭代对象但并不是生成器或者迭代器。

python 3.x 中只保留了`range`函数，它与`xrange`十分相似，但是支持了更多功能，如3.2支持了切片操作。

另外，在 3.3 版更改: 定义 '==' 和 '!=' 以根据 range 对象所定义的值序列来进行比较（而不是根据对象的标识）。也就是说，如果两个 range 对象表示相同的值序列就认为它们是相等的。请注意比较结果相等的两个 range 对象可能会具有不同的 start，stop 和 step 属性，例如 `range(0) == range(2, 1, 3)`而 `range(0, 3, 2) == range(0, 4, 2)`。

## 异常

在 Python 3 中处理异常也轻微的改变了，在 Python 3 中我们现在使用 as 作为关键词。

捕获异常的语法由 `except exc, var` 改为 `except exc as var`。

使用语法`except (exc1, exc2) as var` 可以同时捕获多种类别的异常。 Python 2.6 已经支持这两种语法。

* 在 2.x 版本，所有类型的对象都是可以被直接抛出的，在 3.x 时代，只有继承自`BaseException`的对象才可以被抛出。
* 在2.x 版本`raise` 语句使用逗号将抛出对象类型和参数分开，3.x 取消了这种奇葩的写法，直接调用构造函数抛出对象即可。如`raise TypeError('MyRange expected 1 arguments, got 0')`。

## 布尔值

`True` 和 `False` 在 Python2 中是两个全局变量，既然是变量，那么他们就可以指向其它对象，例如：

```python
# python 2.x
print True
print False
True = 123
False = 321
print True
print False
# 输出结果如下：
# True
# False
# 123
# 321
```

Python3 修正了这个缺陷，True 和 False 变为两个关键字，永远指向两个固定的对象，不允许再被重新赋值。

## 新增nonlocal语句

[`nonlocal`](https://docs.python.org/zh-cn/3.8/reference/simple_stmts.html#nonlocal) 语句会使得所列出的名称指向之前在最近的包含作用域中绑定的除全局变量以外的变量。例如内层函数的局部变量n绑定外层函数的局部变量n。 这种功能很重要，因为绑定的默认行为是先搜索局部命名空间。 这个语句允许被封装的代码重新绑定局部作用域以外且非全局（模块）作用域当中的变量。

## 回收列表推导式的变量

在python2中，如下列表推导式中for语句的变量x在后面的代码中可被使用：

```python
y = [x for x in xrange(10)]
print x
print y
# 输出如下：
# 9
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

而python3，变量x作为局部变量在列表推导式执行结束后就被回收了，后续无法访问。

```python
y = [x for x in range(10)]
print(x)
print(y)
# 输出：
# Traceback (most recent call last):
#   File "<input>", line 2, in <module>
# NameError: name 'x' is not defined
```

## 不可排序类型的报错

当对不可排序类型做比较的时候，python2会返回False，python3会抛出一个类型错误：

```python
# python 2.x
print [1, 2, 3] > 'abc'
# False

# python 3.x
print([1, 2, 3] > 'abc')
# Traceback (most recent call last):
#   File "E:/CS_Practice/python/2021/main.py", line 4, in <module>
#     print([1, 2, 3] > 'abc')
# TypeError: '>' not supported between instances of 'list' and 'str'
```

## 未完，待续......

