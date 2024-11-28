import psycopg2
from psycopg2 import sql

def connect_to_db():
    # Definir os parâmetros de conexão
    host = "localhost"  # ou o endereço do seu servidor PostgreSQL
    database = "xxxxxxx"  # o nome do seu banco de dados
    user = "xxxxxxx"  # o nome de usuário do PostgreSQL
    password = "xxxxxxxx"  # a senha do usuário

    # Conectando ao banco de dados PostgreSQL
    try:
        conn = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )
        print("Conexão Bem-Sucedida ao Banco de Dados!")

        # Criando um cursor para executar consultas
        cursor = conn.cursor()

        # Exemplo de consulta simples
        # cursor.execute("SELECT usuario.nome_usuario, plano.nome_plano FROM usuario inner join plano on plano.id_plano = usuario.id_plano")
        # cursor.execute("insert into grupo_muscular (nome_grupo) values ('biceps')")
        # cursor.execute("select * from grupo_muscular")
        # conn.commit()

        rows = cursor.fetchall()
        for row in rows:
            print(row)

        # Fechar a conexão
        cursor.close()
        conn.close()

    except Exception as e:
        print(f"Erro ao Conectar ao Banco de Dados: {e}")