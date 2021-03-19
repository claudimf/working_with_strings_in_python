from functions.extrator_argumentos_url import ExtratorArgumentosUrl

url = 'https://www.bytebank.com.br/cambio?moedaorigem=moedadestino&moedadestino=dolar'


argumentosUrl = ExtratorArgumentosUrl(url)
moedaOrigem, moedaDestino = argumentosUrl.extraiArgumentos()
print(moedaOrigem, moedaDestino)
