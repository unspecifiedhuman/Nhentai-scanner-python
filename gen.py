import requests
no=int(input('number of urls: '))
b=''
name=input('name: ')
while True:
        for i in range (0,100):
                h=requests.get('https://nhentai.net/random')
                while h.url == 'https://nhentai.net/random/':
                        h=requests.get('https://nhentai.net/random')
                b = b + "\n" + h.url
                print(i)
        with open(name + ".txt", "a") as f:
                f.write('\n' + b)
                b=''
