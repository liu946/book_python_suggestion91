#! /usr/local/bin/python
# -*- coding: utf8 -*-
import django
# 1. pythonic
#   1.1 伪代码风格
#   1.2 元组赋值,in遍历,迭代器,安全关闭with
#   1.3 print 参数

print 'Hello %(name)s!' % {'name': 'Tom'}
print 'Hello {name}!'.format(name = 'Tom')

# 2. python代码
#   2.1 明确完整变量名
#   2.2 风格检查 pep8 $ pip install -U pep8

# 3. python特异性
#   3.1 x if boolean else y
#   3.2 无 switch 用 elif 或跳转表

# 4. 注释
#   4.1 """注释"""
# 5. 空格使用,避免长行
# 6. 函数
#   6.1 层次不大于3 ```python尤其注意,因为python的层次往往很难看清```
#   6.2 与名称粒度一致, 尽量用默认参数扩展行为
# 7. 常量集中,配置文件
# 8. 断言
# 9. 解构,交换值
# 10. lazy load
#   10.1 yield

# 11. 枚举
# 12. 检查类型
isinstance('a', (str, unicode))
# 13. 除法是C规则,先转float
# 14. eval滥用
# 15. 迭代序列
li = ['a', 'b', 'c', 'd', 'e']
for i in li:
  print i,

for i in range(len(li)):
  print '(%d, %s) ' % (i, li[i]),

for i,e in zip(range(len(li)), li):
  print '(%d, %s) ' % (i, e),

for i, e in enumerate(li):
  print '(%d, %s) ' % (i, e),

dic = {'name': 'Jon', 'age': 20, 'hobby': 'football'}
for k, v in dic.iteritems():
  print k, " : ", v

# 16. == 与 is
# 17. 编码
#    17.1 文本文件编码
''.decode('utf-16') # utf-16 => unicode
'unicode string'.encode('utf-16') # unicode => utf-16

file = open('testingFile.txt')
(file.read().decode('utf-8')).encode('gbk')
file.close()

import codecs
content = open('testingFile.txt').read()
if content[:3] == codecs.BOM_UTF8: # BOM?
  content = content[3:]
print content.decode('utf-8')
#   17.2 python file coding
#     coding[:=]\s*([-w.]+)
#     coding=utf-8
#     from __future__ import unicode_literals # 自动使用unicode字符串


