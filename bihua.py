# -*- coding: utf-8 -*-
"""
Created on Sun May 13 20:44:37 2018

@author: zpeng
"""

#!/usr/bin/env python
# -*- coding: UTF-8 -*-

data_lines = open(u'汉字编码表 gbk unicode.txt').readlines()

query_dict = {}

for line in data_lines[7:]:  # 去掉头部无用信息
    l = line.strip().split()
    unicode_mark = chr(int(l[4], 16))
    bihua = l[6]
    query_dict[unicode_mark] = bihua

print(u'收录汉字个数:', len(data_lines))

for s in u'王懿宸':
    print(s, query_dict.get(s, -1))

