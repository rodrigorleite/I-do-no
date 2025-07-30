-- Criação de tabela

Create Table usuario(
    id Int Primary Key Auto_Increment Not Null,
    nome Varchar(45),
    cpf Varchar(15),
    email Varchar(45),
    senha Varchar(45)
);


-- Alterar dados da tabela
Update usuario SET "Alice", email="alice@gmail.com" Where id=2;

-- Excluir dado
Delete FROM usuario Where id=2;

-- Selecionar todos os registros
SELECT nome, cpf FROM usuario;

-- Seleciona todas as colunas com o nome marlon no banco
SELECT * FROM usuario Where nome LIKE "marlon";

SELECT * FROM usuario WHERE id BETWEEN 1 AND 3 ORDER BY nome;

Insert Into usuario (nome,cpf,email, senha) Values
('Leno Brega', '123.123.123-12', 'lenobrega@gmail.com', '123'),
('Joana', '321.321.321-32', 'joana10@gmail.com', '321');

Create Table regiao(
    Id Int Primary Key Not Null Auto_Increment,
    nome Varchar(45)
);
Insert Into regiao (nome) Values
('Noroeste'),
('sul');    

-- 

CREATE TABLE cidade(
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    nome VARCHAR(45) NOT NULL,
    cep VARCHAR(45),
    estado CHAR(2),
    id_regiao_fk INT,
    FOREIGN KEY (id_regiao_fk) REFERENCES regiao(id)
);
INSERT INTO cidade(nome, cep, estado, id_regiao_fk) VALUES
('Nova Londrina', '87970-000', 'PR', '1'),
('Marilena', '87960-000', 'PR', '1'),
('Palmas', '85555-000', 'PR', '2');


CREATE TABLE ponto_focal (
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    nome VARCHAR(45),
    razao_social VARCHAR(45),
    tipo VARCHAR(45),
    cnpj_cpf VARCHAR(255),
    endereco VARCHAR(45),
    telefone VARCHAR(45),
    celular VARCHAR(45),
    email VARCHAR(45),
    id_cidade_fk INT,
    FOREIGN KEY (id_cidade_fk) REFERENCES cidade(id)
);
INSERT INTO ponto_focal (nome, razao_social, tipo, cnpj_cpf, endereco, telefone, celular, email, id_cidade_fk) VALUES
('TecInc', 'TecInc LTDA', 'Privada', '12.345.678/9012-34', 'Rua da agua, 444','4002-8922', '(955) 1234-5678', 'tecinc@gmail.com', 1),
('Tecnologi', 'Tecnoligi LTDA', 'Privada', '12.345.678/9012-34', 'Rua da agua, 355', '4002-8922', '(955) 1234-5678', 'tecnologi@gmail.com', 2);


CREATE TABLE area(
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    nome VARCHAR(15) NOT NULL,
    numero INT
);
INSERT INTO area(nome, numero) VALUES
('Tecnologi', 010101),
('Gastromia', 020202),
('Garoto de Programa', 020202);

CREATE TABLE venda(
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    data DATE,
    origem VARCHAR(255),
    obs VARCHAR(255),
    id_ponto_focal_fk INT,
    id_area_fk INT,
    FOREIGN KEY (id_ponto_focal_fk) REFERENCES ponto_focal(id),
    FOREIGN KEY (id_area_fk) REFERENCES area(id)
);

SELECT cidade.nome, area.nome FROM cidade 
INNER JOIN ponto_focal
ON cidade.id = ponto_focal.id_cidade_fk
INNER JOIN venda
ON ponto_focal.id = venda.id_ponto_focal_fk
INNER JOIN area
ON area.id = venda.id_area_fk;

SELECT + FROM ponto_focal
WHERE tipo Like 'privada';