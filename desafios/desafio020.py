from rich import print
from rich.panel import Panel

class Gamer:
    def __init__(self, nome, nick, ):
        self.nome = nome
        self.nick = nick
        self.favoritos = []

    def add_favoritos(self, favorito):
        self.favoritos.append(f":video_game: [blue]{favorito}[/]\n")
        self.favoritos = sorted(self.favoritos, key=str.lower)
    def ficha(self):
        self.favoritos[-1] = self.favoritos[-1][:-1]
        conteudo = f"Nome real: [black on blue] {self.nome} [/]\n"
        conteudo += "Jogos favoritos:\n"
        print(Panel(f"{conteudo}{''.join(self.favoritos)}", title=f"Jodador {self.nick}", width=40))

j1 = Gamer(nome="Mateus", nick="z0mbi19")
j1.add_favoritos(favorito="Portal 2")
j1.add_favoritos(favorito="nier automata")
j1.add_favoritos(favorito="Peripeteia")
j1.add_favoritos(favorito="Boltgun")
j1.add_favoritos(favorito="Fallout nv")
j1.ficha()