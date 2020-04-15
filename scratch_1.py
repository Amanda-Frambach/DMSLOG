import sqlite3, time

conn = sqlite3.connect('Carga.db')
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE  IF NOT EXISTS Cadastro(
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Cliente TEXT NOT NULL,
    contato TEXT NOT NULL,
    Custo FLOAT,
    Preço FLOAT,
    Data_envio DATE,
    Data_chegada DATE);
    """)

print('Banco de dados criado com sucesso!')

cursor.execute("""
INSERT INTO Cadastro(Id, Cliente, Contato, Custo, Preço, Data_envio, Data_chegada)
VALUES ('1', 'Andressa Oliveira', '21999999999', '219.20', '79.5', '2020-04-15', '2020-05-20')
""")

cursor.execute("""
INSERT INTO Cadastro(Id, Cliente, Contato, Custo, Preço, Data_envio, Data_chegada)
VALUES ('2', 'Victor Gonzaga', '21999999989', '150.70', '119.5', '2020-02-25', '2020-03-10')
""")

cursor.execute("""
        INSERT INTO Cadastro(Id, Cliente, Contato, Custo, Preço, Data_envio, Data_chegada)
VALUES ('3', 'Daniel Silva', '21999949989', '180.70', '102  .5', '2020-01-05', '2020-02-03')
""")

cursor.execute("""
INSERT INTO Cadastro(Id, Cliente, Contato, Custo, Preço, Data_envio, Data_chegada)
VALUES ('4', 'Vivian Assumpção', '21997899989', '250.99', '139.5', '2020-02-25', '2020-03-10')
""")

conn.commit()

print('Dados inseridos com sucesso.')

