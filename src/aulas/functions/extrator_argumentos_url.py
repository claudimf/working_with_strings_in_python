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

        buscaMoedaOrigem = "moedaorigem="
        buscaMoedaDestino = "moedadestino="

        # indiceInicialMoedaDestino = self.url.find("=", 15)
        # indiceInicialMoedaOrigem = self.url.find("=") + 1
        # indiceFinalMoedaOrigem = self.url.find("&")
        # indiceInicialMoedaDestino = self.url.find("=", indiceInicialMoedaOrigem + 1) + 1

        # indiceInicialMoedaDestino = self.url.find(buscaMoedaDestino) + len(buscaMoedaDestino) + 1
        # indiceInicialMoedaOrigem = self.url.find(buscaMoedaOrigem) + len(buscaMoedaOrigem) + 1

        indiceInicialMoedaDestino = self.encontraIndiceInicial(buscaMoedaDestino)
        indiceInicialMoedaOrigem = self.encontraIndiceInicial(buscaMoedaOrigem)
        indiceFinalMoedaOrigem = self.url.find("&")

        moedaOrigem = self.url[indiceInicialMoedaOrigem:indiceFinalMoedaOrigem]
        moedaDestino = self.url[indiceInicialMoedaDestino:]

        if moedaOrigem == "moedadestino":
            self.trocaMoedaOrigem()
            indiceInicialMoedaOrigem = self.encontraIndiceInicial(buscaMoedaOrigem)
            indiceFinalMoedaOrigem = self.url.find("&")
            moedaOrigem = self.url[indiceInicialMoedaOrigem:indiceFinalMoedaOrigem]

        return moedaOrigem, moedaDestino

    def encontraIndiceInicial(self, moedaBuscada):
        return self.url.find(moedaBuscada) + len(moedaBuscada)

    def trocaMoedaOrigem(self):
        self.url = self.url.replace("moedadestino", "real", 1)
        print(self.url)
