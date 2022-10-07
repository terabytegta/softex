teste = False
while teste==False:
    print("Digite Seu Nome Completo:")
    nome=str(input())
    print("Digite o ano que vc nasceu")
    ano=int(input())
    if (ano>=1921 and ano<=2021):
        idade=(2022-ano)
        print("Seu nome é",nome, ", e Idade é:", idade,)
        teste=True
    else:
        print("Dados Invalidos")
        print("Digite Novamente")

    
