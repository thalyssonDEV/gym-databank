CREATE TABLE plano (
	id_plano SERIAL PRIMARY KEY,
	nome_plano VARCHAR(50) UNIQUE NOT NULL,
	valor_plano FLOAT NOT NULL,
	descricao_plano VARCHAR(100) NOT NULL,
	id_plano INT,
	FOREIGN KEY (id_plano) REFERENCES plano(id_plano)
	)

CREATE TABLE usuario (
	id_usuario SERIAL PRIMARY KEY,
	cpf_usuario VARCHAR(50) UNIQUE NOT NULL,
	nome_usuario VARCHAR(100) NOT NULL,
	senha VARCHAR(50) NOT NULL
)

INSERT INTO plano (nome_plano, valor_plano, descricao_plano)
VALUES ('mensal',90,'1 mês, Sem Desconto')

INSERT INTO plano (nome_plano, valor_plano, descricao_plano)
VALUES ('bimestral',140,'2 meses, 22% OFF')

INSERT INTO plano (nome_plano, valor_plano, descricao_plano)
VALUES ('trimestral',175.50,'3 meses, 35% OFF')
  
INSERT INTO plano (nome_plano, valor_plano, descricao_plano)
VALUES ('semestral',324,'6 meses, 40% OFF')

INSERT INTO plano (nome_plano, valor_plano, descricao_plano)
VALUES ('anual',540,'1 ano, 50% OFF')
