# 
# type hint 

from models.categoria import Categoria


class Produto:
    nome:str = ''
    descricao:str = ''
    valor:float = 0.0
    categoria = Categoria()

    def __str__(self) -> str:
        return f'{self.nome};{self.descricao};{self.valor};{self.categoria}'

    @staticmethod
    def lista_para_objeto(lista:list) -> object:
        produto = Produto()
        produto.nome = lista[0]
        produto.descricao = lista[1]
        produto.valor = lista[2]
        produto.categoria = Categoria.lista_para_objeto(lista[3:])
        return produto

