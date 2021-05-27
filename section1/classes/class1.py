# Class 1 - 
# produto
# nome, descricao, valor
# CRUD
# C = Create - Criar/Salvar
# R = Read - ler 1 ou mais
# U = Update - Alteração
# D = Delete = Exclusão

produto = {'id':0, 'nome':'', 'descricao':'', 'valor': 0.0 }
lista = []

def cadastrar(nome, descricao, valor):
    produto['id'] = produto['id'] + 1
    produto['nome'] = nome
    produto['descrica'] = descricao
    produto['valor'] = valor
    lista.append(produto)

def ler():
    for p in lista:
        print(f" {p['id']} {p['nome']} {p['descrica']} {p['valor']}")

def alterar():
    pass

def deletar():
    pass
