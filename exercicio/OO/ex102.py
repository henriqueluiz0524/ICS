'''
Crie uma classe Animal com um método som().
 Em seguida, crie uma classe derivada Gato que implemente o método som() retornando "Miau".
'''

class Animal:
    def som(self):
        return "Som de animal"

class Gato(Animal):
    def som(self):
        return "Miau"

gato = Gato()
print(gato.som())      