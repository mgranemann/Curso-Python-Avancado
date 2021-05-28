class Endereco:
    logradouro = ''
    numero  = ''
    bairro = ''
    cidade = ''
    estado = ''
    pais = ''
    CEP = ''

    def endereco_resumido(self):
        return f'{self.logradouro}, {self.numero}, {self.bairro} - {self.cidade}'

    def __str__(self):
        return f'{self.logradouro};{self.numero};{self.bairro};{self.cidade};{self.estado};{self.pais};{self.CEP}'
