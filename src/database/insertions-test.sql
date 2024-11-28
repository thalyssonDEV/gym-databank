-- Inserindo dados na tabela 'plano'
INSERT INTO plano (nome_plano, valor_plano, duracao_dias, descricao_plano)
VALUES ('mensal',90,30,'1 mês, Sem Desconto');

INSERT INTO plano (nome_plano, valor_plano, duracao_dias, descricao_plano)
VALUES ('bimestral',140,60,'2 meses, 22% OFF');

INSERT INTO plano (nome_plano, valor_plano, duracao_dias, descricao_plano)
VALUES ('trimestral',175.50,90,'3 meses, 35% OFF');
  
INSERT INTO plano (nome_plano, valor_plano, duracao_dias, descricao_plano)
VALUES ('semestral',324,180,'6 meses, 40% OFF');

INSERT INTO plano (nome_plano, valor_plano, duracao_dias, descricao_plano)
VALUES ('anual',540,360,'1 ano, 50% OFF');

-- Inserindo dados na tabela 'grupo_muscular'
INSERT INTO grupo_muscular (nome_grupo)
VALUES 
    ('Bíceps'),
    ('Ombro'),
    ('Peitoral'),
    ('Costas'),
    ('Tríceps'),
    ('Panturrilha'),
    ('Quadríceps'),
    ('Posterior de Coxa'),
    ('Antebraço'),
    ('Glúteo');

-- Inserindo dados na tabela 'usuario'
INSERT INTO usuario (cpf_usuario, nome_usuario, senha, id_plano, telefone)
VALUES 
    ('067.566.234-56', 'Thalysson', '12345678@lindo', 1, '(86) 9576-2070'),
    ('012.345.678-90', 'João Silva', 'senha123', 2, '(86) 9876-5432'),
    ('098.765.432-10', 'Maria Oliveira', 'senha321', 3, '(86) 9922-3344');

-- Inserindo dados na tabela 'exercicio' (Agora garantindo a ordem correta)
INSERT INTO exercicio (nome_exercicio, id_grupo)
VALUES 
    ('Rosca direta', 1),   -- Bíceps
    ('Desenvolvimento', 2), -- Ombro
    ('Supino reto', 3),    -- Peitoral
    ('Puxada frontal', 4), -- Costas
    ('Tríceps testa', 5),  -- Tríceps
    ('Panturrilha em pé', 6), -- Panturrilha
    ('Leg press', 7),      -- Quadríceps
    ('Cadeira flexora', 8), -- Posterior de Coxa
    ('Rosca martelo', 9);  -- Antebraço

-- Inserindo dados na tabela 'ficha' (Agora com id_exercicio correto)
INSERT INTO ficha (id_usuario, ordem_exercicio, id_exercicio, series, repeticoes)
VALUES 
    (1, 1, 1, 3, 12),  -- Thalysson, Rosca direta, 3 séries de 12 repetições
    (1, 2, 3, 4, 10),  -- Thalysson, Supino reto, 4 séries de 10 repetições
    (2, 1, 2, 4, 8),   -- João Silva, Desenvolvimento, 4 séries de 8 repetições
    (2, 2, 5, 3, 15),  -- João Silva, Tríceps testa, 3 séries de 15 repetições
    (3, 1, 4, 5, 12),  -- Maria Oliveira, Puxada frontal, 5 séries de 12 repetições
    (3, 2, 7, 4, 10);  -- Maria Oliveira, Leg press, 4 séries de 10 repetições