CREATE TABLE usuarios (
  id INT PRIMARY KEY IDENTITY(1,1),
  nome VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL UNIQUE,
  data_nascimento DATE NOT NULL,
  endereco VARCHAR(255) NOT NULL
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
  status VARCHAR(255) DEFAULT 'pendente',
  FOREIGN KEY (id_usuario) REFERENCES usuarios(id),
  FOREIGN KEY (id_destino) REFERENCES destinos(id)
);

-- Inserts --
INSERT INTO usuarios (nome, email, data_nascimento, endereco) VALUES 
(1, 'João Silva', 'joao@example.com', '1990-05-15', 'Rua A, 123, Cidade X, Estado Y'),
(2, 'Maria Santos', 'maria@example.com', '1985-08-22', 'Rua B, 456, Cidade Y, Estado Z'),
(3, 'Pedro Souza', 'pedro@example.com', '1998-02-10', 'Avenida C, 789, Cidade X, Estado Y');

INSERT INTO destinos (nome, descricao) VALUES 
(1, 'Praia das Tartarugas', 'Uma bela praia com areias brancas e mar cristalino'),
(2, 'Cachoeira do Vale Verde', 'Uma cachoeira exuberante cercada por natureza'),
(3, 'Cidade Histórica de Pedra Alta', 'Uma cidade rica em história e arquitetura');

INSERT INTO reservas (id_usuario, id_destino, data, status) VALUES 
(1, 2, '2023-07-10', 'confirmada'),
(2, 1, '2023-08-05', 'pendente'),
(3, 3, '2023-09-20', 'cancelada');

-- Selects --
SELECT * FROM usuarios;
SELECT nome, email FROM usuarios;
SELECT * FROM usuarios WHERE nome = 'João Silva';
SELECT * FROM usuarios WHERE data_nascimento < '1990-01-01';
