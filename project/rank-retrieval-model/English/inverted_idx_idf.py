import os
import glob

import json
import math

files = os.listdir('/home/nikhil/wikipediasearch/termfrequencydocs')

Number_Docs = len(files)

addr = '/home/nikhil/wikipediasearch/termfrequencydocs/'


file_path = '/home/nikhil/wikipediasearch/inverted.txt'

indx = {}

idf = {}

for filename in files:
	with open(addr+filename) as f:
		text = f.read()
		words = []
		str = ''
		fl=0
		for c in text:
			if c=='"' and fl==0:
				str+=c
				fl=1
			elif c=='"' and fl==1:
				str+=c
				fl=0
				words.append(str[1:-1])
				str=''
			elif fl==1:
				str+=c
				

		words.sort()

		for word in words:
			if word in indx.keys():
				indx[word].append(','+filename+' ')
			else:
				indx[word]=[]
				indx[word].append(filename+' ')



for key in indx:
	indx[key].sort()
	idf[key] = math.log((Number_Docs/len(indx[key])),10)

with open (file_path, 'w') as invert_idx:
	json.dump(indx, invert_idx, ensure_ascii=False)

with open (file_path, 'w') as idf_:
	json.dump(idf, idf_, ensure_ascii=False)
