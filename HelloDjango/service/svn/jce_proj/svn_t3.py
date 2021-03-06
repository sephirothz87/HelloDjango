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
vLatest = ''
#上次扫描的版本号
#假设是从一个更旧的版本扫描
# vLastScan = '38000'
vLastScan = '38729'#9/26日日报

cmdUpdate = 'svn update'
cmdDiff = 'svn diff -r'

reReversion = r'\d+'

def getModifyFileList(v1,v2):
	resDiffSummrize = subprocess.Popen(cmdDiff+v1+':'+v2+' --summarize',stdout=subprocess.PIPE, stderr=subprocess.STDOUT,bufsize=1)
	line = resDiffSummrize.stdout.readline()
	modifyFileList = []

	while line:
		lineStr = bytes.decode(line)
		fileName = lineStr[8:].strip()

		# print(lineStr)
		if lineStr.startswith(('M','D')) and fileName.endswith('.jce'):
			modifyFileList.append(fileName)

		line = resDiffSummrize.stdout.readline()
	return modifyFileList

def exportDiffResult(fileList,v1,v2,resFile):
	diffOutFile = open(resFile, 'w')

	# 循环所有结果列表
	for file in fileList:
	#测试前几个文件
	# count = 0
	# while count<5:
		# file = fileList[count]

		print(file)
		resDiff = subprocess.Popen(cmdDiff+v1+':'+v2+' '+file,stdout=subprocess.PIPE, stderr=subprocess.STDOUT,bufsize=1)
		isModify = False

		#过滤掉全部都是增加的变更文件
		line = resDiff.stdout.readline()
		while line:
			# print(line)
			#测试过程中发现有的文件是GB2312,会导致报错
			lineStr = bytes.decode(line,errors='ignore').strip()
			if lineStr.startswith('-') and not lineStr.startswith('---'):
				isModify = True
				break
			line = resDiff.stdout.readline()

		if isModify:
			resDiff = subprocess.Popen(cmdDiff+v1+':'+v2+' '+file,stdout=subprocess.PIPE, stderr=subprocess.STDOUT,bufsize=1)
			line = resDiff.stdout.readline()
			while line:
				# print(line)

				# 解决多种编码的问题
				try:
					diffOutFile.write(line.decode('uft-8').rstrip())
				except:
					try:
						diffOutFile.write(line.decode('ascii').rstrip())
					except:
						try:
							diffOutFile.write(line.decode('gb2312').rstrip())
						except:
							diffOutFile.write(line.decode().rstrip())
				diffOutFile.write('\n')
				
				line = resDiff.stdout.readline()
		#限制次数的测试
		# count+=1
	diffOutFile.close()


resUpdate = subprocess.Popen(cmdUpdate,stdout=subprocess.PIPE, stderr=subprocess.STDOUT,bufsize=1)

lastLine = ''
line = resUpdate.stdout.readline()
while line:
	lastLine = line
	line = resUpdate.stdout.readline()
print(lastLine)
lastLine=lastLine.decode('utf-8')
matchObj = re.search(reReversion,lastLine, flags=0)
# print(matchObj.group())

reversion = matchObj.group()
if vLatest == '':
	vLatest = reversion

print(vLatest)

# 与前一个版本对比
# resDiff = subprocess.Popen(cmdDiff+vLatest+':'+reversion,stdout=subprocess.PIPE, stderr=subprocess.STDOUT,bufsize=1)

modifyFileList = []
#发生基线变更，直接输出最新与基线的对比结果
if int(vLastScan) < int(vBase):
	modifyFileList = getModifyFileList(vBase,vLatest)
	
	timeTag = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
	
	#测试
	# modifyFileList = ['trunk\\jce\\feed\\fresh_feed.jce']

	exportDiffResult(modifyFileList,vBase,vLatest,('diff/'+timeTag+'.diff'))
#没有基线变更
else:
	print('modifyFileList')
	modifyFileList = getModifyFileList(vLastScan,vLatest)
	print(len(modifyFileList))

	print('modifyFileListToBase')
	modifyFileListToBase = getModifyFileList(vBase,vLatest)
	print(len(modifyFileListToBase))

	#增量变更列表
	incModifyFileList = []

	for file in modifyFileList:
		if file in modifyFileListToBase:
			incModifyFileList.append(file)
		else:
			print('not modify to base')

	print(len(incModifyFileList))
	print(incModifyFileList)
	
	if len(incModifyFileList) != 0:
		timeTag = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
		exportDiffResult(incModifyFileList,vLastScan,vLatest,('diff/'+timeTag+'.diff'))