import requests, re
a=''
no=0
name=input('name to save file as: ')
tag=input('tag: ')
number=int(input('no. of pages: '))
z=tag
while no != number:
	req=requests.get('https://nhentai.net/tag/' + tag)
	for m in re.finditer('href=', req.text):
		h=m.end()+11
		a=req.text[m.start():h]
		if '/g/' in a:
			print(a)
			with open(name + ".txt", "a") as f:
				f.write('\n' + a)
	no=no+1
	tag = z + '/?page=' + str(no+1)

