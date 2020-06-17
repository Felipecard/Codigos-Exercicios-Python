# EXPRESSOES REGULARES

import re
texto1 = 'Meu numero é 1234-1234'
texto2 = 'Fale comigo em 1234-1234, esse é meu telefone'
texto3 = '1234-1234 ;e o meu celular'
texto4 = 'lalalalalal 99543-1254 aaaaaaaa 33334444 aaaaaaaaaaaaa 2525-6677'

padrao = '[0-9]{4,5}[-]*[0-9]{4}'

retorno = re.findall(padrao,texto4)
print(retorno)

