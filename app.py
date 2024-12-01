from flask import Flask, render_template, request, redirect, url_for
import psycopg2
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'connection'))
from connection import insert_user_into_db

app = Flask(__name__)

@app.route('/')
def home() -> None:
    return render_template('index.html')

@app.route('/usuarios', methods=['POST'])
def register_user() -> str:
    # Pega os dados do formulário
    cpf_usuario = request.form['cpf_usuario']
    nome_usuario = request.form['nome_usuario']
    senha = request.form['senha']
    telefone = request.form['telefone']
    id_plano = request.form['id_plano']

    print(f"\033[32mDados recebidos: CPF={cpf_usuario}, Nome={nome_usuario}, Senha={senha}, Telefone={telefone}, ID_Plano={id_plano}\033[0m")

    insert_user_into_db(cpf_usuario, nome_usuario, senha, telefone, id_plano)

    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)