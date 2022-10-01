nome=(input("Digite seu Nome:"))
N_T01=float(input("Digite a primeira Nota:"))
N_T02=float(input("Digite a segunda Nota:"))
Faltas=int(input("Digite a qnt de Faltas:"))
Media=((N_T01+N_T02)/2)
if Media>=7 and Faltas<3:
    print("Aluno: "+nome+" Foi Aprovado com Media",+Media, )
else:
    print("Aluno: "+nome+" Foi Reprovado")


