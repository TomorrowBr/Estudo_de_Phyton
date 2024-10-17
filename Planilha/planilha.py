import pandas as pd

# Ler as duas planilhas Excel com caminho completo usando barras duplas
df1 = pd.read_excel('./planilha4.xlsx')
df2 = pd.read_excel('./planilha2.xlsx')

# Combinar os DataFrames, mantendo apenas os dados que estão em uma planilha e não na outra
combined_df = pd.concat([df1, df2]).drop_duplicates(keep=False)

# Salvar o resultado em uma nova planilha Excel usando barras duplas
combined_df.to_excel('./planilha_combinada.xlsx', index=False)

print("Dados combinados e salvos em 'planilha_combinada.xlsx'")