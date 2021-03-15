class ExtratorArgumentosUrl():
    def __init__(self, url):
        if self.urlEhValida(url):
            self.url = url
        else:
            raise LookupError("URL inválida")

    @staticmethod
    def urlEhValida(url):
        if url:
            return True
        else:
            return False

    def extraiArgumentos(self):
        # indiceInicialMoedaDestino = self.url.find("=", 15)

        indiceInicialMoedaOrigem = self.url.find("=") + 1
        indiceFinalMoedaOrigem = self.url.find("&")
        indiceInicialMoedaDestino = self.url.find("=", indiceInicialMoedaOrigem + 1) + 1

        moedaOrigem = self.url[indiceInicialMoedaOrigem:indiceFinalMoedaOrigem]
        moedaDestino = self.url[indiceInicialMoedaDestino:]

        return moedaOrigem, moedaDestino
