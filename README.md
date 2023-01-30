# Boas-vindas ao repositório do Inventory Reports

  <summary><strong>👨‍💻 O que foi desenvolvido</strong></summary><br />

  Esse projeto utiliza a Programação Orientada a Objetos para implementar um **gerador de relatórios** que recebe como entrada arquivos com dados de um estoque e gera, como saída, um relatório acerca destes dados.

  Esses dados de estoque poderão ser obtidos de diversas fontes:

  Caminho: inventory_report/data/opções_a_seguir

  - Através da importação de um arquivo `CSV`;

  - Através da importação de um arquivo `JSON`;

  - Através da importação de um arquivo `XML`.

  Além disso, o relatório final tem duas versões: **simples** e **completa**.

<details>
  <summary><strong>Antes de começar</strong></summary><br />

  1. **criar o ambiente virtual**

  ```bash
  $ python3 -m venv .venv
  ```

  2. **ativar o ambiente virtual**

  ```bash
  $ source .venv/bin/activate
  ```

  3. **instalar as dependências no ambiente virtual**

  ```bash
  $ python3 -m pip install -r dev-requirements.txt
  ```
</details>

<details>
  <summary><strong>🛼Executando o Projeto</strong></summary>
  
  O comando a ser executado será `inventory_report`. Para que ele funcione em seu ambiente é preciso antes instalar o próprio código como um pacote pip:
  <code>pip install .</code>

  Agora você poderá chamar o comando `inventory_report` passando seus argumentos:
  
  <code>inventory_report `argumento1` `argumento2`</code>

  - **argumento1** deve receber o caminho de um arquivo a ser importado. O arquivo pode ser um `csv`, `json` ou `xml`.

  - **argumento2** pode receber duas strings: `simples` ou `completo`, cada uma gerando o respectivo relatório.
  
  Outra opção é invocar o comando assim:

  <code>python3 -m inventory_report.main argumento1 argumento2</code>

</details>
