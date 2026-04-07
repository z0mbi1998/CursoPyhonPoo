# Declaracao de classe
class Gafanhoto:
    def __init__(self): # Metodo construtor
        # Atributo de Instancia
        self.nome = ''
        self.idade = 0

    # metodos de instacia
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f'{self.nome} e Gafanhoto(a) e tem {self.idade} anos de idade.'

#Declaracao de Objeto
g1 = Gafanhoto()
g1.nome = 'Mateus'
g1.idade = 26
g1.aniversario()
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = 'Mauro'
g2.idade = 53
print(g2.mensagem())