
# encapsulamento
# modificadores de acesso

class Vendedor:

    def __init__(self, nome, sobrenome, idade, registro, telefone, email, ativo) -> None:    
        self.__nome = nome  
        self.__sobrenome = sobrenome
        self.__idade = idade
        self.__registro = registro
        self.__telefone = telefone
        self.__email = email
        self.__ativo = ativo


vend1 = Vendedor()
