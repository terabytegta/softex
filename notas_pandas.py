import pandas as pd

filepath = r"C:\notas\notas.csv"
df = pd.read_csv(filepath)
df = df.set_index('aluno')
media = (df["nota_1"] + df["nota_2"])/2
df["media"] = media

df.loc [df["media"] >= 7, "situação" ] = "Aprovado"
df.loc [df["faltas"] <= 5, "situação"] = "Aprovado"
df.loc [df["media"] < 7, "situação"] = "Reprovado"
df.loc [df["media"] > 5,"situação"] = "Reprovado"

m_falta = df['faltas'].max()
med_geral = df['media'].sum()
m_media = df['media'].max()
print(f'O maior número de faltas de um aluno: {m_falta}')
print(f'A média geral das notas: {med_geral/4}')
print(f'A maior média entre os alunos: {m_media}')

df.to_csv('alunos_situacao.csv')