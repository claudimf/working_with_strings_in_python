from datetime import datetime, timedelta
from functions.datas_br import DatasBr


hoje = datetime.today()
amanha = datetime.today() + timedelta(days=1, hours=5)

print(hoje)
print(amanha)
print(amanha - hoje)

hoje = DatasBr()
print(hoje.tempo_cadastro())