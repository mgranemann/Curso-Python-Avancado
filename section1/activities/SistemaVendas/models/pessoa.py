from models.endereco import Endereco


class Pessoa:
    nome = ''
    sobrenome= ''
    idade = 0
    sexo = ''
    # em Programação Orientada a Objetos uso de uma classe dentro de outra
    # conposicao
    endereco = Endereco()

    # toda funcao dentro de uma classe
    # precisa ter como primeiro parametro o self
    def nome_completo(self):
        # self representa a instancia da classe
        return f'{self.nome} {self.sobrenome}'

    # sobreescrita de metodo
    # override
    def __str__(self):
        return f'{self.nome};{self.sobrenome};{self.idade};{self.sexo};{self.endereco}'

    @staticmethod
    def lista_para_objeto(pessoa_lista):
        pessoa = Pessoa()
        pessoa.nome = pessoa_lista[0]
        pessoa.sobrenome = pessoa_lista[1]
        pessoa.idade = pessoa_lista[2]
        pessoa.sexo = pessoa_lista[3]
        pessoa.endereco = Endereco.lista_para_objeto(pessoa_lista[4:])
        return pessoa