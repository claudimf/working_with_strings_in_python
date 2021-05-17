from functions.acesso_cep import BuscaEndereco


cep = "25800320"
objeto_cep = BuscaEndereco(cep)
a = objeto_cep.acessa_via_cep()
print(a)

cep = "01001000"
objeto_cep = BuscaEndereco(cep)
a = objeto_cep.acessa_via_cep()
print(a)
