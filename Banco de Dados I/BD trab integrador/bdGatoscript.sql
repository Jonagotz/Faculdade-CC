-- ##########################################################################################################################################################
-- INSERTS
-- ##########################################################################################################################################################

insert into cargo (id_cargo, cargo) values 
                  (1, 'Gerente'), 
                  (2, 'Funcionário'),
                  (3, 'Cliente');

insert into comanda (id_comanda) select * from generate_series(1,100);

INSERT INTO "secao" (nome) VALUES
('Baguete'),
('Burguers'),
('Cervejas'),
('Chopp'),
('Drinks'),
('Não Alcoolico'),
('Pizza'),
('Porção');

INSERT INTO "forma_pagamento" (nome) VALUES
('Dinheiro'),
('Cartão de Crédito'),
('Cartão de Débito'),
('Pix'),
('Fiado');

-- Verificar a sequência atual
SELECT last_value FROM comanda_id_comanda_seq;

-- Ajustar a sequência para o maior valor na tabela comanda
SELECT setval('comanda_id_comanda_seq', (SELECT MAX(id_comanda) FROM comanda));

insert into usuario (nome, cpf, senha, email, telefone, id_cargo, data_admissao, status) values 
                    ('Julia', '662.929.240-50', 'senhavalida', 'juju@gmail.com', 49938768385, 3, '2024-03-12', true),
                    ('Gatinha Comunista', '571.049.780-03', 'senhavalida', 'gata@gmail.com',97933515513, 3, '2024-02-25', true),
                    ('Bruno', '172.336.570-09', 'senhavalida', 'brunao@gmail.com',62323278913 , 1, '2024-01-28', true),
                    ('Fran', '001.720.750-92', 'senhavalida', 'fran@gmail.com',12345678910 , 2, '2024-04-21', true);

INSERT INTO "produto" (nome, descricao, valor, marca, unidade_medida, id_secao) VALUES
('Burguer Gato Caolho', 'Hambúrguer com queijo, alface e tomate', 20.00, 'Gato Caolho', 'UN', 2),
('Burguer Gato Persa', 'Hambúrguer com queijo e bacon', 24.00, 'Gato Caolho', 'UN', 2),
('Brisa da Manha', 'Chopp', 12.00, 'Artesanal', '350ml', 4),
('Pizza Calabresa', 'Pizza com calabresa e cebola', 60.00, 'Marca D', 'G', 7);

INSERT INTO "desconto" (id_produto, valor_desconto, descricao, data_inicial, data_final, hora_inicial, hora_final) VALUES
(1, 5.00, 'Desconto de 5 r no Gato Caolho', '2024-06-25', '2024-06-30', '11:00:00', '13:00:00'),
(2, 5.25, 'Desconto de 5 r no Gato Persa', '2024-06-25', '2024-06-30', '11:00:00', '13:00:00'),
(3, 3.50, 'Desconto de 3 r no chopp BA', '2024-06-25', '2024-06-30', '11:00:00', '13:00:00'),
(4, 10.50, 'Desconto de 8 r na Pizza', '2024-06-25', '2024-06-30', '11:00:00', '13:00:00');


INSERT INTO "pedido" (id_comanda, mesa, status, data_pedido, hora_pedido)
VALUES
    (1, 13, 'Em andamento', '2024-06-28', '12:30:00'),
    (2, 11, 'Cancelado', '2024-06-28', '12:30:00'),
    (3, 12, 'Concluido', '2024-06-28', '12:30:00');

INSERT INTO item_pedido (id_pedido, id_produto, quantidade)
VALUES
    (1, 1, 2),
    (1, 4, 1),
    (2, 3, 1),
    (2, 4, 1),
    (3, 1, 2),
    (3, 2, 1),
    (3, 4, 1);