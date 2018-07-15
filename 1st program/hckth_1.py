# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 12:16:27 2018

@author: Lenovo
"""

#import numpy as np
from collections import Counter
inpu = int(input())
num=input()
num+=" "
array=[]
j=0

for i in range(0,len(num)):
	val=0
	if(num[i]==' '):
		k=j
		if(num[k]=='-'):
			for k in range(j+1,i):
				val=val*10+int(num[k])
			val*=-1
		else:

			for k in range(j,i):
				val=val*10+int(num[k])	
		array.append(val)	
		j=i+1	
if(inpu==len(array)):
	b=[]
	nlist = Counter(array)
	for k,v in nlist.items():
		if(int(k)>0):
			b.append(k)
	count=0
	for i in range(1,len(b)-1):
		count+=int(b[i])
	try:
		print(abs(count/(len(b)-2)))
	except ZeroDivisionError:
		print('length of the array became Zero :)')

else:
	print('Entered Size not matched Please Check it')
	     

