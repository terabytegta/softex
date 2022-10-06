def calculadora(num1,num2,op):
    if op==1:
        print(f'result: {num1+num2}')
    elif op==2:
        print(f'result: {num1-num2}')
    elif op==3:
        print(f'result: {num1*num2}')
    elif op==4:
        print(f'result: {num1/num2}')
op=1
while op:
    print("1-soma / 2-subtração / 3-multiplicação / 4- divisão / 5-Sair")
    op=int(input("Digite a operação:"))
    if (op>=1 and op<=4):
        num1=float(input("Digite o primeiro numero:"))
        num2=float(input("Digite o segundo numero:"))
        calculadora (num1,num2,op)
    elif op==5:
        print("Calculadora encerrada")
        exit()
    else:
        print("Opção invalida")