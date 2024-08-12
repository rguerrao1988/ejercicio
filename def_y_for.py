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


def media(alun_1,alun_2,alun_3):
    print("la media de calificacion es:")
    return (alun_1 + alun_2 + alun_3)/3

resultado=media(int(input("calificacion # 1: ")),int(input("calificacion # 2: ")),int(input("calificacion # 3: ")))
print(resultado)