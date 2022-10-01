rodas=int(input("Digite a quantidade de Rodas:"))
peso=float(input("Digite o Peso do Veiculo:"))
pessoas=int(input("Quantas Pessoas ele Comporta:"))

if rodas<=3 :
    print("Categoria A")
elif rodas>=4 and pessoas>=8 :
    print("Categoria D")
elif rodas==4 and peso<=3500 and pessoas<=8 :
    print("Categoria B")
elif rodas>=4 and peso>3500 and peso<6000 :
    print("Categoria C")
else :
    print("Categoria E")