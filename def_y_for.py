

num_b=int(input("numero a consultar? "))
# ind  0 1 2 3 4 5 6 7 8 9 10
lista=[5,9,2,7,1,6,8,1,3,4,0]

def busqueda(lista,num_b):
    for i in range(len(lista)):
        if lista[i]==num_b:
            return i    
resul_busqueda= busqueda(lista,num_b)
if resul_busqueda == num_b:

    print(f"elemento se encuentra en el indice: {resul_busqueda}")    
else:
    print("elemento digitado no encontrado") 




def saludar(nombre):
    print("hola",nombre)

saludar("ramon")
#ejemplo  



def media(alun_1,alun_2,alun_3):
    print("la media de calificacion es:")
    return (alun_1 + alun_2 + alun_3)/3

resultado=media(int(input("calificacion # 1: ")),int(input("calificacion # 2: ")),int(input("calificacion # 3: ")))
print(resultado)

# ejemplo


def resta(num_1=3,nume_2=2):
    return num_1 - nume_2
total=resta()
print(total)