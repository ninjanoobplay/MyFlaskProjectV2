from meu_site import db
#Esse comando abaixo simplesmente cria todas as tabelas que eu pedi no arquivo meu_site.py
#Na classe User(db.Model, UserMixin) Caso você não tenha um banco de dados recomendo pesquisar sobre
#Obs: É importante criar um DB Com o Mesmo Nome colocado em config.py
#Antes de executar o comando ou não irá funcionar
db.create_all()