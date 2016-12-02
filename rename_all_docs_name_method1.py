# -*- coding: utf-8 -*-

#功能介绍：一次性重命名多个文件，不是文件夹哦

import os
from findtools.find_files import (find_files, Match)


path='/Users/apple/node/test'
found_files = find_files(path)

for found_file in found_files:
    print(found_file)
    newname=found_file.replace('str1','')
    os.rename(os.path.join(path,found_file),os.path.join(path,newname))
    print (found_file+'ok')

