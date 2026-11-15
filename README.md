# Contagem de Páginas de PDFs

Projeto desenvolvido em Python para automatizar a contagem de páginas de arquivos PDF presentes em uma pasta.

A aplicação identifica os arquivos PDF, realiza a leitura de cada documento, contabiliza suas páginas e gera automaticamente um relatório em formato `.txt` com os resultados.

## 🚀 Funcionalidades

- Identificação automática de arquivos PDF em uma pasta.
- Contagem individual de páginas de cada documento.
- Suporte a arquivos PDF com extensão em letras maiúsculas ou minúsculas.
- Tratamento de erros durante a leitura dos documentos.
- Tentativa de abertura de PDFs protegidos por senha vazia.
- Geração automática de relatório em arquivo TXT.
- Exibição dos resultados diretamente no terminal.
- Cálculo do total de páginas de todos os documentos processados com sucesso.

## 🛠️ Tecnologias utilizadas

- **Python 3.10+**
- **PyPDF:** biblioteca utilizada para leitura e manipulação de documentos PDF.
- **Pathlib:** manipulação de caminhos e diretórios.
- **Sys:** captura de argumentos fornecidos pelo terminal.

## 📁 Estrutura do projeto

```text
contagem-paginas-pdf/
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Instalação

1. Clone o repositório:

```bash
git clone https://github.com/Claudiohlm/contagem-paginas-pdf.git
```

2. Acesse a pasta do projeto:

```bash
cd contagem-paginas-pdf
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

## ▶️ Como utilizar

Existem duas maneiras de executar o programa.

### 1. Informando o caminho pelo terminal

Execute:

```bash
python main.py
```

O programa solicitará o caminho da pasta que contém os arquivos PDF.

### 2. Informando o caminho como argumento

```bash
python main.py "C:\Documentos\PDFs"
```

## 📄 Exemplo de resultado

Imagine uma pasta contendo três documentos:

- Documento_A.pdf
- Documento_B.pdf
- Documento_C.pdf

Após a execução, o programa exibirá o resultado:

```text
Documento_A 15 pag.
Documento_B 32 pag.
Documento_C 8 pag.

total: 55 pag.
```

O programa também criará automaticamente o arquivo `contagem_paginas.txt` dentro da pasta analisada.

## 📌 Observações

- O programa analisa somente os arquivos PDF diretamente presentes na pasta informada, sem percorrer subpastas.
- Arquivos que apresentarem erros durante a leitura serão identificados no relatório.
- O total de páginas considera apenas os documentos lidos com sucesso.
- O programa não remove nem modifica os arquivos PDF originais.
Estudante de Sistemas de Informação, com interesse em Python, automação de processos, análise de dados e desenvolvimento de soluções para otimização de tarefas.

- GitHub: [Claudiohlm](https://github.com/Claudiohlm)
