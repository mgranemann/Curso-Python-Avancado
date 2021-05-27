# pacote.modulo import classe


from models.categoria import Categoria
from models.produto import Produto

# Objeto é uma instancia de uma classe
# Ou de forma mais simples uma variavel do tipo da classe

# objeto da classe Categoria
categoria1 = Categoria()
categoria2 = Categoria()
# objeto da classe Produto
produto1 = Produto()


categoria1.nome = 'Carros'
categoria1.descricao = 'Rebaixados, com som paredao'
categoria2.nome = 'Motos'
categoria2.descricao = 'Motos sem silencioso'
print(categoria1.nome, categoria1.descricao)