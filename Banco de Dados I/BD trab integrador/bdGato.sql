create database gato_caolho;
\c gato_caolho
set datestyle to 'ISO,DMY';

-- ##########################################################################################################################################################
-- CREATE TABLES
-- ##########################################################################################################################################################
CREATE TABLE IF NOT EXISTS "usuario" (
  "id_usuario" SERIAL PRIMARY KEY,
  "nome" VARCHAR(100) NOT NULL,
  "cpf" VARCHAR(20) NOT NULL UNIQUE,
  "senha" VARCHAR(100) NOT NULL,
  "email" VARCHAR(256) NOT NULL,
  "telefone" BIGINT NOT NULL,
  "id_cargo" INTEGER NOT NULL,
  "data_admissao" DATE,
  "status" BOOLEAN,
  "id_comanda" INTEGER UNIQUE
);

CREATE TABLE IF NOT EXISTS "cargo" (
  "id_cargo" INTEGER PRIMARY KEY,
  "cargo" VARCHAR(30) NOT NULL
);

CREATE TABLE IF NOT EXISTS "comanda" (
  "id_comanda" SERIAL PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS "venda" (
  "id_venda" SERIAL PRIMARY KEY,
  "id_comanda" INTEGER NOT NULL,
  "id_forma_pagamento" INTEGER NOT NULL,
  "valor_total" NUMERIC(10, 2) NOT NULL,
  "valor_pago" NUMERIC(10, 2),
  "data_venda" DATE NOT NULL,
  "hora_venda" TIME NOT NULL
);

CREATE TABLE IF NOT EXISTS "forma_pagamento" (
  "id_forma_pagamento" SERIAL PRIMARY KEY,
  "nome" VARCHAR(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS "pedido" (
  "id_pedido" SERIAL PRIMARY KEY,
  "id_comanda" INTEGER NOT NULL,
  "mesa" INTEGER NOT NULL,
  "status" VARCHAR(20) NOT NULL,
  "valor_total" NUMERIC(10,2),
  "data_pedido" DATE NOT NULL,
  "hora_pedido" TIME NOT NULL
);

CREATE TABLE IF NOT EXISTS "item_pedido" (
    "id_item_pedido" SERIAL PRIMARY KEY,
    "id_pedido" INTEGER NOT NULL,
    "id_produto" INTEGER NOT NULL,
    "valor" NUMERIC(10, 2) NOT NULL,
    "quantidade" INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS "produto" (
  "id_produto" SERIAL PRIMARY KEY,
  "nome" VARCHAR(50) NOT NULL,
  "descricao" VARCHAR(200) NOT NULL,
  "valor" NUMERIC(10, 2) NOT NULL,
  "marca" VARCHAR(20),
  "unidade_medida" VARCHAR(10) NOT NULL,
  "id_secao" INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS "secao" (
  "id_secao" SERIAL PRIMARY KEY,
  "nome" VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS "desconto" (
  "id_desconto" SERIAL PRIMARY KEY,
  "id_produto" INTEGER NOT NULL,
  "valor_desconto" NUMERIC(10, 2) NOT NULL,
  "descricao" VARCHAR(200),
  "data_inicial" DATE,
  "data_final" DATE,
  "hora_inicial" TIME,
  "hora_final" TIME
);

-- ##########################################################################################################################################################
-- FOREIGN KEYS
-- ##########################################################################################################################################################

ALTER TABLE "usuario" ADD CONSTRAINT "fk_cargo_usuario" FOREIGN KEY ("id_cargo") REFERENCES "cargo" ("id_cargo");

ALTER TABLE "usuario" ADD CONSTRAINT "fk_comanda_usuario" FOREIGN KEY ("id_comanda") REFERENCES "comanda" ("id_comanda");

ALTER TABLE "venda" ADD CONSTRAINT "fk_venda_comanda" FOREIGN KEY ("id_comanda") REFERENCES "comanda" ("id_comanda");

ALTER TABLE "venda" ADD CONSTRAINT "fk_venda_forma_pagamento" FOREIGN KEY ("id_forma_pagamento") REFERENCES "forma_pagamento" ("id_forma_pagamento");

ALTER TABLE "pedido" ADD CONSTRAINT "fk_pedido_comanda" FOREIGN KEY ("id_comanda") REFERENCES "comanda" ("id_comanda");

ALTER TABLE "item_pedido" ADD CONSTRAINT "fk_item_pedido_pedido" FOREIGN KEY ("id_pedido") REFERENCES "pedido" ("id_pedido");

ALTER TABLE "item_pedido" ADD CONSTRAINT "fk_item_pedido_produto" FOREIGN KEY ("id_produto") REFERENCES "produto" ("id_produto");

ALTER TABLE "produto" ADD CONSTRAINT "fk_produto_secao" FOREIGN KEY ("id_secao") REFERENCES "secao" ("id_secao");

ALTER TABLE "desconto" ADD CONSTRAINT "fk_desconto_produto" FOREIGN KEY ("id_produto") REFERENCES "produto" ("id_produto");

-- ##########################################################################################################################################################
-- Triggers
-- ##########################################################################################################################################################

CREATE OR REPLACE FUNCTION criar_comanda_para_cliente()
RETURNS TRIGGER AS $$
DECLARE
    new_id_comanda INTEGER;
BEGIN
    -- Verificar se o id_cargo é 3
    IF NEW.id_cargo = 3 THEN
        -- Inserir uma nova comanda e obter o id_comanda gerado
        INSERT INTO comanda DEFAULT VALUES RETURNING id_comanda INTO new_id_comanda;

        -- Atualizar o id_comanda do novo usuário
		UPDATE usuario SET id_comanda = new_id_comanda WHERE id_usuario = NEW.id_usuario;
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER after_usuario_insert
AFTER INSERT ON usuario
FOR EACH ROW
EXECUTE FUNCTION criar_comanda_para_cliente();

-- ##########################################################################################################################################################

CREATE OR REPLACE FUNCTION set_preco_unitario_com_desconto()
RETURNS TRIGGER AS $$
DECLARE
  v_desconto_aplicavel NUMERIC(10, 2);
  v_data_pedido DATE;
  v_hora_pedido TIME;
BEGIN
  -- Obter a data e hora do pedido
  SELECT p.data_pedido, p.hora_pedido INTO v_data_pedido, v_hora_pedido
  FROM pedido p
  WHERE p.id_pedido = NEW.id_pedido;
  
  -- Atribuir o valor do produto ao campo preco_unitario
  NEW.valor := (SELECT pr.valor FROM produto pr WHERE pr.id_produto = NEW.id_produto);
  
  -- Verificar se existe um desconto válido para o produto
  SELECT d.valor_desconto INTO v_desconto_aplicavel
  FROM desconto d
  WHERE d.id_produto = NEW.id_produto
    AND (d.data_inicial IS NULL OR d.data_inicial <= v_data_pedido)
    AND (d.data_final IS NULL OR d.data_final >= v_data_pedido)
    AND (d.hora_inicial IS NULL OR d.hora_inicial <= v_hora_pedido)
    AND (d.hora_final IS NULL OR d.hora_final >= v_hora_pedido)
  LIMIT 1;
  
  -- Se existir um desconto aplicável, ajustar o preco_unitario
  IF v_desconto_aplicavel IS NOT NULL THEN
    NEW.valor := NEW.valor - v_desconto_aplicavel;
  END IF;

  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER before_insert_item_pedido
BEFORE INSERT ON item_pedido
FOR EACH ROW
EXECUTE FUNCTION set_preco_unitario_com_desconto();

-- Função para atualizar o valor_total na tabela pedido
CREATE OR REPLACE FUNCTION atualizar_valor_total_pedido()
RETURNS TRIGGER AS $$
DECLARE
	v_valor_total NUMERIC(10, 2);
BEGIN
	SELECT calcular_valor_total_pedido(NEW.id_pedido) INTO v_valor_total;

    -- Atualizar o valor total do pedido
    UPDATE pedido
    SET valor_total = v_valor_total
    WHERE id_pedido = NEW.id_pedido;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Trigger para chamar a função após inserir um item na tabela item_pedido
CREATE TRIGGER after_insert_item_pedido
AFTER INSERT ON item_pedido
FOR EACH ROW
EXECUTE FUNCTION atualizar_valor_total_pedido();


CREATE OR REPLACE FUNCTION calcular_valor_total_pedido(pedido_id INTEGER)
RETURNS NUMERIC(10, 2) AS $$
DECLARE
  v_valor_total NUMERIC(10, 2);
BEGIN
  SELECT SUM(ip.valor * ip.quantidade)
  INTO v_valor_total
  FROM item_pedido ip
  WHERE ip.id_pedido = pedido_id;

  RETURN v_valor_total;
END;
$$ LANGUAGE plpgsql;
