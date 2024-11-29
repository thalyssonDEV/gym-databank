CREATE TABLE plano (
	id_plano SERIAL PRIMARY KEY,
	nome_plano VARCHAR(50) NOT NULL,
	valor_plano NUMERIC NOT NULL,
	duracao_dias INT NOT NULL,
	descricao_plano VARCHAR(100) NOT NULL
);

CREATE TABLE usuario (
	id_usuario SERIAL PRIMARY KEY,
	cpf_usuario VARCHAR(50) UNIQUE NOT NULL,
	nome_usuario VARCHAR(100) NOT NULL,
	senha VARCHAR(50) NOT NULL,
	id_plano INT,
	FOREIGN KEY (id_plano) REFERENCES plano(id_plano),
	telefone VARCHAR(100) NOT NULL,
	data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE grupo_muscular (
	id_grupo SERIAL PRIMARY KEY,
	nome_grupo VARCHAR(100) NOT NULL
);

CREATE TABLE exercicio (
	id_exercicio SERIAL PRIMARY KEY,
	nome_exercicio VARCHAR(100) NOT NULL,
	id_grupo INT,
	FOREIGN KEY (id_grupo) REFERENCES grupo_muscular(id_grupo)
);

CREATE TABLE ficha (
	id_ficha SERIAL PRIMARY KEY,
	id_usuario INT NOT NULL,
	FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario),
	id_exercicio INT NOT NULL,
	FOREIGN KEY (id_exercicio) REFERENCES exercicio(id_exercicio),
	series INT NOT NULL,
	repeticoes INT NOT NULL
);
