class vehiculo:
    def mover(self):
        pass

class coche(vehiculo):
    def mover(self):
        print("El coche se mueve por la calle")
        
class bicicleta(vehiculo):
    def mover(self):
        print("La bicicleta se mueve por la bicicenda")

def mover_vehiculo(vehiculos):
    for  vehiculo in vehiculos:
        vehiculo.mover()

if __name__=="__main__":
    vehiculos=[coche(),bicicleta(),coche(),bicicleta()]
    mover_vehiculo(vehiculos)
