import random
def bubbleSort(numeros):
    el = len(numeros)-1
    troca = 0
    seq = False
    while seq == False:
        for i in range(el):
            if (numeros[i] > numeros[i+1]):
                troca = numeros[i]
                numeros[i] = numeros[i+1]
                numeros[i+1] = troca
                print (numeros)
    return numeros
numeros = []
for i in range(0,10,1):
    numeros.append(random.randint(0,100))
print(numeros)
bubbleSort(numeros)