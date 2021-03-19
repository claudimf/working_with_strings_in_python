from functions.extrator_argumentos_url import ExtratorArgumentosUrl

url = 'https://www.bytebank.com.br/cambio?moedaorigem=Real&moedadestino=Dolar&valor=1500'


argumentosUrl = ExtratorArgumentosUrl(url)
moedaOrigem, moedaDestino = argumentosUrl.extraiArgumentos()
valor = argumentosUrl.extraiValor()
print(moedaOrigem, moedaDestino, valor)
