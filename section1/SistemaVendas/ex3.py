from pessoa import Pessoa

pessoa1 = Pessoa()
pessoa1.nome = 'Maykon'
pessoa1.sobrenome = 'Granemann'
pessoa1.idade = 10
pessoa1.sexo = 'M'
pessoa1.endereco.logradouro = 'Avenida Getulio Vargas'
pessoa1.endereco.numero = 2008
pessoa1.endereco.bairro = 'Reino das Itoupavas'
pessoa1.endereco.cidade = 'Blumenau'
pessoa1.endereco.estado = 'Santa Catarina'
pessoa1.endereco.pais = 'Brasil'
pessoa1.endereco.CEP = '88375-000'

print(pessoa1)
