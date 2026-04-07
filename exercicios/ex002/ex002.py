# Declaracao de classe
class Gafanhoto:
    """

    Essa classe cria um Gafanhoto, que e uma pessoa que tem nome e idade .

    Para criar uma nova pessoa, use:
    variavel = Gafanhoto(nome, idade)

    """
    def __init__(self, nome = "vazio", idade = 0): # Metodo construtor
        # Atributo de Instancia
        self.nome = nome
        self.idade = idade

    # metodos de instacia
    def aniversario(self):
        self.idade += 1

    def __str__(self): # Dunder Method
        return f'{self.nome} e Gafanhoto(a) e tem {self.idade} anos de idade.'

    def __getstate__(self):
        return f"Estado: nome = {self.nome}, idade = {self.idade}"

#Declaracao de Objeto
g1 = Gafanhoto('Mateus', 26)
g1.aniversario()
print(g1)

print(g1.__dict__)
print(g1.__getstate__())
print(g1.__class__)

g2 = Gafanhoto('Mauro', 53)
print(g2)

g3 = Gafanhoto()
print(g3)