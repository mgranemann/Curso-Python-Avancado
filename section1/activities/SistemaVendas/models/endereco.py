class Endereco:
    logradouro = ''
    numero  = ''
    bairro = ''
    cidade = ''
    estado = ''
    pais = ''
    cep = ''

    def endereco_resumido(self):
        return f'{self.logradouro}, {self.numero}, {self.bairro} - {self.cidade}'

    def __str__(self):
        return f'{self.logradouro};{self.numero};{self.bairro};{self.cidade};{self.estado};{self.pais};{self.cep}'

    @staticmethod
    def lista_para_objeto(endereco_lista):
        endereco = Endereco()
        endereco.logradouro = endereco_lista[0]
        endereco.numero = endereco_lista[1]
        endereco.bairro = endereco_lista[2]
        endereco.cidade = endereco_lista[3]
        endereco.estado = endereco_lista[4]
        endereco.pais = endereco_lista[5]
        endereco.cep = endereco_lista[6]
        return endereco


        