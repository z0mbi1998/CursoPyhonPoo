from rich import print
from rich.panel import Panel

class Churrasco:
    preco_por_pessoa = 0.4
    preco_por_quilo = 82.40

    def __init__(self, titulo, qtd):
        self.titulo = titulo
        self.qtd = qtd

    def analisar(self):
        total_consulmo = self.qtd * self.__class__.preco_por_pessoa
        total_preco = total_consulmo * self.__class__.preco_por_quilo

        valor_por_pessoa = total_preco / self.qtd

        conteudo = f"Analisando o [green]{self.titulo}[/] com [blue]{self.qtd} convidados[/]\n"

        conteudo += f"Cada participante comera {self.__class__.preco_por_pessoa:,.2f}kg e cada kg custa R${self.__class__.preco_por_quilo}.\n"

        conteudo += f"Recomendo [blue]comprar {total_consulmo:,.2f}KG[/] de carne\n"

        conteudo += f"O custo total sera de [green]R${total_preco:,.2f}[/]\n"

        conteudo += f"Cada pessoa pagara [yellow]R${valor_por_pessoa:,.2f}[/] para participar"

        print(
            Panel(
                conteudo,
                title=self.titulo,
            )
        )

c1 = Churrasco("Churrasco", 150)
c1.analisar()
