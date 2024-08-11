
lista=[1,2,5,4,9,8,7,6]
elemento=7
def busqueda(lista,elemento):
    for i in range(len(lista)):
        print(i)
        if lista[i] == elemento:
            return i
    return -5
resultado =busqueda(lista,elemento)
if resultado != -5:
    print(f"elemento {elemento} se encuentra en la posicion {resultado}")
else:
    print(f"el elemento{elemento} no se encuentra en la lista")    
    