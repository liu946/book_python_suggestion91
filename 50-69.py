# coding=utf-8

# 50. 单例模式
#   50.1 单例类
class Singleton(object):
  _instance = None
  def __new__(cls, *args, **kwargs):
    if not cls._instance:
      cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)

      return cls._instance
#   50.2 使用模块实现,与js一致 推荐

# 51. 对继承类的动态扩展 __base__   (Mixin模式)
def automatic_extend(cls, extend_cls):
  instance = cls()
  instance.__base__ += (extend_cls,)
  return instance

# 52. 发布订阅
from collections import defaultdict
route_table = defaultdict(list)
def sub(topic, callback):
  return route_table[topic].append(callback) \
    if callback not in route_table[topic] else None
def pub(topic, *args, **kwargs):
  return [func(*args, **kwargs) for func in route_table[topic]]
# python 模块 message

# 53. 状态模式
#   state 库提供简单状态机

# 54. 新式类与久类型 todo

# 55. __init__()
#   __new__(cls[, args]) 是构造方法
#   __init__(self[,args]) 是初始化方法
class A(object):
  def __new__(cls, *args, **kwargs):
    print '[A.__new__] called'
    # no return
    # normally
    # return super(A, cls).__new__(cls)
  def __init__(self):
    # no call
    print '[A.__init__] called'
a = A()

#   55.1 继承基础不可变类型, 工厂模式

# 56. 全局(), 局部, 嵌套(动态链), 内置()
print globals()
print locals()
# 使用 global 声明外部变量
# 57. self 参数

# 58. 多继承
# 新式类 继承列表从前往后找成员，避免菱形继承
# 其实多继承的意义也没有那么大，不使用完全没有问题。


# 59. 点. 描述符
# 60. __getattr__() __getattribute__()
#   getattribute 无条件调用，没有找到触发AttributeError
#   异常调用__getattr__()用来承接没有的属性调用
#   注意无穷递归问题

# 61. 使用property
class Screen(object):
  def __init__(self):
    self._w = 1

  @property
  def width(self):
      return self._w
  
  @width.setter
  def width(self, w):
      self._w = w

  @width.deleter
  def width(self):
    del self._w

# 62. 元类
#   js中使用元类，元函数的例子也很多，比如debug，以下举几个例子好了

class Singleton(object):
  def __init__(cls, name, bases, dic):
    super(Singleton, cls).__init__()
    cls.instance = None

  def __call__(cls, *args, **kwargs):
    """调用Singleton()时调用的函数"""
    if cls.instance is None:
      print 'create a new instance'
      cls.instance = super(Singleton, cls).__call__(*args, **kwargs)
    else:
      print 'already created an instance'

    return cls.instance

class SingletonClass(object):
  """docstring for SingletonClass"""
  __metaclass__ = Singleton
  def __init__(self, arg):
    super(SingletonClass, self).__init__()
    self.arg = arg
    
# 63. 对象协议，重载机制
class ClassName(object):
  def __init__(self, arg):
    '''初始化方法'''
    self.arg = arg
  def __str__(self):
    '''字符串化方法'''
    pass
  def __repr__(self):
    '''代码序列化方法'''
    pass
  def __init__(self):
    '''转换方法'''
    pass
  def __long__(self):
    '''转换方法'''
    pass
  def __float__(self):
    '''转换方法'''
    pass
  def __nonzero__(self):
    '''转换方法'''
    pass

  def __eq__(self, that): # ne, lt, gt
    pass
  def __cmp__(self, that): # return self - that
    pass
  # 数值运算重载
  # add,sub,mul,div,floordiv(//)...

# 64. pipe库的使用，中缀用法，惰性求值
from pipe import *
[1,2,3,4,5] | where(lambda x: x % 2) | select(lambda x: x * x)

# 65. 迭代器协议

class Fib(object):
  def __init__(self, arg):
    self.a = 0
    self.b = 1
  def __iter__(self):
    return self
  def next(self):
    self.a, self.b = self.b, self.a + self.b
    return self.a

# 66. 生成器
def generatorFunction(value):
  sum = value
  while True:
    sum += (yield sum) 

generator = generatorFunction(1)
generator.next() # return 1, 第一次必须使用next调用
generator.send(2) # return 3
generator.send(3) # return 6
# generator.throw(type,msg) 可将异常抛入生成器

# 67. 生成器协程 greenlet

# 68. GIL 全局解释器锁
# 多进程编程尽量使用multiprocessing模块实现，绕过GIL

# 69. 引用计数
# 使用 gc.collect() 进行回收
