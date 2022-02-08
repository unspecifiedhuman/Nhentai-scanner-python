import requests, re
a=''
name=input('name to save file as: ')
per='tag'
v=input('tags or character seperated by a comma: ') #e.g. rem,ram,anal
v=v.replace(',','+')
b=v
number=int(input('no. of pages: '))
for i in range (0,number):
        req=requests.get('https://nhentai.net/search/?q=' + v)
        for m in re.finditer('href=', req.text):
                h=m.end()+11
                a=req.text[m.start():h]
                if '/g/' in a:
                        a=a.replace('href="','nhentai.net')
                        while a[-1] != '/':
                                a=a[:-1]
                        print(a)
                        with open(name + ".txt", "a") as f:
                                f.write('\n' + a)
        v = b + '&page=' + str(i)
