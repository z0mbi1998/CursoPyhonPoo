from rich import print

class Caneta:
    def __init__(self, cor):
        self.cor = cor
        self.tampada = True
        self.exist = True

        match self.cor.lower().strip():
            case "azul":
                self.cor = "blue"
            case "vermelho":
                self.cor = "red"
            case "verde":
                self.cor = "green"
            case _:
                print("Nao tenho essa cor de caneta")
                self.exist = False

    def destampar(self):
        if self.exist:
            self.tampada = False
        else:
            print("Nao consigo destampar uma caneta que eu n tenho")

    def escrever(self, texto):
        if self.exist:
            if self.tampada:
                print(f":no_entry_sign: [{self.cor}]caneta[/] esta tampada!")
            else:
                print(f"[{self.cor}]{texto}[/] ", end="")
        else:
            print("Nao consigo escrever uma caneta que eu n tenho")

    def quebrar_linha(self, valor):
        for i in range(valor):
            print("\n", end="")

c1 = Caneta("azul")
c2 = Caneta("vermelho")
c3 = Caneta("Verde")
c1.destampar()
c2.destampar()
c3.destampar()
c1.escrever("Ola, tubo bem!")
c1.quebrar_linha(2)
c2.escrever("Ola, tubo bem")
c3.escrever("ahhhhhhhhhhhhhhhhh")
