# -*- coding:utf-8 -*-
import os
import locale
import subprocess
import sys

 

v1 = '37441'
v2 = '37442'

cmdDiff = 'svn diff -r'
command = cmdDiff+v1+':'+v2
# command = 'python --version'

print(command)

# res = os.popen(command)

# res = os.popen(command,'r').read()

# command = command.encode(locale.getdefaultlocale()[1])
# res = subprocess.Popen(command)
res = subprocess.Popen(command,stdout=subprocess.PIPE, stderr=subprocess.STDOUT,bufsize=1)

# res.wait()

print (sys.getdefaultencoding())

# print(type(res))
# print(res.read())

count = 0
line = res.stdout.readline()
while line:
	print(count)
	print(line)
	line = res.stdout.readline()
	count+=1


print('over')


