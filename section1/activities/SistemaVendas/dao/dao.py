# Dao - Data Access Object
# converter um dado de uma fonte de dados(banco de dados, arquivo text) para objeto de classe

class Dao:
    # método construtor - sempre chamado ao criar um objeto da classe
    def __init__(self, nome_arquivo):
        self.arquivo = nome_arquivo

    def cadastrar(self, dado):
        with open(self.arquivo, 'a') as arquivo:
            arquivo.write(f'{dado}\n')
    
    def ler(self):
        with open(self.arquivo, 'r') as arquivo:
            lista = []
            for linha in arquivo:
                dado = linha.strip()
                lista.append(dado)
        return lista

    def reescrever(self, dados):
         with open(self.arquivo, 'w') as arquivo:
            # percorre a lista de dados alterados e salva item a item no arquivo
            for dado in dados:
                arquivo.write(f'{dado}\n')

    def alterar(self,valor_antigo, novo_valor):
        # buscar o dado antigo no arquivo
        # reutilizano a funcao ler para pegar todos os dados do arquivo
        lista_de_dados= self.ler()

        #criando uma nova lista para receber os dados alterados 
        novos_dados = []
        # percorrendo a lita para verificar se exite correspondencia do valor passado(valor_antigo)
        for dado in lista_de_dados:
            # se o dado do arquivo for igual ao dado informado por parametro, subistitui pelo novo valor
            if dado == valor_antigo:
                dado = novo_valor
            #adicionado os dados da lista antiga na nova lista, junto com as alteracoes
            novos_dados.append(dado)
        
        # reescrever o novo conteudo
        self.reescrever(novos_dados)

    def deletar(self, dado):
        lista_de_dados= self.ler()
        novos_dados = []
        
        for linha in lista_de_dados:         
            if linha != dado:
                novos_dados.append(linha)

        # reescrever o novo conteudo
        self.reescrever(novos_dados)

    