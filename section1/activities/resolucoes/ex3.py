import sys
sys.path.append('.')

from models.pessoa import Pessoa

p1 = Pessoa()

p1.nome = 'Maykon'
p1.sobrenome = 'Granemann'
p1.idade = 17
p1.sexo = 'M'
p1.endereco.logradouro = 'Avenida Getulio Vargas'
p1.endereco.numero = 2008
p1.endereco.bairro = 'Reino das Itoupavas'
p1.endereco.cidade = 'Blumenau'
p1.endereco.estado = 'Santa Catarina'
p1.endereco.pais = 'Brasil'
p1.endereco.CEP = '88375-000'

print(p1)