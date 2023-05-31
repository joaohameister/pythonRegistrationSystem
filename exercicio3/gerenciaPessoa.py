from pessoa import Pessoa


class Gerenciapessoa:
    def __init__(self) -> None:
        self.pessoas = []

    def getPessoas(i, self):
        return self.pessoas[i]

    def imprimePessoas(self):
        aux = ""
        for Pessoa in self.pessoas:
            i = 0
            aux += self.pessoas[i].nome + "\n"
            i += 1
        print(aux)

    def adicionaPessoa(self):
        self.pessoas.append()
