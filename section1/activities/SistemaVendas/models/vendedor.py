
# encapsulamento
# modificadores de acesso

class Vendedor:

    def __init__(self, nome, sobrenome) -> None:    
        self.__nome = nome  
        self.__sobrenome = sobrenome

    @property
    def nome(self):
        return self.__nome
    
    @property
    def sobrenome(self):
        return self.__sobrenome

    @nome.setter
    def nome(self, nome):
        nome = nome + ' da silva '
        self.__nome = nome

    @sobrenome.setter
    def sobrenome(self, sobrenome):
        self.__sobrenome = sobrenome


vend1 = Vendedor('Bruno', 'Toretti')
vend1.nome = 'Brunno'
print(vend1.nome)