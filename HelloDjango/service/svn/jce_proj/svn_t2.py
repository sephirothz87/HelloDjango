# -*- coding:utf-8 -*-
import os
import locale
import subprocess
import sys
import difflib
import time, datetime

v1 = '38592'
# v2 = '37442'

cmdDiff = 'svn diff -r'
# diffFile = 'diff/tmp1.diff'
command = cmdDiff+v1
# command = 'python --version'


print(command)

# res = os.popen(command)

# res = os.popen(command,'r').read()

# command = command.encode(locale.getdefaultlocale()[1])
# res = subprocess.Popen(command)
res = subprocess.Popen(command,stdout=subprocess.PIPE, stderr=subprocess.STDOUT,bufsize=1)

# res.wait()

# print (sys.getdefaultencoding())

# print(type(res))
# print(res.read())


timeTag = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
f = open('diff/'+timeTag+'.diff', 'wb')
count = 0
line = res.stdout.readline()
while line:
	# print(count)
	print(line)
	f.write(line)
	line = res.stdout.readline()
	count+=1
f.close()

print('over')


