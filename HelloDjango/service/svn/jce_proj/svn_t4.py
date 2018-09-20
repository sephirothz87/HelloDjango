#coding:utf-8
import os
import locale
import subprocess
import sys
import time
import datetime
import threading
import re

#5.3基线
vBase = '38111'
#最新版本号
# vLatest = ''
vLatest = ''

cmdUpdate = 'svn update'
cmdDiff = 'svn diff -r'

reReversion = r'\d+'

def loop():
	print('loop start')

	n = 0
	#单次测试
	while n<1:
	#测试2
	# while n<1000:

		print('n =',n)
		n = n+1
		
		resUpdate = subprocess.Popen(cmdUpdate,stdout=subprocess.PIPE, stderr=subprocess.STDOUT,bufsize=1)
		# resUpdateTxt = resUpdate.stdout.read()
		# print(resUpdateTxt)
		
		lastLine = ''
		line = resUpdate.stdout.readline()
		while line:
			lastLine = line
			line = resUpdate.stdout.readline()
		print(lastLine)
		lastLine=lastLine.decode('utf-8')
		matchObj = re.search(reReversion,lastLine, flags=0)
		# print(matchObj.group(1))
		print(matchObj.group())

		reversion = matchObj.group()
		global vLatest
		if vLatest == '':
			vLatest = reversion
		
		print(vLatest)

		#对比版本号，一致则不diff
		# if reversion != vLatest:
		#测试
		if 1:
			print('find new reversion')

			# 与前一个版本对比
			# resDiff = subprocess.Popen(cmdDiff+vLatest+':'+reversion,stdout=subprocess.PIPE, stderr=subprocess.STDOUT,bufsize=1)

			#与基线版本对比
			resDiff = subprocess.Popen(cmdDiff+vBase+':'+vLatest,stdout=subprocess.PIPE, stderr=subprocess.STDOUT,bufsize=1)
			
			timeTag = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')

			f = open('diff/'+timeTag+'.diff', 'wb')
			line = resDiff.stdout.readline()
			while line:
				# print(count)
				print(line)
				f.write(line)
				line = resDiff.stdout.readline()
			f.close()
			vLatest = reversion
			print('save diff file to diff/'+timeTag+'.diff')

			#从DB中读取订阅者列表

			#TODO 发送RTX和邮件

		time.sleep(10)

	print('loop end')


t = threading.Thread(target=loop,name='LoopThread')
t.start()
t.join()
print('thread end loop')