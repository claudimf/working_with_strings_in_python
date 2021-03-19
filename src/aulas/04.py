from functions.extrator_argumentos_url import ExtratorArgumentosUrl

url = 'https://www.bytebank.com.br/cambio?moedaorigem=real&moedadestino=dolar'

# url = 'moedaorigem=real&moedadestino=dolar'
argumentosUrl = ExtratorArgumentosUrl(url)
moedaOrigem, moedaDestino = argumentosUrl.extraiArgumentos()
print(moedaOrigem, moedaDestino)

# 1
index = url.find("moedadestino")
print(index)

# 2
index = url.find("moedadestino")
substring = url[index:]
print(substring)

# 3
index = url.find("moedadestino") + len("moedadestino") + 1
substring = url[index:]
print(substring)
