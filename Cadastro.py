import sqlite3, time

conn = sqlite3.connect('Carga.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE Cadastro (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        cliente TEXT NOT NULL,
        contato INT,
        custo    FLOAT NOT NULL,
        preco FLOAT NOT NULL,
        envio DATE,
        chegada DATE
);
""")

op = 1
while op != 5:
    op = int(input('1-Cadastrar Cliente \n 2-Consultar Todos os Clientes \n 3-Visualizar Custos \n 4-Consultar Lucro \n 5-Sair do Programa \n Digite uma opção:  '))
    if op == 1:
        cliente = str(input('Cliente: '))
        contato = int(input('Contato: '))
        custo = float(input('Custo: '))
        preco = float (input('Preço: '))
        data_envio = input('Data envio [d/m/Y]: ')
        data_chegada = input('Data chegada [d/m/Y]: ')

        cursor.execute("""
        INSERT INTO Cadastro (Cliente, Contato, Custo, Preco, envio, chegada)
        VALUES (?,?,?,?,?,?)
        """, (cliente, contato, custo, preco, data_envio, data_chegada))

        conn.commit()
    elif op == 2:
        cursor.execute("""
        SELECT * FROM Cadastro;
        """)
        for linha in cursor.fetchall():
            print(linha)
    elif op == 3:
        cursor.execute("""
        SELECT SUM(custo)FROM Cadastro;
        """)
        for linha in cursor.fetchall():
            print('A soma de todos os custos é: {}'.format(linha))
    elif op == 4:
        cursor.execute("""
        select custo, preco, (custo - preco) as Lucro From Cadastro;
        """)
        for linha in cursor.fetchall():
            print('O lucro do processo é: \n{}'.format(linha))
    elif op == 5:
        print('Obrigado por utilizar o nosso sistema!!!')
    else:
        print("Opção inválida.")
