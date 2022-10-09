from operator import truediv

cdt1=0
cdt2=0
cdt3=0
cdt4=0
cond=False

while cond==False:
    try:
        cdt=int(input(print("\nEscolha seu Candidato:")))
        if cdt==889:
           cdt1=(cdt1+1)
        elif cdt==847:
            cdt2=(cdt2+1)
        elif cdt==515:
            cdt3=(cdt3+1)
        elif cdt==0:
            cdt4=(cdt4+1)
        elif cdt!=889 and cdt!=847 and cdt!=515 and cdt!=0:
            print("numero invalido digite novamente!")
    except:
        print("opção invalida")
    cond1=False
    while cond1==False:
        cond1=False
        cond1=str(input(print("Digite S para encerrar ou qualquer tecla para continuar")))
        if cond1=='s':
            cond1=True
            cond=True
        elif cond1!="s":
            cond1=True
            
votos=(cdt1+cdt2+cdt3+cdt4)
if (cdt1>cdt2) and (cdt1>cdt3):
    print("-------------------Resultado da Apuração-----------------------")
    print("O candidato vencedor foi o candidato X com: ",cdt1, "votos")
    print("Total de votos:",votos)
    print("votos candidato y: ",cdt2)
    print("votos candidato z: ",cdt3)
    print("votos em branco: ",cdt4)
elif (cdt2>cdt3) and (cdt2>cdt1):
    print("-------------------Resultado da Apuração-----------------------")
    print("O candidato vencedor foi o candidato Y com: ",cdt2, "votos")
    print("Total de votos:",votos)
    print("votos candidato x: ",cdt1)
    print("votos candidato z: ",cdt3)
    print("votos em branco: ",cdt4)
elif(cdt1==cdt2) or (cdt1==cdt3) or (cdt2==cdt3):
    print("-------------------Resultado da Apuração-----------------------")
    print('Eleições serão definidas no segundo turno')
    print("Total de votos:",votos)
    print("votos candidato x: ",cdt1)
    print("votos candidato z: ",cdt3)
    print("votos em branco: ",cdt4)
else:
    print("-------------------Resultado da Apuração-----------------------")
    print("O candidato vencedor foi o candidato Y com: ",cdt3, "votos")
    print("Total de votos:",votos)
    print("votos candidato x: ",cdt1)
    print("votos candidato y: ",cdt2)
    print("votos em branco: ",cdt4)
    
