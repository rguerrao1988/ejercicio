"""

num_b=int(input("numero del 0 al 10"))
lista=[5,9,2,7,1,6,8,1,3,4,0]

def busqueda(lista,num_b):
    for i in range(len(lista)):
        if lista[i]==num_b:
            return i
    return -1
    
    """

def saludar(nombre):
    print("hola",nombre)

saludar("ramon")