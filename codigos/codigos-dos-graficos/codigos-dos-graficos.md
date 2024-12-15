<header>
<h1>📊 Histogramas, Gráficos e Ferramentas para Análise de Dados</h1>
</header>

<main>
<section>
<h2>📋 Introdução</h2>
<p>Este guia apresenta como utilizar gráficos para interpretar dados utilizando ferramentas e bibliotecas como Python, Excel e Power BI. Vamos explorar histogramas, gráficos de dispersão, linhas de tendência e outras representações visuais.</p>
</section>

<section>
<h2>📊 Palavras Técnicas em Análise de Dados</h2>
<ul>
<li><strong>Distribuição:</strong> Como os valores estão espalhados em um conjunto de dados.</li>
<li><strong>Correlação:</strong> A relação entre duas variáveis.</li>
<li><strong>Outliers:</strong> Valores que fogem muito do padrão.</li>
<li><strong>Tendência:</strong> Um padrão ou direção nos dados ao longo do tempo.</li>
</ul>
</section>

<section>
<h2>Python: Explorando Gráficos com Pandas e Matplotlib</h2>
<p>Com Python, você pode criar gráficos de forma prática usando bibliotecas como Pandas e Matplotlib.</p>
<pre><code>import pandas as pd
import matplotlib.pyplot as plt

# Dados de exemplo
dados = {
    "Investimento Marketing": [1000, 1500, 2000, 2500, 3000],
    "Vendas": [10, 20, 30, 35, 50]
}
df = pd.DataFrame(dados)

# Correlação
correlacao = df.corr()
print("Correlação:")
print(correlacao)

# Gráfico de Dispersão
plt.scatter(df["Investimento Marketing"], df["Vendas"])
plt.title("Correlação: Investimento vs Vendas")
plt.xlabel("Investimento Marketing")
plt.ylabel("Vendas")
plt.show()</code></pre>
</section>

<section>
<h2>Excel: Criando Gráficos e Análise</h2>
<ol>
<li>Insira os dados em uma planilha.</li>
<li>Use a fórmula <code>=CORREL(A2:A6, B2:B6)</code> para calcular a correlação.</li>
<li>Crie um gráfico de dispersão selecionando os dados e indo em Inserir &gt; Gráficos &gt; Dispersão.</li>
</ol>
</section>

<section>
<h2>Power BI: Visualizando e Explorando Dados</h2>
<ol>
<li>Importe os dados (CSV ou Excel).</li>
<li>Use o painel de Visualizações para criar um gráfico de dispersão.</li>
<li>Configure os eixos arrastando "Investimento Marketing" para o eixo X e "Vendas" para o eixo Y.</li>
<li>Adicione um cartão de métrica com o DAX: <code>Correlação = CORREL(Tabela[Investimento Marketing], Tabela[Vendas])</code>.</li>
  </ol>
</section>

<section>
<h2>Comparação: Python, Excel e Power BI</h2>
<table border="1">
<thead>
<tr>
<th>Ferramenta</th>
<th>Uso</th>
<th>Vantagens</th>
<th>Limitações</th>
</tr>
</thead>
<tbody>
<tr>
<td>Python</td>
<td>Automação e personalização</td>
<td>Total controle e escalabilidade</td>
<td>Requer conhecimento de programação</td>
</tr>
<tr>
<td>Excel</td>
<td>Simples e visual</td>
<td>Intuitivo e rápido</td>
<td>Pouco eficiente para grandes volumes de dados</td>
</tr>
<tr>
<td>Power BI</td>
<td>Dashboards interativos</td>
<td>Conecta múltiplas fontes de dados</td>
<td>Requer licença Pro para recursos avançados</td>
</tr>
</tbody>
</table>
</section>

<footer>
<p>🚀 Resumo: Use Python para análises profundas e automatizadas, Excel para análises rápidas e Power BI para dashboards interativos.</p>
<p>👉 Qual ferramenta você usa mais no seu dia a dia? Deixe nos comentários!</p>
</footer>
</main>
