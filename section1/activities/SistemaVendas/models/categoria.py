
class Categoria:
    __nome:str
    __descricao:str

    def get_nome(self):
        return self.__nome

    def get_descricao(self):
        return self.__descricao

    def set_nome(self, nome):
        self.__nome = nome

    def set_descricao(self, descricao):
        self.__descricao = descricao

    def __str__(self) -> str:
        return f'{self.get_nome()};{self.get_descricao()}'

    @staticmethod
    def lista_para_objeto(lista)->object:
        categoria = Categoria()
        categoria.set_nome(lista[0])
        categoria.set_descricao(lista[1])
        return categoria