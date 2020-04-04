import urllib.request

try:
    with urllib.request.urlopen("http://www.pudim.com.br") as url: # com o comando urllib.request.urlopen - nao consegui rodar
        s = url.read()
except urllib.error.URLError:
    print('O site do pudim nao esta acessivel no momento')
else:
    print('Consegui acessar o site do pudim')
    print(s)


