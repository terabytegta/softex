class pet:
    nome_animal=''
    raca_animal=''
    idade_animal=''
    nome_resp=''
    tel_resp=''

def novo_pet():
    cad=pet()
    cad.nome_animal=input("Digite o nome do animal")
    cad.raca_animal=input("Digite a Raça")
    cad.idade_animal=input("Digite a Idade do seu Pet")
    cad.nome_resp=input("Digite o nome do Responsavel")
    cad.tel_resp=input("Digite o telefone do responsavel")
    return cad

