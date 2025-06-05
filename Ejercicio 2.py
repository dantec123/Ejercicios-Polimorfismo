class animal:
    def hacer_sonido(self):
        pass

        
    
    
class perro(animal):
    def hacer_sonido(self):
        return "Guau"
    


class gato(animal):
    def hacer_sonido(self):
        return "Miau"


if __name__=="__main__":
    animales=[perro(),gato(),perro(),gato()]
    for animal in animales:
        print(animal.hacer_sonido())
