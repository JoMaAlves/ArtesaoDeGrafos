# Documentação

# Sumário
1. [Estrutura de Dados](#1)
    * [main.py]()
    * [graph.py]()
    * [vertex.py]()
    * [prints.py]()

<a id="1" />
# Estrutura de Arquivos

<a id="1.1" />
## main.py
**Main** é o principal dos arquivos. Ao executar o sistema, é
este arquivo que primeiro é acionado e viabiliza a interação
com o usuário. Comporta-se de modo contínuo até que seja
forçado a interromper, assim o usuário pode executar as
diversas funcionalidades em sequência.

<a id="1.2" />
## graph.py
**Graph** comporta a classe do grafo, a principal em nosso
sistema, na qual todas as informações e características do
grafo são disponibilizadas. Sendo estas: adição de vértice,
arestas, imprimir o grafo, grau do vértice, checar adjacência
e lista de adjacência, ordem e tamanho.

<a id="1.3" />
## vertex.py
**Vertex** comporta a classe vértice, cujos atributos são: valor
e lista de arestas. Permite também a pesquisa interna por
informações cruciais.

<a id="1.4" />
## prints.py
**Prints** é o mecanismo de exibição do menu e todos os
pontos de interface no terminal. Com este arquivo é
possível ocorrer de fato a interação humano-computador, na
qual a máquina exibe as informações e o usuário
correlaciona em resposta. Há também o tratamento dos
dígitos de entrada.