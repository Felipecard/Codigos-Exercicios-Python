from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'dados.txt'

if not arquivoexiste(arq):
    criararquivo(arq)

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        #Opcao de listar o conteudo de um arquivo
        lerarquivo(arq)
    elif resposta == 2:
        #Opcao de cadastrar nova pessoa
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do Sistema... Ate logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opcao valida!\033[m')
    sleep(2)
