# Python语言学习

## Python两大特性
1. 动态语言
    - 要了解什么是动态语言，要首先了解“类型检查”。类型检查是验证类型约束的过程，编译器或解释器通常在编译阶段或运行阶段做类型检查。
    - 类型检查发生在程序运行阶段（run time），那么它便是“动态类型语言”（dynamically typed languages）
2. 强类型语言
    - 强类型语言是指：不管是在编译阶段还是运行阶段，一旦某种类型绑定到变量后，此变量便会持有此类型，并且不能同其他类型在计算表达式时，混合使用。
    ```
    >>> a=5
    >>> b='hello'
    >>> c=a+b
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    ```
   返回错误：不支持int变量和str变量相加
   
## 四大基本语法
### 命名规则
Python 的变量命名规则主要包括两条：
- 允许包括英文、数字以及下划线（_），不能以数字开头
- 名称区分大小写

特别说明以“下划线”开头的变量是有特殊意义的：
- 类变量若以单下划线（_）开头，代表不能直接被访问，类似于 C# 的受保护型变量（protected），表示不能通过 import module_name 而导入。
- 类变量若以双下划（__）开头，表示为类的私有成员，不能被导入和其他类变量访问。
- 以双下划开头和双下划线结尾的变量是 Python 里的专用标识，有特殊的身份。

如 Python 自定义类中都包括 __init__ 和 __add__ 方法，如果不重写 __add__ 去执行两个类加法操作，程序会抛 TypeError 异常。只有重写后，程序才能正常执行加法操作。

Python 变量命名习惯一般遵守蛇形命名法（snake case）：
- 一般变量命名，book_id、book_store_count；
- 类名首字符为大写，如 Python 内置模块 collections.abc 中的 Iterable 类、我们自定义的Book类等；
- 类方法名：get_store_count()；
- 其他特殊变量，会全部大写，M_PI、MAX_VEHICLE_SPEED。

### 缩进原则
Python最具特色的地方就是用缩进代替Java、C++ 中的{}，缩进的层级结构表示代码的逻辑层次。

Python的缩进方法，一般为4个字符。

定义一个Book类
```
class Book(object):
    # 定义类的参数
    def __init__(self, book_id, book_name, book_store_count):
        self.book_id = book_id
        self.book_name = book_name
        self.book_store_count = book_store_count

    # 重写加法操作
    def __add__(self, book):
        return self.book_store_count + book.book_store_count


# 创建两个Book类的实例
python_intro_book = Book(1, 'python入门学习', 100)
ml_intro_book = Book(2, '机器学习入门', 200)

# 求两本书的总销量
sales_cnt = python_intro_book + ml_intro_book
print(sales_cnt)
```
- 代码行`class Book(object)`与代码行 # 定义类的参数 的缩进，此处为 4 个字符；
- 代码行`def __add__(self,book)`: 与 return 所在行缩进也是 4 个字符。

缩进格式、行间空行数、变量和等号空格等 Python 编码规范参考PEP8。

autopep8包遵循PEP8的所有规范，安装此包，做好相关配置，便可自动实现PEP8制定的编码规范。

### 特殊关键字
Python有35个关键字：
```
False      await      else       import     pass
None       break      except     in         raise
True       class      finally    is         return
and        continue   for        lambda     try
as         def        from       nonlocal   while
assert     del        global     not        with
async      elif       if         or         yield
```
自定义变量名不能与它们重复。

常用且不同于其他常用语言C++和Java的关键字，如：
- True和False用于表示值的真假，在Java中是true和false；
- 逻辑反操作Python使用not，Java是!；
- None表示空值，Java使用null；
- Python两个条件同时满足使用and，Java是&&；
- 两者满足其一，Python使用or，Java使用||；
- Python使用elif， Java是else if。

其他比较特殊的关键字，如：
- del用于删除可迭代对象中某个元素；
- def用于定义函数；
- 带yield用于定义生成器（generator）函数；
- global和nonlocal一种应用是Python函数式编程的闭包场景；
- pass一种应用是定义接口，也是Python语言特有的一个关键字。

### 特殊运算符
Python的运算符包括：
```
+       -       *       **      /       //      %      @
<<      >>      &       |       ^       ~       :=
<       >       <=      >=      ==      !=
```
3个比较特殊的：//、**、:=
- // 用于两个数值相除且向下取整，与Python的math模块中floor功能相似
    ```
    >>> 5 // 2
    2
    >>> 5 // 4.5
    1.0
    ```
- ** 用于幂运算：
    ```
    >>> 2**3
    8
    ```
- := 是在2019年，Python 3.8版本里，刚刚才被支持的运算符，被形象地称为“海象运算符”。
    ```
    a = 'Jean, how are you!'
    n = len(a)
    if n > 10:
        print(f"{n}大于10")
    
    # 海象运算符
    if (n := len(a)) > 10:
        print(f"{n}大于10")
    ```

Python比较运算符还支持链式比较，应用起来更加方便
```
>>> i=3
>>> print(1<i<3)
False
>>> print(1<i<=3)
True
```

注意：运算符@是用于装饰器功能

## Python四大数据类型
### 1. 数值型
Python中的数据皆是对象，比如被熟知的int整型对象、float双精度浮点型、bool逻辑对象，它们都是单个元素
- 前缀加`0x`，创建一个十六进制的整数：
    ```
    >>> 0xa5
    165
    ```
- 使用`e`创建科学计数法表示的浮点数：
    ```
    >>> 1.05e3
    1050.0
    ```
### 2. 容器型
可容纳多个元素的容器对象，常用的比如：list列表对象、 tuple元组对象、dict字典对象、set集合对象。Python定义这些类型的变量，语法非常简洁。
- 数组：list
    - 使用一对中括号`[]`，创建一个 list 型变量
- 元组：tuple
    - 使用一对括号`()`，创建一个 tuple 型对象, 但需要注意，含单个元素的元组后面必须保留一个逗号，才被解释为元组， 否则会被认为元素本身
- 字典：dict
    - 使用一对花括号 {} 另使用冒号 :，创建一个 dict 对象。字典是一个哈希表
- set对象
    - 仅使用一对花括号 {}，创建一个 set 对象
### 3. 字符串
所有的字符或串都被统一为str 对象，如单个字符c的类型也为str。
### 4. 自定义类型
Python使用关键字class 定制自己的类，self表示类实例对象本身

一个自定义类内包括属性、方法，其中有些方法是自带的
#### 类（对象）
```
class Person(object):
    pass
```
以上定义一个Person对象，它继承于根类object，pass表示没有自定义任何属性和方法。

使用 __dir__()查看类自带方法
```
['__module__',
 '__dict__',
 '__weakref__',
 '__doc__',
 '__repr__',
 '__hash__',
 '__str__',
 '__getattribute__',
 '__setattr__',
 '__delattr__',
 '__lt__',
 '__le__',
 '__eq__',
 '__ne__',
 '__gt__',
 '__ge__',
 '__init__',
 '__new__',
 '__reduce_ex__',
 '__reduce__',
 '__subclasshook__',
 '__init_subclass__',
 '__format__',
 '__sizeof__',
 '__dir__',
 '__class__']
```
有些地方称以上方法为魔法方法，它们与创建类时自定义个性化行为有关。比如：
- `__init__`方法能定义一个带参数的类；
- `__new__`方法自定义实例化类的行为；
- `__getattribute__`方法自定义读取属性的行为；
- `__setattr__`自定义赋值与修改属性时的行为。

#### 类的属性：
```
def __init__(self, name, age):
    self.name = name
    self.age = age
```
通过`__init__`，定义Person对象的两个属性：name，age

#### 类的实例
```
zhangsan = Person('zhangsan', 25)
```
zhangsan是Person类的实例

#### 类的方法
```
def say(self):
    print('My name is %s.I\'m %s' % (self.name, self.age))
```

注意：
- 自定义方法的第一个参数必须是self，它指向实例本身，如Person类型的实例person；
- 引用属性时，必须前面添加self，比如self.name等。

总结整个类的代码
```
class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        print('My name is %s.I\'m %s.' % (self.name, self.age))


# 创建对象
zhangsan = Person('zhangsan', 25)
# 调用方法
zhangsan.say()
```
看到创建的两个属性和一个方法都被暴露在外面，可被zhangsan调用。这样的话，这些属性就会被任意修改：
```
# 获取对象的属性
print(zhangsan.name)
print(zhangsan.age)

# 篡改对象的内容
zhangsan.name = 'wangxiaoer'
print(zhangsan.name)
```

如果想避免属性name被修改，可以将它变为私有变量。改动方法：属性前加2个`_`后，变为私有属性。如：
```
class Person(object):

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def say(self):
        print('My name is %s.I\'m %s.' % (self.__name, self.__age))
```
这时，在调用获取对象属性就会报错
```
# 获取对象的属性
print(zhangsan.name)

...
AttributeError: 'Person' object has no attribute '__name'
```
但是这样改动后，属性name不能被访问了，也就无法得知zhangsan的名字叫啥。不过，这个问题有一种简单的解决方法，直接新定义一个方法就行：
```
class Person(object):

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def say(self):
        print('My name is %s.I\'m %s.' % (self.__name, self.__age))
```
通过此机制，改变属性的可读性或可写性，怎么看都不太优雅！因为无形中增加一些冗余的方法，如get_name

通过另一种方式，可以更优雅地改变某个属性为只读或只写

使用Python自带的property类，就会优雅地将name变为只读的。使用@property装饰后name变为属性，意味着 .name就会返回这本书的名字，而不是通过 .name() 这种函数调用的方法。这样变为真正的属性后，可读性更好。
```
class Person(object):

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    def say(self):
        print('My name is %s.I\'m %s.' % (self.__name, self.__age))


# 创建对象
zhangsan = Person('zhangsan', 25)
zhangsan.say()

# 获取对象属性
print(zhangsan.name)
```
如果使name既可读又可写，就再增加一个装饰器 @name.setter
```
class Person(object):

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    def say(self):
        print('My name is %s.I\'m %s.' % (self.__name, self.__age))

# 修改属性
zhangsan.name = 'wangxiaoer'
print(zhangsan.name)
```
注意这种装饰器写法：name.setter，name已经被包装为property实例，调用实例上的setter函数再包装name后就会可写。



## list和tuple的基本操作

### 列表（list）

列表（list）作为 Python 中最常用的数据类型之一，是一个可增加、删除元素的可变（mutable）容器。

#### 基本操作

##### 创建

创建 list 的方法非常简单，只使用一对中括号 `[]`

```python
empty = []
arr1 = [1,'huahua',36.5,'18612341234']
arr2 = ['007','2020-09-01',['三文鱼','金枪鱼']]
```

##### len

内置函数len，求 list 内元素个数

```python
>>> len(empty)
0
>>> len(arr1)
4
>>> len(arr2)
3
```

##### type

内置函数type，获取类型

```python
>>> type(empty)
<class 'list'>
```

##### 遍历列表

```python
for _ in arr1:
    print(f'{_}的类型为{type(_)}')
```

输出结果：

```
1的类型为<class 'int'>
huahua的类型为<class 'str'>
36.5的类型为<class 'float'>
18612341234的类型为<class 'str'>
```

因此，Python 的列表不要求元素类型一致

##### 增加/移除元素

如何向arr2中的`['三文鱼','金枪鱼']`中增加一个元素'神户和牛'呢？

```python
# 使用“整数索引”取出这个元素
>>> food = arr2[2]
# 使用列表的append方法增加元素，append默认增加到food列表尾部
>>> food.append('神户和牛')
```

此时，想在food指定的索引处，插入数据

```python
# 使用insert，在指定索引1处插入'鲔鱼'
>>> food.insert(1,'鲔鱼')
```

这时，又不想要'神户和牛'，需要将'神户和牛'移除

```python
# 使用pop方法可直接移除列表尾部元素
>>> item = food.pop()
>>> print(item)
神户和牛
>>> print(food)
['三文鱼', '鲔鱼', '金枪鱼']
```

因为，pop只能移除列表的尾部元素，这时还想移除'三文鱼'

```python
# 使用remove方法移除指定的元素
>>> food.remove('三文鱼') # 更好用：food.remove(food[0])
>>> print(food)
['鲔鱼', '金枪鱼']
```



#### 深浅拷贝

##### 浅拷贝

经过一系列对arr2的操作后，food引用arr2的第三个元素，food指向的内存区域改变，所以arr2也会相应改变

```python
>>> print(arr2)
['007', '2020-09-01', ['鲔鱼', '金枪鱼']]
```

如果不想改变arr2中的元素，就需要复制出arr2的这个元素，列表中`copy`方法可实现复制：

```python
>>> arr2 = ['007','2020-09-01',['三文鱼','金枪鱼']]
>>> print(arr2)
['007', '2020-09-01', ['三文鱼', '金枪鱼']]
>>> food_deep = arr2[2].copy()
>>> print(food_deep)
['三文鱼', '金枪鱼']
```

注意，copy 函数，仅仅实现对内嵌对象的一层拷贝，属于 shallow copy（浅拷贝）。

因为拷贝arr2[2]，所以food_deep位于栈帧中指向一块新的内存空间：

此时，在对food_deep操作，便不会影响到arr2[2]的值。

```python
>>> food_deep[0] = '神户和牛'
>>> print(food_deep)
['神户和牛', '金枪鱼']
>>> print(arr2[2])
['三文鱼', '金枪鱼']
```

因为它们位于不同的内存空间中，所以food_deep中操作，并不影响arr2[2]



至此，仅仅使用 shallow copy。那么，它与深拷贝，英文叫 deepcopy，又有什么不同？

请看下面例子，a 是内嵌一层 list 的列表，对其浅拷贝生成列表 ac，修改 ac 的第三个元素，也就是列表 [3,4,5] 中的第二个元素为 40：

```python
>>> a = [1,2,[3,4,5]]
>>> ac = a.copy()
>>> ac[0] = 10
>>> ac[2][1] = 40
>>> print(ac)
[10, 2, [3, 40, 5]]
```

修改后，分别测试两个值的相等性。

```python
>>> print(a[0] == ac[0])
False
```

返回 False，证明实现拷贝。

而 `ac[2][1]`是否与原数组 a 的对应位置元素相等：

```python
>>> print(a[2][1] == ac[2][1])
True
```

返回 True，进一步证明是浅拷贝，不是深拷贝。

copy 只完成了一层 copy，即 [1,2, id([3,4,5])] 复制一份，而复制后，仍然指向 [3,4,5] 所在的内存空间

##### 深拷贝

```python
from copy import deepcopy

a = [1, 2, [3, 4, 5]]
ac = deepcopy(a)
ac[0] = 10
ac[2][1] = 40
print(a[0] == ac[0])
print(a[2][1] == ac[2][1])
```

执行结果：

```
False
False
```

内嵌的 list 全部完成复制，都指向了不同的内存区域。



