#!/usr/bin/env python

import os
import re

path = r'./file'

"""
批量修改文件名 Zoe
"""
for (path, dirs, files) in os.walk(path):
    for filename in files:
        fore = filename.split('.')[0]
        tail = filename.split('.')[-1]
        # print(fore,tail)
        fore = re.sub(r"\W+", "_", fore)
        newname = fore + '.' + tail
        # print(filename)
        os.rename(path + '/' + filename, path + '/' + newname)
