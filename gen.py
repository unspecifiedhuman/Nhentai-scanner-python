import requests
a=0
c=0
no=int(input('number of urls: '))
b=''
r='https://nhentai.net/random'
name=input('name: ')
while True:
	h=requests.get('https://nhentai.net/random')
	while h.url == 'https://nhentai.net/random/':
		h=requests.get('https://nhentai.net/random')
	b = b + "\n" + h.url
	c+=1
	a+=1
	f=a/no
	f=f*100
	print(f)
	if c == 100:
		with open(name + ".txt", "w") as f:
			f.write(b)
		c=0

