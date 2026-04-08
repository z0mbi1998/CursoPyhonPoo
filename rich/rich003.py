from rich import print
from rich.table import Table

tabela = Table(title="Tabela de precos")

tabela.add_column("Nome", justify="center", style="cyan")
tabela.add_column("Preco", justify="center", style="blue")

tabela.add_row("Lapis", "R$1.50")
tabela.add_row("Borracha", "R$5.00")

print(tabela)