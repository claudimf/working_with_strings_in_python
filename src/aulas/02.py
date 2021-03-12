#Using find

argumento = "moedaorigem=real"
index = argumento.find('=')
subString = argumento[index + 1:]
print(subString)

argumento = 'https://www.bytebank.com.br/cambio?moedaorigem=real'
index = argumento.find('=')
subString = argumento[index + 1:]
print(subString)

# Using split
argumento = "moedaorigem=real"
listargumento = argumento.split('=')
print(listargumento)

url = "pagina?argumentos"
indice = url.find("?")
print(url[indice + 1:] )