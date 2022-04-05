# MyFlaskProject.V2

Nesse Projeto que é um Complemento com o Primeiro

Eu Adicionei Um Banco De Dados Para Fazer Cadastro/Login,Está funcionando perfeitamente!

# Instalações Necessárias:

Recomendo Uma Versão Do Python Compativel com o Flask Para Não Ter Nenhum Problema

Eu Estou Utilizando a Versão 3.8.0, Caso Queira Baixar

Basta Clicar no Icone Abaixo Para Ser Redirecionado:

[![Python 3.8.0 Download](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/release/python-380/)

Para Testes No Banco De Dados no LocalHost Utilize o XAMPP e ative o  Apache e MySQL.

<img align="center" src="https://github.com/ninjanoobplay/MyFlaskProjectV2
/blob/main/imgs/XAMPPstart.png"/>

Caso Não queira usar o LocalHost e queira usar seu proprio banco de dados

Basta Passar as Infomações de Conexão No Arquivo `config.py`

Da Seguinte Maneira:

```
SQLALCHEMY_DATABASE_URI = 'mysql://username:password@server/db'
```

Ou

```
SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
```

**Obs:Recomendo Utilizar Um Ambiente Virtual**

Abra o Terminal, Vá Para a Pasta Do Seu Projeto e Digite:

Para Windows:
```
python -m venv venv
```
Para Linux:
```
python3 -m venv venv
```

Pronto Agora Para Rodar o Programa Primeiro Vamos Ativar Nosso Ambiente Virtual:
```
venv\Scripts\activate
```
Caso queira sair só digitar:
```
deactivate
```
Obs: `venv` Foi o Nome que escolhemos logo em cima, E Certifique de estar na pasta do projeto!

Logo Em Seguida  Ja Pode Baixar Todas as Dependencias Para Esse Projeto com o Comando:
```
pip install -r requirements.txt
```

E Para Iniciar o Projeto

Para Windows:
```
python meu_site.py
```
Para Linux:
```
python3 meu_site.py
```

## Imagens do Layout Que Estou Utilizando:

### Login:

<img align="center" src="https://github.com/ninjanoobplay/MyFlaskProjectV2
/blob/main/imgs/LayoutLogin.png" width="600"/>

### Cadastro:

<img align="center" src="https://github.com/ninjanoobplay/MyFlaskProjectV2
/blob/main/imgs/LayoutCadastro.png" width="600"/>

## Como Abrir Esse Projeto Para Modificar e Testar:

Recomendo Um Pouco de Conhecimento com Flask, Caso Queira Modificar Algo, Mas no HTML Vocês Podem Testar O layout de vocês Sem Problema

Basta Editar e deixar o mesmo nome do arquivo que  está na pasta **Static**, ou se quiser alterar o nome basta modificar o **meu_site.py**

Procurar a Linha que faz o link com o arquivo HTML que você quer editar, como na imagem abaixo:

<img align="center" src="https://github.com/ninjanoobplay/MyFlaskProjectV2
/blob/main/imgs/EditLineHtml.png" width="400"/>

***É Basicamente Isso,Obrigado!***
