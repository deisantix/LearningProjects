import re


# CLASSE EXTRATORA DE URL
class ExtratoUrl:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)

        self.valida_url()

    # MÉTODOS ESPECIAIS
    def __len__(self):
        return len(self.url)

    def __str__(self):
        return f'{self.url}\nBase: {self.get_base_url()}\nParâmetros: {self.get_parametros_url()}'

    def __eq__(self, other):
        return self.url == other.url

    # SANITIZAÇÃO DA URL (retirar espaços)
    @staticmethod
    def sanitiza_url(url):
        if type(url) is str:
            return url.strip()
        else:
            return ""

    # VALIDAR URL
    def valida_url(self):
        if not self.url:
            raise ValueError("A Url está vazia")

        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        esta_no_padrao = padrao_url.match(self.url)

        if not esta_no_padrao:
            raise ValueError("A Url não é válida")

    # RETORNAR BASE DA URL
    def get_base_url(self):
        base_url_find = self.url.find('?')

        if base_url_find != -1:
            base_url = self.url[:base_url_find]
        else:
            base_url = self.url

        return base_url

    # RETORNAR PARAMETROS DA URL
    def get_parametros_url(self):
        parametros_url = self.url[len(self.get_base_url()) + 1:]
        return parametros_url

    # RETORNAR VALOR DO PARAMETRO ESCOLHIDO
    def get_valor_parametros(self, parametro):
        parametros_url = self.get_parametros_url()

        indice_parametro = parametros_url.find(parametro)
        indice_valor = indice_parametro + len(parametro) + 1

        indice_e_comercial = parametros_url.find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = parametros_url[indice_valor:]
        else:
            valor = parametros_url[indice_valor:indice_e_comercial]

        return valor


# CONVERSOR DOS VALORES
def conversor_moeda(origem, destino, quantidade):
    # valor do dólar atualmente arredondado
    dolar_real = 5.13

    # conversor
    valor_convertido = None
    quantidade = int(quantidade)

    if origem == "real" and destino == "dolar":
        valor_convertido = quantidade / dolar_real

    elif origem == "dolar" and destino == "real":
        valor_convertido = quantidade * dolar_real

    else:
        return f"Conversão de {origem} para {destino} não está disponível"

    return f'{valor_convertido:.2f}'


# FUNÇÃO PRINCIPAL
def main():
    site = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"

    extrato_url = ExtratoUrl(site)
    origem = extrato_url.get_valor_parametros("moedaOrigem")
    destino = extrato_url.get_valor_parametros("moedaDestino")
    quantidade = extrato_url.get_valor_parametros("quantidade")

    print(conversor_moeda(origem, destino, quantidade))


if __name__ == '__main__':
    main()
