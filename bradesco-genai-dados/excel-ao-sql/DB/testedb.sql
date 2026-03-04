USE testedb;

CREATE TABLE usuarios (
    id INT IDENTITY(1,1) PRIMARY KEY,
    nome VARCHAR(100),
    email VARCHAR(100)
);

INSERT INTO usuarios (nome, email) VALUES
    ('Teste', 'teste2@email.com'),
    ('Teste 1', 'teste1@email.com'),
    ('Teste 2', 'teste2@email.com');


SELECT * FROM usuarios;

-- Análise do plano de execução
SET STATISTICS IO ON;
SET STATISTICS TIME ON;

SELECT * FROM usuarios WHERE nome = 'teste';

SET STATISTICS IO OFF;
SET STATISTICS TIME OFF;

-- índice criado para melhorar a performance da consulta
CREATE INDEX idx_nome ON usuarios(nome);
