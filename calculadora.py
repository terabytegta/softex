def calculadora(num1,num2,op):
    if op==1:
        print(f'result: {num1+num2}')
    elif op==2:
        print(f'result: {num1-num2}')
    elif op==3:
        print(f'result: {num1*num2}')
    elif op==4:
        print(f'result: {num1/num2}')
    else:
        print('0')

print("Qual calculo deseja fazer")
print("1-soma / 2-subtração / 3-multiplicação / 4- divisão")
op=int(input("Digite a operação:"))
num1=float(input("Digite o primeiro numero:"))
num2=float(input("Digite o segundo numero:"))
calculadora (num1,num2,op)