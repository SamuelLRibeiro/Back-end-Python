class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self.categoria = categoria.title()
        self._ativo = False
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self._nome} | {self.categoria}'

    def listar_restaurantes():
        print(f'{'Nome do restaurante'} | {'Categoria'} | {'Status'}')
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante._nome} | {restaurante.categoria} | {restaurante.ativo}')
        
    @property
    def ativo(self):
        return 'verdadeiro' if self._ativo else 'false'

restaurante_praca = Restaurante('praça', 'gourmet')
restaurante_pizza = Restaurante('pizza', 'italiana')
Restaurante.listar_restaurantes()