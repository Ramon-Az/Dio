-- Primeiro, criar a tabela original (se não existir)
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'usuarios')
BEGIN
  CREATE TABLE usuarios (
    id INT PRIMARY KEY IDENTITY(1,1),
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    data_nascimento DATE NOT NULL,
    endereco VARCHAR(100) NOT NULL
  );
END;

-- Criando nova tabela com estrutura atualizada
CREATE TABLE usuarios_nova (
  id INT PRIMARY KEY IDENTITY(1,1),
  nome VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL UNIQUE,
  data_nascimento DATE NOT NULL,
  endereco VARCHAR(255) NOT NULL
);

-- Migrando os dados
INSERT INTO usuarios_nova (nome, email, data_nascimento, endereco)
SELECT nome, email, data_nascimento, endereco FROM usuarios;

-- Excluindo tabela anterior
DROP TABLE usuarios;

-- Renomeando nova tabela (sintaxe SQL Server)
EXEC sp_rename 'usuarios_nova', 'usuarios';


-- OU OPÇÃO 2: Alterar tamanho da coluna diretamente (sem migrate)
-- ALTER TABLE usuarios ALTER COLUMN endereco VARCHAR(255);
