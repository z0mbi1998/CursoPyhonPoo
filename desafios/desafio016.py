from rich import print

class Funcionario:
    empresa = "Curso em Video" # Atributo de classe

    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentar(self):
        return f":handshake: Ola, sou [blue]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da empresa {self.__class__.empresa}"

c1 = Funcionario("Maria", "Administracao", "Diretora")
print(c1.apresentar())

c2 = Funcionario("Pedro", "TI", "Programador")
print(c2.apresentar())