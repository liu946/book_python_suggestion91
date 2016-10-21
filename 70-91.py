# coding=utf-8

# 70. PyPI
# 71. pip yolk
# 72. distutils 构建,打包,发布PyPI
#   建立 setup.py 文件
from distutils.core import setup
setup(name='modelname',
      version='1.0',
      py_modules=['modelname'],
      )
#   使用 python setup.py install 安装到系统中
#   包项目初始化工具: pastescript(paster)
# 打包命令 $ paster create -o packageName -t basic_package originPackageDir

# 73. UnitTest
# pyUnit

# 74. 为包编写测试


# 75. TDD 测试
import unittest
class Test(unittest.TestCase):
  def test_int(self):
    self.assertEqual(sum([0, 1, 2]), 3)

if __name__ == '__main__':
  unittest.main()

# 76. pylint
# 77. 代码审查
# 78. pypi
# 79. 代码优化

# 80. 性能优化工具 Psyco, Pypy

# 81. cProfile
import cProfile
cProfile.run('someFunction()') # python -m cProfile file.py

# 82. profiler
import memory_profiler
@memory_profiler.profile
def someFunction():
  return sum(range(1, 100))


# 83. 减低算法复杂度 哦

# 84. 循环优化
import math
local_sin = math.sin # 尽量使用内部变量
for i in xrange(len([])): # 迭代器
  pass

# 85. 使用生成器 之前提过了, 略

# 86. 数据结构性能优化
# 少拷贝,多引用

# 87. set 速度比 list 快
seta = {1, 2, 3}
setb = {3, 4, 5}
seta.union(setb) # V
seta.intersection(setb) # ^
seta.difference(setb) # a-b
seta.symmetric_difference() # a ^ b


# 88. multiprocessing 克服 GIL 缺陷
from multiprocessing import Process, Pipe, Queue

# 89. 线程池 
# import threadpool

# 90. C/C++接口
# 用到再看

# 91. Cython 一个python模块，将python编译为C代码
# 可以引用C的函数，提高代码性能
# 