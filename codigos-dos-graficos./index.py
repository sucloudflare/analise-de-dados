import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Configurando os dados de exemplo
dados = {
    "Investimento Marketing": [1000, 1500, 2000, 2500, 3000],
    "Vendas": [10, 20, 30, 35, 50],
    "Região": ["Norte", "Sul", "Leste", "Oeste", "Norte"]
}
df = pd.DataFrame(dados)

# 1. Histogramas
def gerar_histograma():
    plt.hist(df["Vendas"], bins=5, color='skyblue', edgecolor='black')
    plt.title("Histograma das Vendas")
    plt.xlabel("Vendas")
    plt.ylabel("Frequência")
    plt.show()

# 2. Gráfico de dispersão
def gerar_grafico_dispersao():
    plt.scatter(df["Investimento Marketing"], df["Vendas"], color='green')
    plt.title("Investimento vs Vendas")
    plt.xlabel("Investimento em Marketing")
    plt.ylabel("Vendas")
    plt.grid(True)
    plt.show()

# 3. Gráfico de linha com tendência
def gerar_grafico_linha():
    plt.plot(df["Investimento Marketing"], df["Vendas"], marker='o', color='blue')
    plt.title("Tendência: Investimento em Marketing vs Vendas")
    plt.xlabel("Investimento em Marketing")
    plt.ylabel("Vendas")
    plt.grid(True)
    plt.show()

# 4. Gráfico de boxplot
def gerar_boxplot():
    sns.boxplot(data=df["Vendas"], color="orange")
    plt.title("Boxplot das Vendas")
    plt.show()

# 5. Heatmap de correlação
def gerar_heatmap():
    correlacao = df.corr()
    sns.heatmap(correlacao, annot=True, cmap="coolwarm")
    plt.title("Mapa de Correlação")
    plt.show()

# 6. Gráfico de barras
def gerar_grafico_barras():
    df.groupby("Região")["Vendas"].sum().plot(kind='bar', color='purple')
    plt.title("Vendas por Região")
    plt.xlabel("Região")
    plt.ylabel("Total de Vendas")
    plt.show()

# Execução das funções
if __name__ == "__main__":
    print("1. Histograma")
    gerar_histograma()

    print("2. Gráfico de Dispersão")
    gerar_grafico_dispersao()

    print("3. Gráfico de Linha")
    gerar_grafico_linha()

    print("4. Boxplot")
    gerar_boxplot()

    print("5. Heatmap de Correlação")
    gerar_heatmap()

    print("6. Gráfico de Barras")
    gerar_grafico_barras()
