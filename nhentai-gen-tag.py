import requests, re
a=''
no=0
name=input('name to save file as: ')
per='tag'
v=input('input 1 if searching for character, leave blank if searching for a tag: ')
tag=input('tag/char: ')
number=int(input('no. of pages: '))
z=tag
if v == '1':
	per='character'
while no != number:
	req=requests.get('https://nhentai.net/' + per + '/' + tag)
	for m in re.finditer('href=', req.text):
		h=m.end()+11
		a=req.text[m.start():h]
		if '/g/' in a:
			print(a)
			with open(name + ".txt", "a") as f:
				f.write('\n' + a)
	no=no+1
	tag = z + '/?page=' + str(no+1)
