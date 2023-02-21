class Animal:
    def __int__(self, nome, idade, especie, cor, som):
        self.nome = nome
        self.idade = idade
        self.especie = especie
        self.cor = cor
        self.som = som
    def emitir_som(self):
        print(self.som)
    def mudar_cor(self, nova_cor):
        self.cor = nova_cor

class Elefante(Animal):
    def __init__(self, tamanho):
        self.tamanho = tamanho
    def trombar(self):
        print(self.som)
    def mudar_tamanho(self, novo_tamanho):
        self.tamanho = novo_tamanho

def dados_elefante():
    elefante.nome = input("Entre com o nome do Elefante: ")
    elefante.idade = int(input("Entre com a idade do Elefante: "))
    elefante.especie = input("Entre com a especie do Elefante: ")
    elefante.cor = input("Entre com a cor do Elefante: ")
    elefante.som = input("Entre com o som do Elefante: ")

elefante = Elefante(input("Entre com o tamanho do Elefante: "))
dados_elefante()

if(elefante.especie.upper() == "AFRICANO" and elefante.idade < 10):
    elefante.tamanho = "pequeno"
    elefante.som = "Paaah"
elif(elefante.especie.upper() == "AFRICANO" and elefante.idade >= 10):
    elefante.tamanho = "grande"
    elefante.som = "PAHHHHHH"

print("O elefante tem o porte", elefante.tamanho)
elefante.emitir_som()
