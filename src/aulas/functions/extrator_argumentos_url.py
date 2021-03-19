class ExtratorArgumentosUrl():
    def __init__(self, url):
        if self.urlEhValida(url):
            self.url = url.lower()
        else:
            raise LookupError("URL inválida")

    @staticmethod
    def urlEhValida(url):
        if url and url.startswith("https://www.bytebank.com"):
            return True
        else:
            return False

    def __len__(self):
        return len(self.url)

    def __str__(self):
        moedaOrigem, moedaDestino = self.extraiArgumentos()
        # representacaoString2 = "Valor: " + self.extraiValor() + " " + moedaOrigem + " " + moedaDestino
        representacaoString = 'Valor: {}\n Moeda Origem: {} \n Moeda Destino: {} \n'.format(self.extraiValor(), moedaOrigem, moedaDestino)
        return representacaoString

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


        if moedaOrigem == "moedadestino":
            self.trocaMoedaOrigem()
            indiceInicialMoedaOrigem = self.encontraIndiceInicial(buscaMoedaOrigem)
            indiceFinalMoedaOrigem = self.url.find("&")
            moedaOrigem = self.url[indiceInicialMoedaOrigem:indiceFinalMoedaOrigem]


        indiceFinalMoedaDestino = self.url.find("&valor")
        moedaDestino = self.url[indiceInicialMoedaDestino:indiceFinalMoedaDestino]

        return moedaOrigem, moedaDestino

    def encontraIndiceInicial(self, moedaBuscada):
        return self.url.find(moedaBuscada) + len(moedaBuscada)

    def trocaMoedaOrigem(self):
        self.url = self.url.replace("moedadestino", "real", 1)
        print(self.url)

    def extraiValor(self):
        buscaValor = "valor="
        indiceInicialValor = self.encontraIndiceInicial(buscaValor)
        valor = self.url[indiceInicialValor:]
        return valor
