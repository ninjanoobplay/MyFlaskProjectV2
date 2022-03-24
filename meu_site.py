import re
from unicodedata import name
from flask import Flask, render_template, request, redirect, url_for , flash
from config import config
from flask_mysqldb import MySQL
from flask_login import LoginManager,login_user,logout_user,login_required
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy

# Modelos
from models.ModelUser import ModelUser

# Entities
from models.entities.User import User

app = Flask(__name__)

csrf=CSRFProtect()
db = SQLAlchemy(app)
login_manager_app=LoginManager(app)

@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db,id)


@app.route("/")
def index():
    return redirect(url_for('login'))

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        #print(request.form['username'])
        #print(request.form['password'])

        user = User(0,request.form['username'],request.form['password'])
        logged_user=ModelUser.login(db,user)
        if not logged_user == None:
            if logged_user.password:
                login_user(logged_user)
                return redirect(url_for('home'))
            else:
                flash("Senha Incorreta...")
                return render_template ("auth/login.html")
        else:
            flash("Usuário Não Encontrado...")
            return render_template ("auth/login.html")
    else:
        return render_template ("auth/login.html")

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route("/home")
@login_required
def home():
    return render_template ("home.html")
def status_401(error):
    return redirect(url_for('login'))
def status_404(error):
    return "<h1>Página Não Encontrada</h1>", 404

@app.route("/cadastrar", methods=['GET', 'POST'])
def cadastrar():
    if request.method == "POST":
        flname = request.form['fullname']
        name= request.form['username']
        pwd= request.form['password']
        cursor=db.connection.cursor()
        sql=""" INSERT INTO user (username, password, fullname) VALUES({}, {}, {}) """.format(name, pwd, flname)
        db.session.add(sql)
        db.session.commit()


    #cadastrar_user = User(0,request.form['username'],request.form['password'],request.form['fullname'])
    #if request.method == "POST":
    #elif fullname and username and password:


    #    flash("Conta Criada Com Sucesso!")
    #    return redirect(url_for('login'))
    return render_template("cadastrar.html")
3
# colocar o site no ar
if __name__ == "__main__":
    app.config.from_object(config['development'])
    csrf.init_app(app)
    app.register_error_handler(401,status_401)
    app.register_error_handler(404,status_404)
    app.run()

    # servidor do heroku

