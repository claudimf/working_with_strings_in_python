import re

padrao = "\w{5,50}@\w{3,10}.\w{2,3}.\w{2,3}"
texto = "aaabbbcc rodrigo123@gmail.com.br"
retorno = re.search(padrao, texto)
print(retorno.group())

padrao = "\w{5,50}@[a-z]{3,10}.com.br"
texto = "aaabbbcc rodrigo123@gmail.com.br ccbbbaaa"
retorno = re.search(padrao, texto)
print(retorno.group())
