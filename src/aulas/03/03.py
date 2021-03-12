from extrator_argumentos_url import ExtratorArgumentosUrl

url = 'https://www.bytebank.com.br/cambio?moedaorigem=real&moedadestino=dolar&valor=700'
argumento = ExtratorArgumentosUrl(url)
print(argumento)

# url = None
# argumento = ExtratorArgumentosUrl(url)
# print(argumento)

# url = ''
# argumento = ExtratorArgumentosUrl(url)
# print(argumento)