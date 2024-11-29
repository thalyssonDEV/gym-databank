import psycopg2
import bcrypt

def insert_user_into_db(cpf_usuario, nome_usuario, senha, telefone, id_plano):
    # Definir os parâmetros de conexão
    host = "localhost"  # ou o endereço do seu servidor PostgreSQL
    database = "gym_databank"  # o nome do seu banco de dados
    user = "postgres"  # o nome de usuário do PostgreSQL
    password = "95629740"  # a senha do usuário

    # Criptografando a senha
    hashed_password = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())

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

        query = """
        INSERT INTO usuario (cpf_usuario, nome_usuario, senha, telefone, id_plano)
        VALUES (%s, %s, %s, %s, %s);
        """
        cursor.execute(query, (cpf_usuario, nome_usuario, senha, telefone, id_plano))
        conn.commit()
        print('Usuário Registrado')

    except Exception as e:
        print(f"Erro ao Registrar Usuário: {e}")
    
    finally:
        if conn:
            cursor.close()
            conn.close()
        else:
            print('Erro ao Conectar ao Banco de Dados')