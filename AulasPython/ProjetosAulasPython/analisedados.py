# Passo 1: Importar a base de dados (tabela que vamos analisar)

import pandas as pd

tabela = pd.read_csv(r"C:\Users\shied\Downloads\Arquivo.csv") #diretorio do meu arquivo

# Passo 2: Visualizar a base de dados:
    # 2.1 - Entender as informações q vc tem disponível
    # 2.2 - Descobrir as cagadas da base de dados

# -> caso queira parar de ver uma coluna ou linha, usamos o comando:

tabela = tabela.drop("nome da coluna ou linha", axis = 1)
    # axis -> 0 = Linha; axis -> 1 = Coluna
print(tabela) # -> vai mostrar a tabela

# Passo 3: Tratamento de Dados
    # 3.1 - Resolver os valores que estão sendo reconhecidos de forma errada
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")

# errors="coerce" -> vai anular as letras nesse caso, deixando somente os números
# errors="ignore" -> vai ignorar os erros
# errors="raise" -> vai mostrar os erros pra mim

    # 3.2 - Resolver valores vazios:
        # Pra isso, eu vou excluir: COLUNAS em que TODOS os valores estão vazios:
tabela = tabela.dropna(how="all", axis=1)

# how="all" -> TODOS os valores vazios
# how="any" -> ALGUM valor vazio

# E linhas que tem PELO MENOS 1 valor vazio
tabela = tabela.dropna(how="any", axis=0)

#Passo 4: Análise inicial:
    # 4.1 - Primeiro, vamos analisar o que realmente nos interessa, que no caso da aula, foi a quantidade de pessoas que cancelaram a assinatura do serviço telefonico
print(tabela["Churn"].value_counts())

# pra visualizar essa contagem em forma de porcentagem:
print(tabela["Churn"].value_counts(normalize=True).map(lambda x: "{:.1%}".format(x)))

# Churn não é um comando, é o nome da coluna que estava na tabela e significa "cancelamento" 

# Passo 5: Analise Detalhada - descobrir as causas do cancelamento
    # 5.1 - Comparar cada coluna da base de dados com a coluna Churn (quem cancelou)
#pra isso, usamos outra biblioteca, pra poder criar gráficos, etc
import plotly.express as px

    # 5.2 - Crie o gráfico
coluna = "Nome da coluna q vc quer ver"
grafico = px.histogram(tabela, x=coluna, color="Churn", text_auto=True)

# color="Churn" -> serve pra poder diferenciar as colunas usando uma cor pra cada 

    # 5.3 - Exibe o gráfico
grafico.show()

# 5.4 - Se eu quiser comparar TODAS as colunas, posso criar um gráfico pra todas de uma só vez
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color="Churn", text_auto=True)
    grafico.show
