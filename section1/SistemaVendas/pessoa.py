class Pessoa:
    nome = ''
    sobrenome= ''
    idade = 0
    sexo = ''

    # toda funcao dentro de uma classe
    # precisa ter como primeiro parametro o self
    def nome_completo(self):
        # self representa a instancia da classe
        return f'{self.nome} {self.sobrenome}'