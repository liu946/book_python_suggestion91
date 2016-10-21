# -*- coding: utf8 -*-
# 18. 包管理
#   18.1 文件夹/文件树管理
#   18.2 __init__.py 用来导入文件夹级别(模块级别)的内容
#     __all__ = ['PackageNames'] # to import *

# 19. import
#   19.1 优先 import model 使用 model.func
#        有节制 from model import func 直接使用 func
#        避免 from model import *
#   19.2 使用 import model 解决循环引用问题

# 20. 相对import (不推荐使用)

# 21. 无++运算符

# 22. 使用 with
#   22.1 上下文管理对象方法 __enter__() 和__exit__()
#   22.2 运行步骤和异常见书 P51
with open('testingFile.txt', 'r') as f:
  print f.read().decode('utf-8')

# 23. else 子句
#   23.1 循环的 else子句
#     在循环条件结束时执行一次
for i in xrange(2, 100):
  for j in xrange(2, i):
    if i % j == 0:
      break
  else:
    print '%d is prime' % i

#   23.2 try except 中的 else
try:
  f = open('config.file')
except:
  # some code use other configs
  pass
else:
  config = f.read().decode()
  f.close()

# 24. try except
try:
  pass
except EOFError:
  pass
except AssertionError:
  pass
except (BufferError, EnvironmentError):
  pass
except FloatingPointError as data:
  pass
except:
  pass
else:
  pass
finally:
  pass

# 25. finally 的坑
#   25.1 finally中执行break和return语句,不会上抛异常
#   25.2 finally会抢先在return之前执行,如果其中return则覆盖之前的return

# 26. bool表达式隐式转换
#   False : None, False, 0, 0.0, 0j, '', (), {}, [], len(obj) == 0
#   重载函数 : __nonzero__() 缺省为True

# 27. join
','.join(['str1', 'str2', 'str3'])

# 28. format 推荐使用
# {索引[,][[填充]对齐][符号][#][0][宽度][,][.精度][类型]}
'{0:s}'
'{key:,}' # 12,103
'{0[0]:#x}' # hex

# 29. 函数默认值是固定对象,下次调用不重新赋值 !!! 注意这反人类设计
def foo(a = []):
    a.append(1)
    return a

foo() # [1]
foo() # [1, 1]

# 30. [] {} 和 ()
# 逻辑 + 解构: 更方便的map函数,甚至加入了我一直想加入的元素删除功能
singleNumberList = [i for i in range(1, 10) if i % 2]
# 本人最喜欢的一个99乘法表版本, 虽然可读性并不是很好. 还是习惯node的join...
print '\n'.join([', '.join(['{0} * {1} = {2:2}'.format(j, i, i * j) for j in range(1, i + 1)]) for i in range(1, 10)])
singleNumberSet = {i for i in range(1,10) if i % 2} # set
isSingleNumberDict = dict({(str(i), bool(i % 2)) for i in range(1, 10)})

# 转置
matrix = [[1, 2, 3, 4], [2, 4, 6, 8], [3, 6, 9, 12]]
transposed = [list(row) for row in zip(*matrix)]

# 31. 函数参数传递,与js,java相同

# 32. 函数参数坑, 之前提过一次了, 默认参数在def时计算

# 33. 慎用变长参数
def foo(a, *arg, **kwargs):
  pass
foo(1, *[1], **{'k': 'v'})
# 常使用在 装饰器结构 或 重载调父类方法上
def decorator(foo):
  def new(*args, **kwargs):
    pass
    return foo(*args, **kwargs)
  return new

# 34 str() repr() 后者用于生成这个对象
obj = {'k': 'v'}
sameObj = eval(repr(obj)) # 实现__repr__()方法保证这条代码的运行

# 35 staticmethod 和 classmethod
class C(object):
  attribute = 0 # 类变量,类级共享空间, 子类继承之后有一个不同的空间存储
  def __init__(self):
    self.attr = 1 # 对象属性

  def instance_method(self, x):
    pass

  @classmethod # 类方法
  def class_method(cls, x): # cls传入的可能是子类
    cls.attribute += 1 #
    pass

  @classmethod # 类方法, 工厂模式中也常用
  def function_mechod(cls, x):
    return cls() # 有可能构造子类对象

  @staticmethod # 静态方法
  def static_method(x):
    pass


