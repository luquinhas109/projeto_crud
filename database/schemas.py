from connector import connect

conexao = connect()
cursor = conexao.cursor()

cursor.execute("""
create table if not exists Safra(
    id_safra int primary key auto_increment,
    nome_safra varchar(100) not null,
    cultura varchar(100) not null,
    ano_agricola date default (current_date)
)
""")

cursor.execute("""
create table if not exists Insumo(
    id_insumo int primary key auto_increment,
    nome_comercial varchar(100) not null,
    tipo_insumo varchar(100) not null,
    custo_unitario decimal(10,2) not null
)
""")

cursor.execute("""
create table if not exists AplicacaoInsumo(
    id_aplicacao int primary key auto_increment,
    id_safra int not null,
    id_insumo int not null,
    quantidade_aplicada decimal(10,2) not null,
    custo_total decimal(10,2) not null,
    foreign key (id_safra) references Safra(id_safra),
    foreign key (id_insumo) references Insumo(id_insumo)
)
""")

conexao.commit()
cursor.close()
conexao.close()