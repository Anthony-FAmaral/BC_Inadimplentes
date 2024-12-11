import pandas as pd

#Codificar string descinhecidos da fonte
dados = 'planilha_202407.csv'
import chardet
with open('planilha_202407.csv', 'rb') as f:
    data = f.read()

encoding_result = chardet.detect(data)
encoding = encoding_result['encoding']
print("Detected Encoding:", encoding)

# Datafrime
bccredito = pd.read_csv('planilha_202407.csv', encoding=encoding, sep=';')
print(bccredito.head())

#Analisando dados Null´s
bccredito.isnull().sum()

bccredito.fillna('N/A', inplace=True)

dados_importante = bccredito.drop(columns=[])

# Exibe as primeiras linhas do novo DataFrame
print(dados_importante.head())

# Escolhendo as variaveis principais para Analise
dados_importante = bccredito[['uf','ocupacao', 'modalidade', 'porte', 'vencido_acima_de_15_dias', 'carteira_inadimplida_arrastada']]

dados_importante.head()

#ETL
dados_importante['modalidade'].value_counts()

dados_importante['modalidade']= dados_importante['modalidade'].str.replace('PJ - ', '')
dados_importante['modalidade']= dados_importante['modalidade'].str.replace('PF - ', '')
print(dados_importante)

dados_importante['porte']= dados_importante['porte'].str.replace('PJ - ', '')
dados_importante['porte']= dados_importante['porte'].str.replace('PF - ', '')
print(dados_importante)

dados_importante['ocupacao']= dados_importante['ocupacao'].str.replace('PJ - ', '')
dados_importante['ocupacao']= dados_importante['ocupacao'].str.replace('PF - ', '')
print(dados_importante)

dados_importante.head()

#Dados tratados
dados_importante.to_csv('dados_importantes_tratados.csv')