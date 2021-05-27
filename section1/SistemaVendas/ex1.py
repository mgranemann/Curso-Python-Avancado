# Crie uma classe Pessoa
# A classe de ter os seguintes atributos(variáveis):
# - nome
# - sobrenome
# - idade
# - sexo
# Crie em outro arquivo duas instancias(variáveis do tipo da classe) desta classe
# Atribua valores diferentes para cada instancia
# imprima todos os dados de cada instancia

from pessoa import Pessoa

p1 = Pessoa()
p2 = Pessoa()

p1.nome = 'Maykon'
p1.sobrenome = 'Granemann'
p1.idade = 17
p1.sexo = 'M'

p2.nome = 'Dyego'
p2.sobrenome = 'Rauen'
p2.idade = 19
p2.sexo = 'M'

print(f'{p1.nome_completo()}-{p1.idade}-{p1.sexo}')
print(f'{p2.nome_completo()}-{p2.idade}-{p2.sexo}')