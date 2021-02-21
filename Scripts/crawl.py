#!/usr/bin/env python
import json

filename = "ptt_dump_20210218_1132.json"

f = open(filename,encoding="utf-8")
data = json.load(f)

# Given the json dictionary, and the keyword want to filter
# return a list that contains all the related articles
def search(data, keyword):
	l = []
	count = 0
	for i in data['articles']:
		count += 1
		if keyword in i['article_title'] or keyword in i['content'] or keyword in i['messages']:
			i['count'] = str(count)
			l.append(i)
	return l
while 1:
	print('(A)Alisasa')
	print('(P)puipui')
	print('(L)List')
	print('(S)Search')
	command = input()
	if command == 'A':
		a = search(data, "愛莉莎莎")
		for i in a:
			print('{'+i['count']+'}'+i['article_title'])
		number = input();
		for i in a:
			if i['count'] == number:
				print(str(i['content']))
			
	if command == 'P':
		a = search(data, "天竺鼠車車")
		for i in a:
			print('{'+i['count']+'}'+i['article_title'])
		number = input();
		for i in a:
			if i['count'] == number:
				print(str(i['content']))
	if command == 'L':
		a = search(data, "")
		for i in a:
			print('{'+i['count']+'}'+i['article_title'])
		number = input();
		for i in a:
			if i['count'] == number:
				print(str(i['content']))
	if command == 'S':
		search_k = input('keyword:')
		a = search(data, search_k)
		for i in a:
			print('{'+i['count']+'}'+i['article_title'])
		number = input();
		for i in a:
			if i['count'] == number:
				print(str(i['content']))



