from functions.extrator_argumentos_url import ExtratorArgumentosUrl

url = 'https://www.bytebank.com.br/cambio?moedaorigem=real&moedadestino=dolar&valor=700'

url = 'moedaorigem=real&moedadestino=dolar'
argumentosUrl = ExtratorArgumentosUrl(url)
print(argumentosUrl)

moedaOrigem, moedaDestino = argumentosUrl.extraiArgumentos()

print(moedaOrigem, moedaDestino)
