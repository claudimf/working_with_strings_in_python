import re
email1 = "Meu numero é 1234-1234"
email2 = "Fale comigo em 1234-1234 esse é meu telefone"
email3 = "1234-1234 é o meu celular"
email4 = "lalalalala 9543-1254 hsiahsahrueuhdiaeu"
email5 = "lalalalala 9543-1254 hsiahsahrueuhdiaeu 9243-1254 9343-1254"
email6 = "12341234 é o meu celular"

# padrao = "[012345679][012345679][012345679][012345679][-][012345679][012345679][012345679][012345679]"
padrao = "[0-9]{4}[-]*[0-9]{4}"

retorno = re.search(padrao, email1)
print(retorno.group())

retorno = re.search(padrao, email2)
print(retorno.group())

retorno = re.search(padrao, email3)
print(retorno.group())

retorno = re.search(padrao, email4)
print(retorno.group())

retorno = re.findall(padrao, email5)
print(retorno)

retorno = re.search(padrao, email6)
print(retorno.group())
