from dao.dao import Dao
from models.pessoa import Pessoa


# heranca
class PessoaDao(Dao):
    def __init__(self):
        nome_arquivo = 'pessoa.txt'
        # super() == classe mãe (heranca)
        # chama o construtor da classe mãe passando o valor para o parametro obrigatorio
        super().__init__(nome_arquivo)

    def cadastrar(self, pessoa:Pessoa ):
        return super().cadastrar(str(pessoa))

    def ler(self):
        dados = super().ler()
        lista_pessoas = []
        for dado in dados:
            pessoa_dados = str(dado).split(';')
            pessoa = Pessoa.lista_para_objeto(pessoa_dados)
            lista_pessoas.append(pessoa)
        return lista_pessoas

    def alterar(self, pessoa_antiga:Pessoa, pessoa_nova:Pessoa):
        valor_antigo = f'{pessoa_antiga.nome};{pessoa_antiga.sobrenome};{pessoa_antiga.idade};{pessoa_antiga.sexo}'
        novo_valor = f'{pessoa_nova.nome};{pessoa_nova.sobrenome};{pessoa_nova.idade};{pessoa_nova.sexo}'
        return super().alterar(valor_antigo, novo_valor)

    def deletar(self, pessoa:Pessoa):
        dado = f'{pessoa.nome};{pessoa.sobrenome};{pessoa.idade};{pessoa.sexo}'
        return super().deletar(dado)

