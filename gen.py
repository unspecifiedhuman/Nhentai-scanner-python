import requests
no=int(input('number of urls: '))
na=input('name of file:')
b=''
u=0
for i in range (0,no):
	h=requests.get('https://nhentai.net/random')
	while h.url == 'https://nhentai.net/random/':
		h=requests.get('https://nhentai.net/random')
	print(h.url)
	open(na,'a').write('\n' + h.url)

