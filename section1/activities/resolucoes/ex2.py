import sys
sys.path.append('.')


from models.endereco import Endereco

end1 = Endereco()
end1.logradouro = 'Avenida Getulio Vargas'
end1.numero = 2008
end1.bairro = 'Reino das Itoupavas'
end1.cidade = 'Blumenau'
end1.estado = 'Santa Catarina'
end1.pais = 'Brasil'
end1.CEP = '88375-000'

end2 = Endereco()
end2.logradouro = 'Avenida Jucelino'
end2.numero = -50
end2.bairro = 'Reino do Garcia'
end2.cidade = 'Ilha da Magia'
end2.estado = 'Santa Catarina'
end2.pais = 'Argentina'
end2.CEP = '39990-000'

print(f'{end1.endereco_resumido()}, {end1.estado}, {end1.pais}, {end1.CEP}')
print(f'{end2.endereco_resumido()}, {end2.estado}, {end2.pais}, {end2.CEP}')

