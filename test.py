from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuração do banco de dados PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://seu_usuario:sua_senha@localhost:5432/seu_banco_de_dados'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Definindo os modelos de banco de dados (equivalente às suas tabelas SQL)

class Plano(db.Model):
    __tablename__ = 'plano'
    id_plano = db.Column(db.Integer, primary_key=True)
    nome_plano = db.Column(db.String(50), nullable=False)
    valor_plano = db.Column(db.Numeric, nullable=False)
    duracao_dias = db.Column(db.Integer, nullable=False)
    descricao_plano = db.Column(db.String(100), nullable=False)

    # Relacionamento com a tabela usuario
    usuarios = db.relationship('Usuario', backref='plano', lazy=True)

class Usuario(db.Model):
    __tablename__ = 'usuario'
    id_usuario = db.Column(db.Integer, primary_key=True)
    cpf_usuario = db.Column(db.String(50), unique=True, nullable=False)
    nome_usuario = db.Column(db.String(100), nullable=False)
    senha = db.Column(db.String(50), nullable=False)
    telefone = db.Column(db.String(100), nullable=False)
    data_cadastro = db.Column(db.TIMESTAMP, default=db.func.current_timestamp())
    id_plano = db.Column(db.Integer, db.ForeignKey('plano.id_plano'))

    # Relacionamento com a tabela ficha
    fichas = db.relationship('Ficha', backref='usuario', lazy=True)

class GrupoMuscular(db.Model):
    __tablename__ = 'grupo_muscular'
    id_grupo = db.Column(db.Integer, primary_key=True)
    nome_grupo = db.Column(db.String(100), nullable=False)

    # Relacionamento com a tabela exercicio
    exercicios = db.relationship('Exercicio', backref='grupo_muscular', lazy=True)

class Exercicio(db.Model):
    __tablename__ = 'exercicio'
    id_exercicio = db.Column(db.Integer, primary_key=True)
    nome_exercicio = db.Column(db.String(100), nullable=False)
    id_grupo = db.Column(db.Integer, db.ForeignKey('grupo_muscular.id_grupo'))

    # Relacionamento com a tabela ficha
    fichas = db.relationship('Ficha', backref='exercicio', lazy=True)

class Ficha(db.Model):
    __tablename__ = 'ficha'
    id_ficha = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=False)
    id_exercicio = db.Column(db.Integer, db.ForeignKey('exercicio.id_exercicio'), nullable=False)
    ordem_exercicio = db.Column(db.Integer, nullable=False)
    series = db.Column(db.Integer, nullable=False)
    repeticoes = db.Column(db.Integer, nullable=False)

# Rotas para interagir com o banco de dados

@app.route('/planos', methods=["GET"])
def listar_planos():
    planos = Plano.query.all()
    return render_template('planos.html', planos=planos)

@app.route('/usuarios', methods=["GET", "POST"])
def cadastrar_usuario():
    if request.method == "POST":
        cpf = request.form["cpf"]
        nome = request.form["nome"]
        senha = request.form["senha"]
        telefone = request.form["telefone"]
        id_plano = request.form["id_plano"]

        novo_usuario = Usuario(
            cpf_usuario=cpf, 
            nome_usuario=nome, 
            senha=senha, 
            telefone=telefone, 
            id_plano=id_plano
        )
        db.session.add(novo_usuario)
        db.session.commit()
        return redirect(url_for("listar_usuarios"))

    planos = Plano.query.all()
    return render_template("cadastro_usuario.html", planos=planos)

@app.route('/usuarios', methods=["GET"])
def listar_usuarios():
    usuarios = Usuario.query.all()
    return render_template('usuarios.html', usuarios=usuarios)

@app.route('/fichas', methods=["GET", "POST"])
def cadastrar_ficha():
    if request.method == "POST":
        id_usuario = request.form["id_usuario"]
        id_exercicio = request.form["id_exercicio"]
        ordem_exercicio = request.form["ordem_exercicio"]
        series = request.form["series"]
        repeticoes = request.form["repeticoes"]

        nova_ficha = Ficha(
            id_usuario=id_usuario, 
            id_exercicio=id_exercicio,
            ordem_exercicio=ordem_exercicio,
            series=series,
            repeticoes=repeticoes
        )
        db.session.add(nova_ficha)
        db.session.commit()
        return redirect(url_for("listar_fichas"))

    usuarios = Usuario.query.all()
    exercicios = Exercicio.query.all()
    return render_template("cadastro_ficha.html", usuarios=usuarios, exercicios=exercicios)

@app.route('/fichas', methods=["GET"])
def listar_fichas():
    fichas = Ficha.query.all()
    return render_template('fichas.html', fichas=fichas)

if __name__ == '__main__':
    app.run(debug=True)
