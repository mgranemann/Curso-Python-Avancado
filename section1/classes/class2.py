# Class 2 - 

class Produto:
    id_produto = 0
    nome = ''
    descricao = ''
    valor = 0.0

    def cadastrar(self, nome, descricao, valor):
        self.id_produto = 0
        self.nome = nome
        self.descricao = descricao
        self.valor = valor

    def ler(self):
        return f'{self.id_produto}{self.nome}{self.descricao}{self.valor}'

    def alterar(self, id):
        pass

    def deletar(self):
        pass

produto = Produto()
produto.cadastrar()