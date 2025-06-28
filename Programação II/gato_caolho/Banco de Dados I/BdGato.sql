create database gato_caolho;
\c gato_caolho
set datestyle to 'ISO,DMY';

create table if not exists usuario(
  id_usuario serial,
  nome varchar(30) not null,
  cpf integer not null,
  senha integer not null,
  email varchar(25) not null,
  cliente_id integer,
  funcionario_id integer,
  telefone integer,
  constraint pk_usuario primary key (id_usuario),
  constraint fk_usuario_cliente foreign key (cliente_id) references cliente(id_cliente),
  constraint fk_usuario_funcionario foreign key (funcionario_id) references funcionario(id_funcionario)
);
--
create table if not exists cliente(
  id_cliente integer not null,
  constraint pk_cliente primary key (id_cliente)
) INHERITS (usuario);
--
create table if not exists funcionario(
  id_funcionario integer not null,
  cargo varchar(30) not null,
  status boolean not null,
  constraint pk_funcionario primary key (id_funcionario)
) INHERITS (usuario);
--
create table if not exists comanda(
  id_comanda serial,
  numero integer not null,
  cliente_id integer not null, 
  constraint pk_comanda primary key (id_comanda),
  constraint fk_comanda_cliente foreign key (cliente_id) references cliente(id_cliente)
);
--
create table if not exists venda(
  id_venda serial,
  comanda_id integer not null,
  forma_pagamento_id integer not null,
  data_venda date not null,
  hora_venda time not null,
  constraint pk_venda primary key (id_venda),
  constraint fk_venda_comanda foreign key (comanda_id) references comanda(id_comanda),
  constraint fk_venda_forma_pagamento foreign key (forma_pagamento_id) references forma_pagamento(id_forma_pagamento)
);
--
create table if not exists forma_pagamento(
  id_forma_pagamento serial,
  nome varchar(20) not null,
  status boolean not null,
  constraint pk_forma_pagamento primary key (id_forma_pagamento)
);
--
create table if not exists pedido(
  id_pedido serial,
  comanda_id integer not null,
  mesa integer not null,
  valor integer not null,
  status boolean not null,
  data_pedido date not null,
  hora_pedido time not null,   
  constraint pk_pedido primary key (id_pedido),
  constraint fk_pedido_comanda foreign key (comanda_id) references comanda(id_comanda)
);
--
create table if not exists item_pedido(
  id_item_pedido serial,
  pedido_id integer not null,
  produto_id integer not null,
  constraint pk_comanda primary key (id_comanda),
  constraint fk_item_pedido_pedido foreign key (pedido_id) references pedido(id_pedido),
  constraint fk_item_pedido_produto foreign key (produto_id) references produto(id_produto)
);
--
create table if not exists produto(
  id_produto serial,
  nome varchar(50) not null,
  descricao varchar(200) not null,
  unidade_medida varchar(5) not null,
  valor integer not null,
  marca varchar(15),
  secao_id integer not null,
  constraint pk_produto primary key (id_produto),
  constraint fk_produto_secao foreign key (secao_id) references secao(id_secao)
);
--
create table if not exists secao(
  id_secao serial,
  nome varchar(50) not null,
  constraint pk_secao primary key (id_secao)
);
--
create table if not exists desconto(
  id_desconto serial,
  produto_id integer not null,
  valor_desconto integer not null,
  descricao varchar(30),
  data_inicial DATE,
  data_final DATE,
  hora_inicial TIME,
  hora_final TIME,
  constraint pk_desconto primary key (id_desconto),
  constraint fk_desconto_produto foreign key (produto_id) references produto(id_produto)
);
--
insert into usuario (nome, cpf, senha, email, cliente_id, funcionario_id, admin_id, telefone) values
   ('Alfred', 123456789, 123456, 'cliente@email.com', 1, null, null, 48912345678),
   ('Stephen', 987654321, 123456, 'funcionario@email.com', null, 1, null, 47912345678),
   ('Harrison', 12105140955, 123456, 'admin@email.com', null, null, 1, 49912345678);
--

