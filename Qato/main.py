from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
import getpass

password = getpass.getpass("Password: ")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:'+password+'@20.168.54.19/Qato'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class ONG(db.Model):
    id_ong = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), unique=True, nullable=False)
    descricao = db.Column(db.String(200), nullable=False)
    cnpj = db.Column(db.Integer, unique=True, nullable=False)
    tipo = db.Column(db.String(52), nullable=False)
    telefone = db.Column(db.Integer, unique=True, nullable=False)
    email = db.Column(db.String(50), nullable=False)

    def __init__(self, nome, descricao, cnpj, tipo, telefone, email):
        self.nome = nome
        self.descricao = descricao
        self.cnpj = cnpj
        self.tipo = tipo
        self.telefone = telefone
        self.email = email


@app.route('/')
def home():
    return '<a href="/cadastrarong"><button> Cadastrar ONG </button></a>'


@app.route("/cadastrarong")
def cadastrarong():
    return render_template("index.html")


@app.route("/ongadicionada", methods=['POST'])
def ongadicionada():
    nome = request.form["nome"]
    descricao = request.form["descricao"]
    cnpj = request.form["cnpj"]
    tipo = request.form["tipo"]
    telefone = request.form["telefone"]
    email = request.form["email"]

    entry = ONG(nome, descricao, cnpj, tipo, telefone, email)

    db.session.add(entry)

    ''' 
    deletar ong
    from sqlalchemy import select, update, delete, values
    deletarOng = delete(ONG).where(ONG.id_ong == 3)
    db.session.execute(deletarOng)
    db.session.commit()

    '''

    db.session.commit()

    return render_template("index.html")


if __name__ == '__main__':
    db.create_all()
    app.run()