from functions.TelefonesBr import TelefonesBr


telefone = "2126481234"
telefone_objeto = TelefonesBr(telefone)
print(telefone_objeto.numero)

telefone = "abc"
telefone_objeto = TelefonesBr(telefone)
print(telefone_objeto.numero)
