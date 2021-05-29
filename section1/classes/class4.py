# Class 4 - CRUD
# C = create - cadastrar
# R = read - ler
# U = update - alterar
# D = delete = delete

class Crud:
    def cadastar(dado):
        with open('dados.txt', 'a') as arquivo:
            arquivo.write(f'{dado}\n')
    
    def ler():
        with open('dados.txt', 'r') as arquivo:
            lista = []
            for linha in arquivo:
                dado = linha.strip().split(';')
                lista.append(dado)
        return lista

    def alterar():
        pass

    def deletar():
        pass
