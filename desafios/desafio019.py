from rich import print
import time

class Livro:
    pag = 1

    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas

        print(f":book: [blue]Voce acabou de abrir o livro '[red]{self.titulo}[/]' que tem [green]{self.paginas} paginas[/] no total. Voce agora esta na pagina[/] [yellow]pagina {self.pag}[/]")

    def avancar_paginas(self , paginas):
        av = 0
        for i in range(paginas):
            if self.pag == self.paginas:
                break
            av += 1
            self.pag += 1
            time.sleep(0.5)
            print(f"Pag{self.pag} :arrow_forward: ", end="")



        print(f"[blue]Voce avancou {av} e agora vc esta na[/] [yellow]pagina {self.pag}[/]")

        if self.pag == self.paginas:
            print(f":closed_book: [red]Voce chegou ao final do livro '{self.titulo}'[/]")

l1 = Livro("Livro 1", 10)
l1.avancar_paginas(5)
l1.avancar_paginas(1)
l1.avancar_paginas(18)
