#coding:utf-8
import os
import json
from tqdm import tqdm
import zip

txtpath = ""
jsonpath = ""
with open(txtpath, 'r', encoding='utf-8')as f:
titles = []
docs = []
	for line in f:
		if line.endswith(":") and line<=10:
			title = line.strip()[:-1]
			titles.append(title)
			docs.append(doc_text)

			context = ""

		doc_text += line

	dic = dict(zip(titles,docs))

with open(jsonpath, "w")as f:
	json.dump(dic,f)
	print(down)