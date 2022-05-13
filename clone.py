#this clones x number of galleries and saves them to a directory with a html file to desplay them.
#made in linux in the directory "~.bot" where there is clone.py and files directory.
#when i out this on github, i accidentally removed the origional gen.py so i'll make a better one.

import requests, re, wget, os, time
no=int(input('number of galleries: '))
b=''
u=0
for i in range (0,no):
	h=requests.get('https://nhentai.net/random')
	while h.url == 'https://nhentai.net/random/':
		h=requests.get('https://nhentai.net/random')
	b =  "\n" + h.url
	print(b)
	for g in re.finditer('"name" content=', h.text):
		y=g.end()+80
		j=h.text[g.start()+16:y]
		while j[-20:] != '" /><meta itemprop="':
			j=j[:-1]
		j=j[:-20]
		j=j.replace(' ', '_')
		print(j)
		os.mkdir('files/' + j)
	for m in re.finditer('data-src=', h.text):
		u+=1
		l=m.end()+55
		z=h.text[m.start():l]
		while z[-1] != 'g':
			z=z[:-1]
		z=z[10:]
		print(str(z))
		r=requests.get(str(z))
		open(str(u) + str(z[-4:]), 'wb').write(r.content)
		os.system('mv ' + str(u) + str(z[-4:]) + ' files/"' + j + '"/')

		q="'"
#		os.system("wget -o " + str(u) + str(z[-4:]) + " " +  str(z))
		r='<p><img src=' + q + './' + str(u) +  str(z[-4:]) + '' + q + '></p>'
		os.system('echo "' + str(r) + '" >> ~/bot/files/' + str(j) +  '/index.html')
#		os.system('rm ' + str(u) + str(z[-4:]))
