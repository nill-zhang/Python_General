#!/usr/bin/python
#-*-coding = UTF-8-*-
import os
from os.path import join, getsize
t = open('E:/walk.txt','w')
for root, dirs, files in os.walk('D:/work'):
    t.write('###################################################################\n')
    t.write('root:'+repr(root)+'\n')
    t.write('dirnames:'+repr(dirs)+'\n')
    t.write('files:'+repr(files)+'\n')
t.close()