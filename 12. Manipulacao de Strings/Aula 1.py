
class Extrator_argumentos_url:
    def __init__(self, url):
        if self.url_valida(url):
            self.url = url
        else:
            raise LookupError('Url inválida!')

    @staticmethod
    def url_valida(url):
        if url:
            return True
        else:
            return False

    def extrai_argumentos(self):

        busca_moeda_origem = 'moedaorigem'
        busca_moeda_destino = 'moedadestino'

        indice_inicial_moeda_destino = self.encontra_indice_inicial(busca_moeda_destino)

        indice_inicial_moeda_origem = self.encontra_indice_inicial(busca_moeda_origem)
        indice_final_moeda_origem = self.url.find('&')

        moeda_origem = self.url[indice_inicial_moeda_origem: indice_final_moeda_origem]
        moeda_destino = self.url[indice_inicial_moeda_destino:]

        return moeda_origem, moeda_destino

    def encontra_indice_inicial(self, moeda_buscada):
        return self.url.find(moeda_buscada) + len(moeda_buscada) + 1

# MAIN
url = 'https://bytebank.com/cambio?moedaorigem=real&moedadestino=dólar'

argumentos_url = Extrator_argumentos_url(url)
moeda_origem, moeda_destino = argumentos_url.extrai_argumentos()
print(moeda_destino, moeda_origem)

index = url.find('moedadestino') + len('moedadestino') + 1
substring = url[index:]
print(substring)
