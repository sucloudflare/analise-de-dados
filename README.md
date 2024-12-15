<h1>Histogramas, Gráficos e Ferramentas para Análise de Dados</h1>
</header>
<section>
<h2>Palavras Técnicas em Análise de Dados</h2>
<ul>
<li><strong>Distribuição:</strong> Como os valores estão espalhados em um conjunto de dados.<br>Exemplo: A distribuição das idades em uma turma mostra a quantidade de alunos em cada faixa etária.</li>
<li><strong>Correlação:</strong> A relação entre duas variáveis.<br>Exemplo: Se aumentar o investimento em marketing faz as vendas crescerem, essas variáveis têm uma correlação positiva.</li>
<li><strong>Outliers:</strong> Valores que fogem muito do padrão.<br>Exemplo: Em um grupo de pessoas que ganham entre R$2.000 e R$5.000, alguém ganhando R$50.000 seria um outlier.</li>
<li><strong>Tendência:</strong> Um padrão ou direção nos dados ao longo do tempo.<br>Exemplo: Aumento contínuo nas vendas ao longo dos meses.</li>
</ul>
</section>

<section>
<h2>Python: Explorando Gráficos com Pandas e Matplotlib</h2>
<p>Com Python, podemos transformar dados em gráficos de forma prática. Aqui está um exemplo simples de análise de correlação com Pandas e Matplotlib:</p>
<code>
import pandas as pd<br>
import matplotlib.pyplot as plt<br><br>

# Dados de exemplo<br>
dados = {<br>
    "Investimento Marketing": [1000, 1500, 2000, 2500, 3000],<br>
    "Vendas": [10, 20, 30, 35, 50]<br>
}<br>
df = pd.DataFrame(dados)<br><br>

# Correlação<br>
correlacao = df.corr()<br>
print("Correlação:")<br>
print(correlacao)<br><br>

# Gráfico de Dispersão (Scatter Plot)<br>
plt.scatter(df["Investimento Marketing"], df["Vendas"])<br>
plt.title("Correlação: Investimento em Marketing vs Vendas")<br>
plt.xlabel("Investimento Marketing")<br>
plt.ylabel("Vendas")<br>
plt.show()
</code>
<p><strong>O que este código faz?</strong></p>
<ul>
<li>Calcula a correlação entre investimento em marketing e vendas.</li>
<li>Gera um gráfico de dispersão para visualizar a relação.</li>
</ul>
</section>

<section>
<h2>Excel: Criando Gráficos e Análise</h2>
<p><strong>Passos no Excel:</strong></p>
<ol>
<li>Insira os dados em uma planilha (exemplo: colunas para investimento e vendas).</li>
<li>Use a fórmula <code>=CORREL(A2:A6, B2:B6)</code> para calcular a correlação.</li>
<li>Crie um gráfico de dispersão:
<ul>
<li>Selecione os dados.</li>
<li>Acesse Inserir &gt; Gráficos &gt; Dispersão.</li>
</ul>
</li>
</ol>
</section>

<section>
<h2>Power BI: Visualizando e Explorando Dados</h2>
<p><strong>Passos no Power BI:</strong></p>
<ol>
<li>Importe os dados (CSV ou Excel).</li>
<li>Use o painel de Visualizações para criar um gráfico de dispersão.</li>
<li>Configure os eixos:
<ul>
<li>Arraste "Investimento Marketing" para o eixo X.</li>
<li>Arraste "Vendas" para o eixo Y.</li>
</ul>
</li>
<li>Adicione um cartão de métrica para exibir a correlação manualmente calculada no DAX:</li>
</ol>
<code>
Correlação = CORREL(Tabela[Investimento Marketing], Tabela[Vendas])
</code>
</section>

<section>
<h2>Comparação: Python, Excel e Power BI</h2>
<table>
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
<td>Intuitivo e rápido de usar</td>
<td>Pouco eficiente para grandes dados</td>
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
<p>&copy; 2024 - Guia de Análise de Dados. Desenvolvido por Edson Bruno.</p>
</footer>
