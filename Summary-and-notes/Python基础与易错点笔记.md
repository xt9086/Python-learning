# Python基础与易错点笔记

## 小的注意事项

1. 注意单双引号嵌套时的匹配  。
2. 整数等类型直接用于字符串拼接会报类型错误，需要先用`str()`转换类型  。
3. `python2`除法`a/b`：若a、b都是整数则地板除，结果向下取整（结果为负数时，取小于该结果的第一个负整数），例如\(-5/2=-3\)；若a、b至少一个为浮点数，则结果也是相对精确的浮点数；对于`a//b`，无论a、b为何种数字类型结果都向下取整，只是a、b有浮点数时结果取整后以浮点数形式显示（5.0//2=2.0）。`python3`中`a/b`默认结果总为浮点数，`a//b`与`python2`一致。
4. 反斜杠`'\'`用于将字符转义表达，`r'str'`表示`'str'`该字符串内所有字符不转义，按字符原始意义表达。
5. 函数中`finally`下的`return`语句会执行并把之前的`return`语句的值覆盖。
6. 对递归的理解的要点主要在于放弃！放弃你对于理解和跟踪递归全程的企图，只理解递归两层之间的交接，以及递归终结的条件。
7. 在函数里用`with`语句创建`socket`，即使`with`语句代码块内创建的子线程还在运行，只要执行完`with`里的代码就会跳出`with`语句执行函数剩余代码。导致子线程的内容还没执行完就被with自动关闭了`socket`。可以在`with`代码块最后或者说在关闭`socket`之前调用`socket`对象的`join`方法。`join`方法在子线程结束后才能执行，可以保证子线程没完成作业前`socket`不会被提前关闭。
8. lambda表达式是个未被调用的匿名函数，相当于函数名。要调用它，需要在后面加括号。
9. float浮点数最多显示17位有效数字，超过17位的会被四舍五入到最后一位。

## 字符串

### 注意

1. 字符串没有`reverse()`方法，list才有，字符串和list都可以使用`reversed()`函数来实现逆序。但是得到的不是`list`而是迭代器，需要用`list()`转化。
2. 空字符串`'' in str`，*str*为任何字符串结果都为`True`。
3. 常见空白字符：`' '空格，'\n'换行，'\r'回车，'\t'水平制表符，'\v'垂直制表符，'\f'翻页`

### 基本操作

1. 消除多余字符

   `str.strip(chars)`返回一个将`str`两端删去字符串`chars`包含的字符的副本，默认删除空白字符。只删去两端在`chars`里有的字符，直到遇到不是目标字符停止。

   `str.lstrip()`左侧，`str.rstrip()`右侧。

2. 分割组装成列表

   `str.split(sep, maxsplit)`按参数`sep`分隔标志将原字符串分割并组装成列表返回。

   `maxsplit`表示从左到右最大分割次数，如`maxsplit=2`表示分两次得到三个元素列表。

   `str.partition(sep)`在`str`内根据正序找到的首个参数`sep`输入的字符串将原`str`分成三组构成一个元组返回，即`(str1,sep,str2)`。若`sep`在`str`内不存在，则返回`(str,'','')`。

   `str.rpartition(sep)`从右侧开始分割，`sep='.'`时可用于分割文件名和后缀名。

3. 可迭代对象组装成字符串

   `str.join(iterable)`将可迭代对象的元素(必须是`str`类型)用字符串`str`连接起来组成新的字符串。

4. 查找

   `str.find(sub,start,end)`正序查找sub在字符串首次出现的下标，查找失败时返回-1。

   参数`start`和`end`表示从切片`str[start:end]`中查找，仅字符串有此方法。

   `str.index(sub,start,end)`与`find()`相似，但字符不存在时抛出错误。

5. 计数

   `str.count(sub,start,end)`统计并返回参数sub在`str[start:end]`出现的次数。

6. 替换

   `str.replace(old,new,count)`将`str`中原来的参数`old`字符替换为参数`new`字符。

   参数`count`为替换个数，默认值为-1，表示全部替换。

7. 大小写

   `str.upper()`使字符串里英文字母全改为大写，`str.lower()`使字符串里字母全变小写。

   `str.capitalize()`使整个字符串仅首字母大写其他字母均为小写。

   `str.title()`使字符串里每一个单词首字母大写，将由其他符号隔开的英文字母识别为单词。

8. 对齐排列

   `str.ljust(width,fillchar)`返回一个将`str`向左对齐排列总宽度`width`个字符的字符串。当`str`宽度小于`width`，用`fillchar`(默认为空格)指定的字符填充空白部分，反之不填充。

   `rjust()`为右排列，`center()`为居中排列，其他与`ljust()`类似。

## 列表

### 基本操作

1. 添加元素

   `list.append(object)`每次在列表末尾添加一个元素。

   `list.insert(index,object)`指定索引位置插入一个元素，原处元素右移一位，若索引号大于list的最大索引则添加在末尾。

   `list.extend(iterable)`将一个可迭代对象的所有元素按顺序添加到`list`的末尾。

2. 删除元素

   `del list[index]`使用`del`语句根据索引号删除，被删除的值无法访问。

   `list.pop(index)`弹出对应索引的值，同时返回被删除的值，`index`缺省时弹出最后一个值。

   `list.remove(object)`索引未知时可根据值删除元素 ，有重复值时一次调用也只能按顺序删一个值。

   `list.clear()`清空列表所有元素。

### 排序

使用使用`sort()`方法按特定规则排序会永久性地改变原来的值，参数`reverse=True`时倒序排列。它可以传入参数key，key是函数,会对传入的list进行处理，按处理后的结果进行比较。

```python
# str.lower是指str类的lower方法，此时作为参数传的是方法名，切记不能带括号
seq_list = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
print(seq_list)
# ['Zoo', 'Credit', 'bob', 'about']
```

使用`reverse()`方法可得到仅逆转原来顺序并不按规则排序的列表，原来的值会永久性改变，但可再次调用`reverse()`方法恢复。

## range函数

`range`函数返回range对象，它表示一个不可变的数字序列。range对象相比常规 `list` 或 `tuple` 的优势在于一个 range 对象总是占用固定数量的（较小）内存，不论其所表示的范围有多大（因为它只保存了 start, stop 和 step 值，并会根据需要计算具体单项或子范围的值）。这一点与生成器的惰性计算有点相似，它是可迭代对象但并不是生成器或者迭代器。

`list(range(n))为[0,1,...,n-2,n-1]`

`list(range(m,n))为[m,m+1,...,n-2,n-1]`

`list(range(m,n,k))为[m,m+k,m+2k,...,n-(n-m)%k]`

若*step*为正，通项公式为`r[i]=start+step*i`，其中`i>=0`且`r[i]<stop`。

若*step*为负，通项公式仍为`r[i]=start+step*i`，但其中`i>=0`且`r[i]>stop`。

*step*为负表示创建从m到n以*step*的绝对值递减的数列，故`m>n`时才有意义。

## 元组

### 注意

1. 元组真的不可变吗

   元组的元素虽然不能修改，但是可给指向该元组的变量赋新值。

   元组虽然是不可变类型，但是若元组的元素是列表等可变类型，则当该元素的的成员改变也会影响到元组。因为元组的不可变指的是每个元素指向的地址不变，而不保证指向的地址存储的内容不变。因此要想定义一个内容也不变的元组就得使每一个元素都是不可变对象。

   ```Python
   b = ('d', 'e')
   a = (1, 2, 3, b)
   print(a)
   b = ('f', 'g')
   print(a)
   # (1, 2, 3, ('d', 'e'))
   # (1, 2, 3, ('d', 'e'))
   # 对元组b重新赋值改变的是b的指向，不会影响a的值
   # 这里b即使为列表也不会改变元组a，因为改变的是b的指向而不是对b指向的内容的修改
   ```

2. 只有1个元素的tuple定义时必须加一个逗号，来消除歧义与`()`运算符的歧义。


## 浮点数与字符串转整型

`int()`将浮点数转整型原理是直接舍去小数部分。

`int(x, base=10)`是把字符按照给定的进制识别再转换成十进制整数，注意不是转换为字符对应的ASCII码！另外并不是所有字符都可以直接转成对应整数，要注意相关进制的范围,以及`int()`默认参数是对应的十进制数。例如：十进制0到9，十六进制0到9以及a到f。

`'a'`直接用`int()`转会报错，因为十进制没有a，只能按照16进制转：`int('a', 16)`，结果是十进制的10。

## 赋值

### 基本方式

可以连等：`a=b=c=1`

可以用可迭代对象拆包分散赋值：`a,b,c = 1,2,3`相当于`a,b,c=[1,2,3]`相当于`a,b,c = (1,2,3)`

python中变量前加\*号代表可变长度，则有

```python
>>> a, *b, c = [1, 2, 3, 4]
>>> print(a, b, c)
1 [2, 3] 4
```

### 赋值添加值易错点

列表的变量名相当于地址，将它赋给别的变量，则牵一发而动全身。一处变量更改地址对应内存的值，变化也会反应到别的指向这块内存的变量。

所以在使用`append()`和`insert()`方法添加一个列表作为元素到另一个列表时要十分谨慎，添加单个值不会有问题。

对于元组，虽是不可变类型，也要注意，元组名被重新赋值初始化，其他地方的值也会变。

## 逻辑运算的短路问题

```Python
# 1. and

>>> 2 > 1 and print('yes')
yes
>>> 2 < 1 and print('no')
False
# 因为逻辑与只要遇到False值就不再执行后续的逻辑运算了
>>> print(1 and 2 and 0 and 'hello')
0

# 2. or

>>> 2 > 1 or print('yes')
True
>>> 2 < 1 or print('no')
no
# 因为逻辑或只要遇到True就不再执行后续的逻辑运算了
>>> print(0 or [] or 'yes' or 'no')
yes
```

## 推导式

### 列表推导式

1. 在一个列表推导式中，for前面的if ... else是表达式，而for后面的if是过滤条件，不能带else：

   ```Python
   >>> [x if x % 2 == 0 else -x for x in range(1, 11)]
   [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]
   >>> [x for x in range(1, 11) if x % 2 == 0]
   [2, 4, 6, 8, 10]
   ```

2. 列表推导式易错题

   ```Python
   L1 = [x for x in range(10) if x % 2]
   print(L1)
   # 输出为：[1, 3, 5, 7, 9]
   # 上面代码等效于如下代码：
   L2 = []
   for i in range(10):
       if i % 2:
           L2.append(i)
   # 当i为偶数，i%2为0，对应布尔值False，此时不会向L2里添加i
   # 当i为奇数，i%2!=0，对应布尔值True，此时执行后面语句添加i
   ```

### 字典推导式

```Python
d = {'a': 1, 'b': 2, 'c': 3}
L = [('e', 5), ('f', 6)]

d1 = {v: k for k, v in d.items()}
d2 = {k: v for k, v in L}
print(d1)
print(d2)

# 结果如下：
# {1: 'a', 2: 'b', 3: 'c'}
# {'e': 5, 'f': 6}
```

## 切片

`L[m:n:k]`从下标m切到下标n（不包括n），每k个单位切走一个。m、n为负数时表示从右往左数第m、n个。k为负数表示从右往左每k个单位切一个，用于逆序切片。

`L[::]`或者`L[:]`切片复制原列表。

`L[::-1]`切片逆序原列表，因为步长为负表示从右往左切。

`L[-m:-n`]且`m>n`，表示从右往左数从第m切到第n个，步长为正从左向右输出。

## 格式字符串

更多格式化参数见：[格式规格迷你语言](https://docs.python.org/zh-cn/3.8/library/string.html#formatspec)

下述的 *f-string*是3.6版本新增功能，参见：[格式化字符串字面值](https://docs.python.org/zh-cn/3.8/reference/lexical_analysis.html#f-strings)

```Python
name = '小明'
height = 180
weight = 143.1415926

#       用%格式化输出

print("我叫%s,身高%dcm,体重%f斤，体脂率%%10" % (name, height, weight))
# %s字符串、%d十进制整数、%x十六进制数、%f浮点数，%f默认保留6位小数，用%%输出%
# 我叫小明,身高180cm,体重143.141593斤，体脂率%10

print("我叫%s,身高%6dcm,体重%8.2f斤" % (name, height, weight))
# 6和8表示输出占位多少格，未占满会在左侧留下空白，2表示四舍五入保留几位小数
# 我叫小明,身高   180cm,体重  143.14斤

print("我叫%s,身高%-6dcm,体重%08.2f斤" % (name, height, weight))
# ‘-’负号表示靠左对齐，0用来填充左侧空白
# 我叫小明,身高180   cm,体重00143.14斤


#       用format()方法

print("我叫{},身高{:06d}cm,体重{:8.2f}斤".format(name, height, weight))
# 按顺序一一对应赋值，且{}内可以用:替代%加格式化参数来控制输出格式
# 我叫小明,身高000180cm,体重  143.14斤

print("我叫{0},身高{2:06d}cm,体重{1:8.2f}斤".format(name, weight, height))
# {}内可以指定序号，填充format()里对应排序的参数值
# 我叫小明,身高000180cm,体重  143.14斤

print("我叫{n},身高{h:06d}cm,体重{w:8.2f}斤".format(n=name, h=height, w=weight))
# {}内可以指定变量名来填充值，变量名和序号可以混合使用但format()里变量名的参数要先给出，不建议这样用
# 我叫小明,身高000180cm,体重  143.14斤

L = ['小明', 180, 143.1415926]
print("我叫{},身高{:06d}cm,体重{:8.2f}斤".format(*L))
# 列表或元组可以通过 * 加变量名的可变参数传入format()
# 我叫小明,身高000180cm,体重  143.14斤

D = {'name': '小明', 'height': 180, 'weight': 143.1415926}
print("我叫{name},身高{height:06d}cm,体重{weight:8.2f}斤".format(**D))
# 字典可通过**加字典名的关键字参数将value传入format()，{}里是字典的key值
# 我叫小明,身高000180cm,体重  143.14斤


#       用f-string格式化输出
print(f"我叫{name},身高{height:06d}cm,体重{weight:8.2f}斤")
# f加在字符串前，{}做占位符，变量填充值，同样{}内可以用:替代%加格式化参数来控制输出格式
# 我叫小明,身高000180cm,体重  143.14斤
```

## is和==的本质

`is`表示两边的内存地址相等，`==`表面上是两边的值相等。

两个对象a、b使用==进行比较实际上是调用对象a的`__eq__`方法，即`A.__eq__(b)`。自定义的类如果未重写`__eq__`方法，那么`__eq__`方法和`is`一样是比较两者的内存地址。

## time模块

`clock()`函数自 python3.3 版本开始不再推荐使用，并且于3.8版本正式删除。

可用`time()`、`perf_counter()`、`process_time()`以及 python3.7 新增的精确到纳秒的`time_ns()`、`perf_counter_ns()`、`process_time_ns()`等。

## 浅拷贝与深拷贝

```Python
import copy as cp

# 1.这不是拷贝，只是将变量存的指向数据的地址赋给另一个变量
L1 = [1, 2, 3, ['a', 'b']]
L2 = L1
# L1和L2修改指向的数据时会影响到对方

# 2.浅拷贝
L3 = L1.copy()
L4 = cp.copy(L1)
# 以上都是浅拷贝，即只复制原结构第一层级的数据
# 更深层级的数据发生改变会影响到拷贝得到的副本
# 比如copy()方法复制L1时，L1里面的列表只被复制了改列表指向数据的地址
# 往后那块地址的数据发生改变也会影响到L3、L4里同样指向那块数据的列表

# 3.深拷贝
L5 = cp.deepcopy(L1)
# 深拷贝会将原数据所有层级的内容复制，副本所有元素不再指向原来的内存地址
# 深拷贝得到的副本与原来对象无任何关系，也不会受到其的影响
# 深拷贝可通过引入copy模块的deepcopy()实现
```

## 字典

### 注意

字典的键必须是不可变对象。

两个字典不支持用`+`拼接。

两个字典的比较当且仅当它们具有相同的 (键, 值) 对时才会相等（不考虑顺序）。 排序比较 ('<', '<=', '>=', '>') 会引发 `TypeError`。

`in`只作用于字典的`key`，判断某个对象是否存在于字典的`key`。

字典的元素在`python3.7`版本前是无序的，即获取元素的顺序是不可测的，键—值对的排列顺序与添加顺序不同。自3.7后，`dic`t类型的顺序是插入的顺序，此特性由自 3.6 版开始的 CPython 实现。

在 3.8 版更改，字典及其视图对象`keys()`、`values()`、`items()`现在是可逆的。可以通过`reversed()`函数返回一个逆序的迭代器。

### 基本操作

`dic.get(key,default==None)`根据`key`查找并返回值，`key`不存在时默认返回`None`，可以指定返回值。

`dic.pop(key)`根据`key`删除值并返回删除的值，`key`不可缺省，`key`不存在则报错。

`dic.popitem()`删除一个键值对，并组装成一个元组返回，若字典空则报错。注意在3.7版本以前该方法是返回任意键值对，之后改为LIFO (last-in, first-out)的方法确定删除返回的键值对。

`dic.update(iterable)`只有一个参数，可以是将一个字典里的键值对添加到`dic`组成一个新字典。也可以传入两个可迭代对象E和F组成的关键字参数，E和F分别提供键和值。

## 拆包

```Python
# 不只有字典可以这样遍历，可迭代对象都行，且变量可以不止两个
l1 = [('a', 1, 3), ('b', 2, 4)]
for k, v, m in l1:
    # 每次循环l1取出的元组l1[i]都会被拆包，使得被拆开的三个元素一一对应赋值给k,v,t
    # 理论上l1[i]如果有n个元素，那for循环可以赋值n个变量进行遍历
    print(k, ':', v, ':', m)
```

## enumerate函数使for循环带下标

```Python
L = ['a', 'b', 'c', 'd', 'e']
# enumerate()接收一个可迭代对象，与从0开始的索引序列组装到一起
# 遍历时拆包将值赋给对应变量
for index, member in enumerate(L):
    print(f'L[{index}] = {member}')
```

## 函数参数

### 参数类型

1. 位置参数

   传参时须按照定义函数时的参数顺序。

2. 必选参数

   必须传入，不可缺省的参数。

3. 默认参数

   定义时给出默认值的参数，缺省时传入默认值。可以按位置向默认参数传值，也可指定默认参数传值。

4. 可变参数

   可以传入任意个参数，系统自动将传入的多个参数组装为`tuple`，也可以提供一个`list`或者`tuple`的参数并在传入时变量名前面加上\*，表示把list或tuple的所有元素变成可变参数传入\*。

5. 关键字参数

   关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个`dict`。

6. 命名关键字参数

   命名关键字参数可以限定传入的关键字参数的名字，但必须传入参数名。用\*与一般的位置参数隔开，如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符\*了。

   ```Python
   def f1(a, b, c=0, *, d, **kw):
       print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
   
   def f2(a, b, c=0, *args, **kw):
       print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
   ```

### 参数组合

请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数：

```Python
# 参数组合
l1 = ['1', '2', '3', '4', '5']
d1 = {'h': 'H', 'd': 'D', 'e': 'E', 'g': 'G'}
# a、b是必选的位置参数，c是默认参数，args是可变参数
# d、e、f是命名关键字参数,其中e、f还给出了默认值，kwargs是关键字参数
def test_c_args(a, b, c=0, *args, d, e='up', f='F', **kwargs):
    print(a, b, c, args, d, e, f, kwargs)
# 函数调用时解释器会自动按照参数位置、名称、类型将参数传进去
# 可变参数*l1传进去时先传前面的必选参数和默认参数，剩余的再组成元组传到可变参数args
# 关键字参数**d1先传命名关键字参数，剩下的再以字典形成传入关键字参数kwargs
test_c_args(*l1, **d1)
# 输出结果：
# 1 2 3 ('4', '5') D E F {'h': 'H', 'g': 'G'}
# 故对于任意函数，都可以通过类似func(*args, **kwargs)的形式调用它，无论它的参数是如何定义的
```

### 类型提示

定义函数时可以给参数指定类型，但并非强制要求，仅作为提示：

```Python
def point(x: int, y: int):
    return x, y
print(point('a', 'b'))
# ('a', 'b')
# 编辑器会提示实参应为int，但是仍传str也不会报错
```

## reduce函数易错点

`reduce()`是`functools.py`模块的一个函数，使用时要引入该模块。

传入的函数必须只有两个参数，传参时要传函数名，不能带括号。

当函数参数返回值与列表值类型不一致易产生如下错误：

```Python
from functools import reduce

L = [
    {'index': 0, 'data': 5},
    {'index': 1, 'data': 12},
    {'index': 2, 'data': 13}
]

def get_ele_sum(x, y):
    return x['data'] + y['data']

print(reduce(get_ele_sum, L))

# 结果会报错 TypeError: 'int' object is not subscriptable
# 原因是reduce会把get_ele_sum(x, y)返回的结果作为下一轮的参数x
# 但是L的元素都是字典，get_ele_sum(x, y)的返回值是整数
# 接着整数x传入函数计算x['data'] + y['data']就会出错，因为整数没有下标

#   解决方法一
# 使参数一函数的返回值和参数二列表里的元素类型保持一致

#   解决方法二
# reduce还可以接收一个初始化参数，把它添加到第二个参数的序列最前面参与第一次运算
# 去掉函数get_ele_sum内参数一的下标
# 给reduce加个个初始化值参数0
# 这个0相当于加在L的第一个元素，除了第一次x等于0
# 以后x都是等于y['data']然后和下一个y['data']相加
# def get_ele_sum(x, y):
#     return x + y['data']
#
# print(reduce(get_ele_sum, L, 0))
```

## 闭包易错点

```python
def count():
    # fs里最终存的是循环创建未被调用的三个函数f
    fs = []
    for i in range(1, 4):
        # 每次循环都是在创建函数f但并没有调用
        def f():
            return i * i
        # 此时函数f并没有被调用，添加的是函数f本身，不是f的调用结果
        fs.append(f)
        # 也就是说count()得到的返回值是三个函数
    # 循环结束i为3
    return fs

print(count())

#   易错点1
# 运行print(count())你以为会输出[1,4,9]，而实际上打印了由三个函数构成的列表
# 如果要想打印[1,4,9]，应该将fs.append(f)里的f改为f()

#   易错点2
# 如果不改原代码，而是运行以下代码，结果还是1,4,9吗
# 将count()的返回值(三个函数f)分别赋给三个变量
# f1, f2, f3 = count()
# 打印调用三个函数的结果
# print(f1(), f2(), f3())
# 结果为: 9 9 9 而不是：1 4 9
# 原因是循环里i由1增加到3这个过程只创建了三个函数而未立即调用
# 函数f虽然引用了i，但当循环结束i已经变为，故返回fs时都只会取到i为3
# 综上返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量
# 如果一定要引用循环变量就再创建一个函数，用该函数的参数绑定循环变量当前的值
# 无论该循环变量后续如何更改，已绑定到函数参数的值不变：
# def count():
#     def f(j):
#         def g():
#             return j * j
#         return g
#     fs = []
#     for i in range(1, 4):
#         # f(i)立刻被执行，因此i的当前值被传入f()
#         fs.append(f(i))
#     # 虽然i的值是变化的，但是i在循环的每个值时传入f(i)被绑定给了j
#     # 故后续j不会受到i的影响
#     return fs
```

## 由round函数到浮点数的精度陷阱

`round(num, ndigits)`，返回数`num`上取整舍入精确到小数点`ndigits`位的浮点数，除非当前小数位是5，则向最近的偶数高位舍入。如round(0.5)=0，round(1.5)=2，round(2.5)=2。

另外，对浮点数执行 [`round()`](https://docs.python.org/zh-cn/3.8/library/functions.html#round) 的行为可能会令人惊讶：例如，`round(2.675, 2)` 将给出 `2.67` 而不是期望的 `2.68`。 这不算是程序错误：这一结果是由于大多数十进制小数实际上都不能以浮点数精确地表示。 请参阅 [浮点算术：争议和限制](https://docs.python.org/zh-cn/3.8/tutorial/floatingpoint.html#tut-fp-issues) 了解更多信息。

## pip工具常用命令

`pip freeze` 以 `包名==版本号` 的格式列出已下载安装的包

`pip freeze > 路径+文件名` 将`pip freeze`命令的结果存入指定文件

`pip install -r 路径+文件名` 读取指定文件里的包和版本号并安装

`pip install 包名 -i 源路径` 从指定的镜像源下载包

修改`pip`的默认下载源，在当前系统用户文件夹下的具体用户文件夹里创建一个名为`pip`的文件夹，并在里面新建一个`pip.ini`文件，写入如下代码：

```ini
[global]
index-url=https://pypi.tuna.tsinghua.edu.cn/simple/
[install]
trusted-host=pypi.tuna.tsinghua.edu.cn
```

## 关于类

### 类的访问和修改限制

如果要隐藏类的属性不被外部访问，可以在属性名前加上两个下划线`__`,在Python中，变量名如果以`__`开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问。子类也不会直接继承父类的私有属性和方法。

双下划线开头的变量并不是一定不能从外部访问，因为不能直接访问`__属性名`实际上是因为Python解释器对外把`__属性名`变量改成了`_类名__属性名`，所以，仍然可以通过`_类名__属性名`来访问`__属性名`变量。

但是强烈建议你不要这么干，因为不同版本的Python解释器可能会把`__name`改成不同的变量名。

```Python
>>> bart.__name = 'New Name' # 设置__name变量！
>>> bart.__name
'New Name'
```

表面上看，上述外部代码“成功”地设置了`__name`变量，但实际上这个`__name`变量和class内部的`__name`变量不是一个变量！内部的`__name`变量已经被Python解释器自动改成了`_Student__name`，而外部代码给`bart`新增了一个`__name`变量。

python允许直接通过实例给类添加属性和值，可以添加一个特殊变量`__slots__`来限制可以存在的属性：

```python
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称
```

使用`__slots__`要注意，会禁止创建 `__dict__` 和 `__weakref__` (除非是在 `__slots__` 中显式地声明或是在父类中可用)。`__slots__`定义的属性仅对当前类实例起作用，对继承的子类是不起作用的。除非在子类中也定义`__slots__`，这样，子类实例允许定义的属性就是自身的`__slots__`加上父类的`__slots__`。

### 类的特殊方法

[参考python官方文档](https://docs.python.org/zh-cn/3.8/reference/datamodel.html#special-method-names)

[廖雪峰python教程之定制类](https://www.liaoxuefeng.com/wiki/1016959663602400/1017590712115904)

一个类可以通过定义具有特殊名称的方法来实现由特殊语法所引发的特定操作 (例如算术运算或下标与切片)。这是 Python 实现 *操作符重载* 的方式，允许每个类自行定义基于操作符的特定行为。

### 类属性和实例属性

类属性可以通过类对象以及实例对象访问，但只能通过类对象修改。若类属性名和实例属性名相同，则当通过实例对象访问该属性名时，访问到的是对应实例属性的值。因为实例属性优先级高会屏蔽类属性，但是用类对象访问到的还是类属性。

实例属性只能通过实例对象访问。

### 实例方法、类方法与静态方法

* 实例方法：需要用到实例对象的属性，self指向调用该方法的实例对象。可以直接用实例对象调用，此时将自动把实例对象传给self，不需要显式传递self参数。也可以通过类名调用，但是不会自动给self传参，需要手动将实例对象传给self。
* 类方法：只使用类属性，定义前附加装饰器`@classmethod`，默认有一个参数`cls`，指向类对象。调用时自动将类对象传给`cls`。在类方法通过 `cls.类属性名` 使用类属性。可以直接用类名或者实例对象调用。
* 静态方法：既不使用实例对象的属性也不使用类属性。有时会定义一个类用于封装一类函数，而不需要使用实例对象，被封装的函数就会被定义成静态方法。可以直接用类名或者实例对象调用，传参取决于方法定义。

### 特殊函数super

继承父类时，若想基于父类的某个方法进行改造或者添加功能，而又不想把父类的对应方法从头写一遍，可以使用`super`函数将父类的方法关联到子类对应方法：

```python
class C(B):
    def method(self, arg):
        # super().父类对应方法(父类的参数)
        super().method(arg)
        # 上一句写法在Python3等价于如下语句
        # super(C, self).method(arg)     
```

### 多重继承

继承一个类也会继承其祖上家族所有类的属性和方法，python也允许继承多个类。若继承的多个父类中有重名的属性或方法，则从先继承的类及其家族类开始查找。若找到了，则取最先找到的值不再继续找，否则接着从下一个父类家族找，直至找到。

## 文件

### 打开模式

| 字符  | 含义                                               |
| :---- | :------------------------------------------------- |
| `'r'` | 读取（默认），文件不存在则报错                     |
| `'w'` | 写入，并覆盖原文件内容，若文件不存在则新建一个     |
| `'x'` | 排它性创建，如果文件已存在则失败                   |
| `'a'` | 写入，如果文件存在则在末尾追加，若不存在则创建一个 |
| `'b'` | 二进制模式                                         |
| `'t'` | 文本模式（默认）                                   |
| `'+'` | 打开用于更新（可读取与写入）                       |

模式可组合使用，默认模式为 `'r'` (打开用于读取文本，与 `'rt'` 同义)。 模式 `'w+'` 与 `'w+b'` 将打开文件并清空内容。 模式 `'r+'` 与 `'r+b'` 将打开文件并不清空内容。

注意慎用`'w+'`，若使用该模式打开文件后立即读会读不到内容，因为该模式会先清空原文件内容。另外，使用该模式写入内容后立即读也是空，因为写入后文件指针处于原先写的内容末尾，往下读自然是空。需要通过`file.seek(0,0)`把文件指针置于最前。`file.tell()`方法可以返回文件指针的当前位置。

### 注意

1. 使用`with`关键字访问文件更好，因为系统会自动判断时机并关闭文件，避免了忘记关闭或者因为错误而过早关闭文件。
2. 打开文件持续对其循环写入数据，可能会出现写入的数据被滞留在缓冲区而无法成功写入的情况。这时可以用文件对象的`flush`方法刷新缓存。将`print`函数的`file`参数置为以写入方式打开的文件对象可以将内容输出至对应文件，将参数`flush`置为`True`也可刷新缓存。

## json模块

`json.dumps(obj)`把python对象转换为`json`格式字符串返回，`json.loads(s)`把`json`字符串加载为python对象。

`json.dump(obj,fp)`把对象序列化为`json`流，写入文件，`json.load(fp)`读取文件，把其中的`json`文本反序列化为python对象。`fp`为一个文件流对象。

`json`默认只能序列化和反序列化常见的通用类型，比如序列化一个自定义的类对象，就会报错`TypeError`。但是你也可以定义一个将要序列化的对象转为可被`json`序列化的类型的函数，将它传给`dumps`方法的默认参数`default`。同理反序列化也可以定义相反作用的函数传给`loads`方法的`object_hook`参数。

## pickle和json的异同

pickle模块中有和json类似的`dumps()/dump()`，`loads()/load()`函数，通过它们可以将python中任意对象转换为二进制数据，并能完整地转回和原来一样的数据。不过，此类二进制格式数据需要python解释器才能良好识别，并不通用。

json格式的优势是能跨平台跨语言使用，但是只能存储常见的通用数据类型数据，而且序列化后的数据再反序列化回来得到的数据可能与原数据有差异。例如JSON 中的键值对中的键永远是 `str` 类型的。当一个对象被转化为 JSON 时，字典中所有的键都会被强制转换为字符串。这所造成的结果是字典被转换为 JSON 然后转换回字典时可能和原来的不相等。换句话说，如果 x 具有非字符串的键，则有 `loads(dumps(x)) != x`。

## 编码与解码

在内存中使用便于操作的`Unicode`标准编码，在传输和存储中使用基于`Unicode`进行优化的`UTF_8`编码。`UTF_8`兼容`Ascii`，对使用频率高的字符编短码，反之长码，节省了存储空间。

早期Unicode标准并未发布，python的代码源文件和字符串`str`默认使用`ASCII`进行编码。`python2.0`提供了一种新的存储文本数据的数据类型：`Unicode` 对象，它可以用来存储和操作 `Unicode` 数据。所以`python2`同时有`Ascii`编码的`str`和`Unicode` 字符串。到了`python3`以后`python`删除了`Unicode` 对象类型，使字符串均由`Unicode`编码，源文件默认编码也改为`UTF_8`。

在`python2.x`版本，由于源代码文件默认使用`Ascii`编码，所以无法显示中文。需要通过在源代码文件头部声明`# -*- encoding: utf-8 -*-`来使用`utf-8`编码处理源文件。

windows简体中文版系统默认使用`GB2312`来处理文本，所以python在写入和读取windows文件时要注意指明一致的编码。

对于单个字符的`Unicode`编码，Python提供了`ord(str)`函数获取字符的十进制整数表示，`chr(str)`函数把编码转换为对应的字符。`hex(x)`将整数转换为以“0x”为前缀的小写十六进制字符串，`oct(x)`将一个整数转变为一个前缀为“0o”的八进制字符串， `bin(x)`将一个整数转变为一个前缀为“0b”的二进制字符串。

`python3`提供了由单个字节构成的不可变二进制序列类型bytes，它的字面值的语法与字符串字面值的大致相同，只是添加了一个 b 前缀，`bytes` 字面值中只允许 ASCII 字符。字符串在内存中以`Unicode`表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的`bytes`。

`str.encode(coding)`方法将字符串以给定的编码规则编码成对应的`bytes`字节序列。

`bytes.decode(coding)`方法将`bytes`序列按给定规则解码成对应字符串，可以传入`errors='ignore'`忽略错误无法解码的字节。

参考文档：[廖雪峰python字符串和编码](https://www.liaoxuefeng.com/wiki/1016959663602400/1017075323632896#0)，[追本溯源：字符串及编码](https://zhuanlan.zhihu.com/p/73917931)，[编码格式与 Unicode](https://docs.python.org/zh-cn/3.8/library/codecs.html#encodings-and-unicode)，[Unicode 指南](https://docs.python.org/zh-cn/3.8/howto/unicode.html#converting-between-file-encodings)，[Python2和python3字符编码的区别](https://www.cnblogs.com/luodaoqi/p/11323828.html)，[Unicode 和 UTF-8 ](https://www.zhihu.com/question/23374078)

## 可迭代对象、迭代器与生成器

可迭代对象`Iterable`指能够逐一返回其成员项的对象。外在特征是都能通过*for*循环遍历，实质是类定义了`__iter__`方法。

迭代器`Iterator`用来表示一连串数据流的对象。重复调用迭代器的 `__next__()` 方法（或将其传给内置函数 `next()`）将逐个返回流中的项。当没有数据可用时则将引发 *StopIteration* 异常。迭代器必须具有` __iter__ `方法用来返回该迭代器对象自身，因此迭代器必定也是可迭代对象。总的来说，迭代器都能作用于`next()`函数，即都定义了 `__next__()` 方法。迭代器都是可迭代对象，但是诸如list、dict、str等类型是`Iterable`但不是`Iterator`，不过可以通过`iter()`函数获得一个`Iterator`对象。对迭代器调用`iter`函数，则会返回迭代器自身。迭代器不像list等类型一次性把所有数据确定并存储下来，迭代器是保存计算方法，再根据需要惰性计算结果。

生成器`Generator`，主要指生成器函数，一般通过在函数里添加`yield`语句创建。生成器是一个用于创建迭代器的简单而强大的工具，也就是说生成器也是迭代器。生成器较于一般的迭代器一是写法更紧凑，因为它会自动创建 [`__iter__()`](https://docs.python.org/zh-cn/3.8/reference/datamodel.html#object.__iter__) 和 [`__next__()`](https://docs.python.org/zh-cn/3.8/reference/expressions.html#generator.__next__) 方法。另一点是每次在生成器上调用 [`next()`](https://docs.python.org/zh-cn/3.8/library/functions.html#next) 获取`yield`返回的值时时，它会从上次离开的位置恢复执行（会记住上次执行语句时的所有数据值）。除了会自动创建方法和保存程序状态，当生成器终结时，它们还会自动引发 [`StopIteration`](https://docs.python.org/zh-cn/3.8/library/exceptions.html#StopIteration)。 这些特性结合在一起，使得创建迭代器能与编写常规函数一样容易。

生成器表达式：某些简单的生成器可以写成简洁的表达式代码，所用语法类似列表推导式，但外层为圆括号而非方括号。 这种表达式被设计用于生成器将立即被外层函数所使用的情况。 生成器表达式相比完整的生成器更紧凑但较不灵活，相比等效的列表推导式则更为节省内存。

```python
# for循环的本质：
# for语句会在要遍历的可迭代对象上调用 iter()
# 该函数返回一个定义了__next__()方法的迭代器对象
# 此方法将逐一访问容器中的元素
# 当元素用尽时，__next__()将引发StopIteration异常来通知终止for循环
for x in [1, 2, 3, 4, 5]:
    pass

# 实际上完全等价于下列代码：
# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break 
```

## 迭代器要点

1. 预计生成有限个元素的生成器函数如果有`return`语句，那么用for循环遍历它是无法直接拿到`return`返回的值的。需要用`try...except`语句捕获`StopIteration`异常，返回值包含在`StopIteration`的`value`中。

   在用`next(Iterator)`获取迭代器的值途中若原迭代器发生改变，指向了一个新的迭代器，那么改变后的`next(Iterator)`会忘记原迭代器而根据新迭代器从头取值。

   ```python
   it1 = iter([0, 1, 2, 3, 4, 5])
   # 两个迭代器
   it2 = iter([6, 7, 8, 9])
   print(next(it1))
   print(next(it1))
   it1 = it2
   print(next(it1))
   print(next(it1))
   # 结果为：0 1 6 7
   ```

2. 用for循环遍历迭代器时，若中途在循环体内改变该迭代器的指向，遍历的结果依然是未变之前的迭代器的结果，不会受到影响。原因是python的for循环本质上是将要遍历的可迭代对象传入`iter()`函数并将返回的迭代器绑定给一个新的变量`it`，再在while循环中不断调用`next(it)`获取迭代器`it`的值，直到遇到迭代器停止异常`StopIteration`就退出循环。在循环体中改变的是最初未传入`iter()`函数的可迭代对象的指向，而循环中本质上用到的是迭代器`it`，所以才不会对当前循环有影响。

   ```python
   it1 = iter([0, 1, 2, 3, 4, 5])
   # 两个迭代器
   it2 = iter([6, 7, 8, 9])
   
   for i in it1:
       if i > 2:
           it1 = it2
       print(i, end=' ')
   # 结果为：0 1 2 3 4 5
   # 只打印了it1的值，it1 = it2对结果未造成影响
   
   # 下面的代码时本质上等价于上面的for循环
   
   it = iter(it1)
   # 迭代器it1传入iter()，返回的还是迭代器,并绑定给了it
   while True:
       try:
           # 获得下一个值:
           x = next(it)
           if x > 2:
               it1 = it2
               # 此时改变的时it1，而循环实际使用的是it
           print(x, end=' ')
       except StopIteration:
           # 遇到StopIteration就退出循环
           break
   
   # 另外注意以下情况：
   
   l1 = [0, 1, 2, 3, 4, 5]
   l2 = [6, 7, 8, 9]
   # 这次要遍历的是可变对象——列表
   it = iter(l1)
   while True:
       try:
           x = next(it)
           if x == 2:
               l1.append(6)
               # 原列表指向不变，但内容变化，列表是可变对象
               # 变化会同步到iter引用的l1，导致返回的迭代器it也随之变化
               # 所以结果是：0 1 2 3 4 5 6
               # 若这里是 l1=l2 则改变的是指向，不会影响到it=iter(l1)
           print(x, end=' ')
       except StopIteration:
           break 
   ```

3. 迭代器在用`next()`取值途中未取完的情况下被中断了，下一次调用next()还会从中断的位置接着往下取值。

   ```python
   it1 = iter([0, 1, 2, 3, 4, 5])
   # 两个迭代器
   it2 = iter([6, 7, 8, 9])
   
   for i in it1:
       print(i, end=' ')
       if i > 2:
           break
   print('承上启下', end=' ')
   for j in it1:
       print(j, end=' ')
   # 最终结果：0 1 2 3 承上启下 4 5 
   ```

4. 有限长度的迭代器在被`list()`函数转换成列表或者for循环完全遍历等方式将数据完全获取之后将失效，再次试图访问数据得到的是空值。也就是说不能重复使用，包括赋值后指向这个迭代器的其他变量也将无法使用。

   ```python
   it1 = iter([0, 1, 2, 3, 4, 5])
   it2 = it1  # 使it2指向it1指向的内存地址存的迭代器
   
   for i in it1:
       print(i, end=' ')
       
   print('\n----分割线----')    
   
   print('it1:', list(it1))
   print('it2:', list(it2))
   # 输出结果如下：
   # 0 1 2 3 4 5 
   # ----分割线----
   # it1: []
   # it2: []
   ```

## 使用filter、lambda表达式时的闭包易错点

```Python
#   1.正确使用的情况

def not_equal(n):
    """
    绑定参数n，返回一个函数
    两个对象不相等则内层函数返回True
    """
    def lambda_func(x):
        print(f'被filter调用了，x={x},n={n}')
        return x != n
    # 相当于return lambda x : x != n
    return lambda_func

def correct_way():
    """正确的方式
    用于从序列中筛选掉指定内容并打印新序列
    """
    # 生成1,2,3,4,5,6的生成器
    g1 = (x for x in range(1, 7))
    for i in [1, 3, 5]:
        # 从g1过滤掉1,3,5
        g1 = filter(not_equal(i), g1)
        # 上一行等价于：g1 = filter(lambda x, m=i: x != m, g1)
        # 在lambda表达式内部绑定i给m,且m是第二个位置的默认参数
        # 所以不会影响到对x的赋值
    print(list(g1))

correct_way()
# 运行结果
# 被filter调用了，x=1,n=1
# 被filter调用了，x=2,n=1
# 被filter调用了，x=2,n=3
# 被filter调用了，x=2,n=5
# 被filter调用了，x=3,n=1
# 被filter调用了，x=3,n=3
# 被filter调用了，x=4,n=1
# 被filter调用了，x=4,n=3
# 被filter调用了，x=4,n=5
# 被filter调用了，x=5,n=1
# 被filter调用了，x=5,n=3
# 被filter调用了，x=5,n=5
# 被filter调用了，x=6,n=1
# 被filter调用了，x=6,n=3
# 被filter调用了，x=6,n=5
# [2, 4, 6]


#   2.错误使用的情况

def wrong_way():
    """错误的方式"""
    g2 = (x for x in range(1, 7))
    for i in [1, 3, 5]:
        def lambda_func(x):
            print(f'被filter调用了，x={x},n={i}')
            return x != i
        g2 = filter(lambda_func, g2)
        # 上一行等价于：g2 = filter(lambda x: x != i, g2)
    print(list(g2))

wrong_way()
# 运行结果
# 被filter调用了，x=1,n=5
# 被filter调用了，x=1,n=5
# 被filter调用了，x=1,n=5
# 被filter调用了，x=2,n=5
# 被filter调用了，x=2,n=5
# 被filter调用了，x=2,n=5
# 被filter调用了，x=3,n=5
# 被filter调用了，x=3,n=5
# 被filter调用了，x=3,n=5
# 被filter调用了，x=4,n=5
# 被filter调用了，x=4,n=5
# 被filter调用了，x=4,n=5
# 被filter调用了，x=5,n=5
# 被filter调用了，x=6,n=5
# 被filter调用了，x=6,n=5
# 被filter调用了，x=6,n=5
# [1, 2, 3, 4, 6]

# 	错误原因解析
# lambda表达式引用了每轮循环的会变化的变量i
# 而且filter返回的是迭代器，它不会一次性计算出所有结果
# 而是保存当时的筛选条件，在next()调用时才根据保存的条件计算
# 这里的条件就是对应时期的lambda表达式以及它的变量和执行状态
# 前面说到i随着循环变化，lambda表达式直接引用i
# 迭代器又惰性计算，类似于引用了外部变化的量却未在变量变化之前调用的函数
# 所以当循环结束，迭代器记录的所有筛选方法的i都会变成最后一个i的值
# 而正确方法在使用i的函数外套再函数是为了把i作为参数绑定给每次的筛选方法
# 这样由于是不可变对象的赋值，所以外面的i变化不会影响到被绑定的参数
```

