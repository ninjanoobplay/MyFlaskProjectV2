from meu_site import db,User
from werkzeug.security import check_password_hash , generate_password_hash

def deletar_user():
    escolha = str(input("Digite o Usuário que quer apagar: "))
    usuario_object = User.query.filter_by(username = escolha).first()
    try:
        db.session.delete(usuario_object)
        db.session.commit()
    except Exception as error:
        print(error)

def adicionar_user():
    print('CADASTRO')
    user_name = str(input("Digite Um Usuário: "))
    pwd = str(generate_password_hash(input("Digite Uma Senha: ")))
    full_name = str(input("Digite Seu Nome: "))
    usuario_object = User(username=user_name,password=pwd,fullname=full_name)
    try:
        db.session.add(usuario_object)
        db.session.commit()
    except Exception as error:
        print(error)

# Para Apagar algum usuario do banco de dados que vc tem certeza que existe basta chamar "deletar_user()"
#deletar_user()
# Para Adicionar Um Usuario ao banco de dados basta chamar"adicionar_user()"
#adicionar_user()