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

