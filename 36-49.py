# -*- coding: utf8 -*-
# 36. 字符串
#   36.1 多行字面量
string = ('line1'
          'line2'
          'line3')
#   36.2 字符串判断
isinstance('str', basestring) # unicode 和 str 是 basestring 的子类
#   36.3 性质判断
string.isalnum()
string.isalpha()
string.isdigit()
string.islower()
string.isupper()
string.isspace()
string.istitle()
string.startswith('line', 0, 10)
#   36.4 查找替换 foo(sub[, start[, end]])
string.count('line')
string.find('line')
string.index('line')
string.rfind('line')
string.rindex('line')
#   36.5 replace(old, new[,count]) # 注意不指定是全部替换!
string.replace('line', 'LINE', 2)
#   36.6 切分
string.partition('sep') # return ('before', 'sep', 'after')
string.split() # 默认按\b+分,
#   36.7 变形
string.title().upper().lower().capitalize().swapcase()
#   36.8 删除
string.strip().lstrip().rstrip()
#   36.9 填充 foo(width[, fillChar])
string.center(50).ljust(50).rjust(50).zfill(50).expandtabs()

# 37. sort() sorted() 推荐 key 方式
l = [3, 4, 3, 6, 5, 9, 1, 0]
l.sort(cmp = lambda a, b: a - b, reverse = False)
newList = sorted(l, key = lambda x: -x, reverse = True) # l is not changed
# sorted 可以排任何可迭代对象

# 38. 深拷贝浅拷贝
a = {'a1': 1, 'a2': {'a3': 2}}
b = a # id(b) == id(a)
import copy
b = copy.copy(a) # 单层浅拷贝 b = Object.assign({}, a)
b = copy.deepcopy(a) # 深拷贝

# 39. 计数 default data
from collections import defaultdict
dic = defaultdict(int)
dic['key'] += 1
from collections import Counter
counter = Counter([1,6,3,4,3,2,4,1,4,3,2,1])
print counter
counter.most_common(2)
counter.update([1,2,3,2,1])

# 40. config parser
import ConfigParser
conf = ConfigParser.ConfigParser()
# conf.read('filename') # 这里的配置文件方式并不好,采用的节配置,参考书P99
# 可以考虑自己实现一个基于模块的配置覆盖系统

# 41. argparse 处理命令行参数
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-o', '--output')
parser.add_argument('-v', dest='verbose', action='store_true')
parser.add_argument('-bar', type=argparse.FileType('w'))
args = parser.parse_args()

# 42. pandas 处理 CSV
# 42.1 naive
import csv
with open('data.csv', 'wb') as csvfile:
  csvWriter = csv.writer(csvfile, dialect='excel', delimiter=',',
                         quotechar='"', quoting=csv.QUOTE_MINIMAL)
  csvWriter.writerow(['sj_mino1001.jpg', '451921', 'C4E80463'])
  csvWriter.writerow(['sj_mino1002.jpg', '451922', 'C4E80464'])
  csvWriter.writerow(['sj_mino1003.jpg', '451929', 'C4E80467'])
# csv.DictReader
# csv.DictWriter
# 42.2 pandas
import pandas as pd
dataFrame = pd.read_csv('data.csv', nrows=5, usecols=range(0, 3)) # 避免文件过大
print dataFrame

# 43. xml
import xml.etree.ElementTree as ET
tree = ET.ElementTree(file='data.xml')
root = tree.getroot()

# 44. 序列化,数据存文件pickle
import cPickle as pickle
with open('pickle.dat', 'wb') as fp:
  pickle.dump({'k': 'v'}, fp) # 相反 load(fp)

# 45. json 更小,慢,支持类型少

# 46. 栈信息
import traceback
traceback.print_exc()

# 47. logging
import logging
logging.basicConfig(
  level=logging.DEBUG
  # format =
)
logger = logging.getLogger(__name__)
logger.info('msg')

# 48. 多线程
import threading

# 49. 队列
import Queue
