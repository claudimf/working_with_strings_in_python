from datetime import datetime
from functions.datas_br import DatasBr


hoje = datetime.today()
hoje_formatada = hoje.strftime("%d/%m/%Y")

print(hoje)
print(hoje_formatada)

hoje = datetime.today()
hoje_formatada = hoje.strftime("%d/%m/%Y %H:%M")

print(hoje)
print(hoje_formatada)
print(type(hoje_formatada))