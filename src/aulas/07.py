from functions.extrator_argumentos_url import ExtratorArgumentosUrl

url = 'https://www.bytebank.com/cambio?moedaorigem=Real&moedadestino=Dolar&valor=1500'


argumentosUrl = ExtratorArgumentosUrl(url)
argumentosUrl2 = ExtratorArgumentosUrl(url)

print(argumentosUrl)
print(argumentosUrl == argumentosUrl2)
print(id(argumentosUrl))
print(id(argumentosUrl2))

url2 = 'https://www.bytebank.com/cambio?moedaorigem=Real&moedadestino=Dolar&valor=100'

argumentosUrl2 = ExtratorArgumentosUrl(url2)

print(argumentosUrl)
print(argumentosUrl == argumentosUrl2)
print(id(argumentosUrl))
print(id(argumentosUrl2))

