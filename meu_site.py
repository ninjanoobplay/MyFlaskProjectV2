from flask import Flask, Response, render_template, request, redirect, url_for , flash
from config import config
from flask_login import login_user, logout_user,login_required,LoginManager, UserMixin, fresh_login_required
from werkzeug.security import check_password_hash , generate_password_hash
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy


#Certifique-se de estar utilizando uma versão do python compativel com o Flask
#Ou Não Irá rodar,recomendo python 3.8.0

#Para Mais Informações, leia a documentação do Flask
app = Flask(__name__)
app.config.from_object(config['development'])

csrf=CSRFProtect()

db = SQLAlchemy(app)



login_manager_app=LoginManager(app)

@login_manager_app.user_loader
def get_user(user_id):
    return User.query.filter_by(id=user_id).first()


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    fullname = db.Column(db.String(255), unique=False, nullable=False)

    def __init__(self,username,password,fullname):
        self.username = username
        self.password = generate_password_hash(password)
        self.fullname = fullname

    def check_password(self, pwd):
        return check_password_hash(self.password, pwd)

@app.route("/")
def index():
    return redirect(url_for('login'))

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if not user or not user.check_password(password):
            flash("Usuário ou Senha Incorreta!")
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for('home'))

    return render_template ("auth/login.html")

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route("/home")
@login_required
@fresh_login_required
def home():
    return render_template ("auth/user_loged.html")
def status_401(error):
    return redirect(url_for('login'))
def status_404(error):
    return "<h1>Página Não Encontrada</h1>", 404

@app.route("/cadastrar", methods=['GET', 'POST'])
def cadastrar():
    if (request.method == 'POST') and (request.form['username']!= '' and len(request.form['username']) > 2) and (request.form['password'] != ''and len(request.form['password']) > 2) and (request.form['fullname'] != ''and len(request.form['fullname']) > 2):
        try:
            cadastrar_user = User(username=request.form['username'],password=request.form['password'],fullname=request.form['fullname'])
            db.session.add(cadastrar_user)
            db.session.commit()
            flash("Conta Criada Com Sucesso!")
            return redirect(url_for('login'))
        except Exception as e:
            print(e)
            flash("Usuário Já Existe!")
            return redirect(url_for('cadastrar'))
    #if request.method == "POST":

    #    flash("Conta Criada Com Sucesso!")
    #    return redirect(url_for('login'))
    return render_template("cadastrar.html")
# colocar o site no ar
if __name__ == "__main__":
    #app.config.from_object(config['development'])
    #app.config['SECRET_KEY'] = 'B!1weNAt1T^%kvhUI*S'
    #app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/flask_login'
    csrf.init_app(app)
    app.register_error_handler(401,status_401)
    app.register_error_handler(404,status_404)
    app.run()

    # servidor do heroku

