USE testedb;

CREATE TABLE usuarios (
  id INT PRIMARY KEY IDENTITY(1,1),
  nome VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL UNIQUE,
  data_nascimento DATE NOT NULL,
  endereco VARCHAR(100) NOT NULL
);

CREATE TABLE destinos (
  id INT PRIMARY KEY IDENTITY(1,1),
  nome VARCHAR(255) NOT NULL UNIQUE,
  descricao VARCHAR(255) NOT NULL
);

CREATE TABLE reservas (
  id INT PRIMARY KEY IDENTITY(1,1),
  id_usuario INT,
  id_destino INT,
  data DATE,
  status VARCHAR(255) DEFAULT 'pendente'
);

-- Chaves estrangeiras --

-- Adicionando chave estrangeira na tabela "reservas" referenciando "usuarios"
ALTER TABLE reservas
ADD CONSTRAINT fk_reservas_usuarios
FOREIGN KEY (id_usuario) REFERENCES usuarios(id)
ON DELETE CASCADE;

-- Adicionando chave estrangeira na tabela "reservas" referenciando "destinos"
ALTER TABLE reservas
ADD CONSTRAINT fk_reservas_destinos
FOREIGN KEY (id_destino) REFERENCES destinos(id)
ON DELETE CASCADE;
