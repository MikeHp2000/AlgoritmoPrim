#REALIZAR CODIGO PARA ALGORITMO DE PRIM
#PROBAR PARA EL GRAFO DE 6 NODOS CON LA SIGUIENTE MATRIZ DE ADYACENCIA
#W = [0,1,3,10000,10000,2]
#    [1,0,3,6,10000,1]
#    [3,3,0,4,2,6]
#    [10000,6,4,0,5,11]
#    [10000,10000,2,5,0,7]
#    [2,1,6,11,7,0]
#PROBAR TAMBIEN PARA EL CASO VISTO EN CLASE


print("Ingrese la cantidad de vértices que desea que tenga el grafo: ", end="")
n = int(input())
print("La cantidad de vértices del grafo es", n)#¿

W=[]
peso = 0
for i in range(n):
    W.append([])
    for j in range(n):
        print("Ingrese los valores en la fila", i+1, " y la columna", j+1, "para la matriz de adyacencia:  ", end="")
        peso = int(input())
        W[i].append(peso)
    
    
F = []
minimo = 0
e = []
vcercano = 0
distArbol = 0

cercano = []
for i in range(n-1):
    cercano.append(0)


distancia = []
for i in range(n-1):
    distancia.append(0)

print(cercano, distancia)


for i in range(n-1):
    cercano[i] = 1
    distancia[i] = W[0][i+1]

print(cercano, distancia)


for m in range(n-1):
    minimo = 100000000
    e = []
    vcercano = 0
    for i in range(n-1):
        if (0 < distancia[i] < minimo):
            minimo = distancia[i]
            print(minimo)
            vcercano = i+2
            print(vcercano)
    print("minimo, vertice cercano")
    print(minimo, vcercano)

    distArbol = distArbol + minimo
    e.append((vcercano, cercano[vcercano-2]))
    F.append(e[0])
    print(" ")
    print("arista, conjuntoAristas")
    print(e, F)

    distancia[vcercano-2] = -1


    for i in range(n-1):
        print(" ")
        print("Wcercano, distancia i")
        print(W[i+1][vcercano-1], distancia[i])
        if (W[i+1][vcercano-1] < distancia[i]):
            print("entra_")
            distancia[i] = W[i+1][vcercano-1]
            cercano[i] = vcercano

    print(" ")
    print("cercano, distancia")
    print(cercano, distancia)

print(" ")
print("aristas del árbol")
print(F)
print("valor objetivo")
print(distArbol)
