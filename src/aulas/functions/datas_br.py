from datetime import datetime


class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def mes_cadastro(self):
        meses_do_ano = [
            "janeiro", "fevereiro", "março",
            "abril", "maio", "junho",
            "julho", "agosto", "setembro",
            "outubro", "novembro", "dezembro"
            ]
        mes = self.momento_cadastro.month - 1
        return meses_do_ano[mes]

    def dia_semana(self):
        dia_semana_lista = [
            "segunda", "terça",
            "quarta", "quinta", "sexta"
        ]
        dia_semana = self.momento_cadastro.weekday()
        return dia_semana_lista[dia_semana]
