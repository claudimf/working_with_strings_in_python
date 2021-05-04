import re

padrao_molde = "(xx)aaaa-wwww"
padrao = "[0-9]{2}[0-9]{4,5}[0-9]{4}"
texto = "eu gosto do numero 2126451234"
retorno = re.search(padrao, texto)
print(retorno.group())
