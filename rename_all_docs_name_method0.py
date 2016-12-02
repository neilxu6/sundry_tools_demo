# -*- coding: utf-8 -*-

#功能介绍：一次性重命名多个文件，不是文件夹哦

# 设计思路：
#1、首先遍历path指定的目录
#2、如果是文件（不是文件夹）并且文件名中不存在 ‘.’ ，也就是没有后缀名，
#3、就把这个文件加上后缀名，然后重命名

#有些细节需要注意：
#1.如果path指定的文件夹不是这个程序的所在的目录，rename函数里面的路径就必须是绝对路径，否则就会报‘WindowsError: [Error 2]’错误
#2.重命名时如果新文件名已经存在，就会报‘WindowsError: [Error 183]’ 错误，所以，新文件名最好加上一些随机字符串
#3.如果改文件名或者后缀名可以用split() 函数进行分割
#4.find函数如果找不到指定的字符串的话就会返回 ‘-1’

import os

path = '/Users/xujianfei/Desktop/'
# os.listdir方法返回path下的所有文件名
for file in os.listdir(path):
#使用os.path.isfile函数判断是否是文件，并取出所有的文件，排除文件夹的影响，该方法的参数path
#os.path.join(path,file)方法是
    if os.path.isfile(os.path.join(path,file))==True:
#find函数，表示如果文件名中
        if file.find('.')<0:

            newname=file+'rsfdjndk.jpg'
#使用os.rename()方法，进行重命名,参数是新文件名称
            os.rename(os.path.join(path,file),os.path.join(path,newname))

            print(file+'ok')
#        print file.split('.')[-1]