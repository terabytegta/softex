import time
iniciar=int(input("Digite a quantidade de segundos para a bombar explodir:"))
print("Inciando Contagem")
for i in range(iniciar,0,-1):
    print(i)
    time.sleep(1)
print("BOOMMM")