# DMSLOG Project

Esse manual tem a função de ajudar a utilizar um sistema simples para registrar dados de clientes.
Para utulizar o software é necessário os seguintes requisitos:

-Qualquer sistema operacional
-Python 3, PyCharm ou qualquer um que uso o sistema de linguagem Python,
-MYSQL ou SQLite

Primeiros passos:

Primeiros comandos a serem inseridos no sistema para que importe os dados do Python :

import sqlite3, time

conn = sqlite3.connect('Carga.db')
cursor = conn.cursor()

Com os comandos cursor.execute iremos criar a tabela com os dados a serem inseridos pelo usuário 
O ID foi usado como primary key sendo autoincrement.

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

Logo apos usaramos While para criar uma estrutura de repeteção para que consiga consultar demais informações acrescentadas no sistema,
aqui temos 5 opções que foi fornecida:

 1-Cadastrar Cliente 
 2-Consultar Todos os Clientes 
 3-Visualizar Custos 
 4-Consultar Lucro 
 5-Sair do Programa 
 Digite uma opção:  

Desta forma conseguiremos criar condições para que o sistema dê a opção e após retorne a tela inicial: 

op = 1
while op != 5:
  op = int(input('1-Cadastrar Cliente \n 2-Consultar Todos os Clientes \n 3-Visualizar Custos \n 4-Consultar Lucro \n 5-Sair do Programa \n Digite uma opção:  '))

A tabela deverar ser feita desta forma, com a atribuição de cada variavel para que não aconteça erro na leitura do programa:

 cliente = str(input('Cliente: '))
        contato = int(input('Contato: '))
        custo = float(input('Custo: '))
        preco = float (input('Preço: '))
        data_envio = input('Data envio [d/m/Y]: ')
        data_chegada = input('Data chegada [d/m/Y]: ')

Inserindo os valores de com o comando INSERT_TO da seguinte forma:
cursor.execute("""
        INSERT INTO Cadastro (Cliente, Contato, Custo, Preco, envio, chegada)
        VALUES (?,?,?,?,?,?)
        """, (cliente, contato, custo, preco, data_envio, data_chegada))
        
        conn.commit()
        
if, else e elif é estrutura condicional, utulizado aqui para que cada opção faça uma função de acordo com a necessidade solicitada:

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

Sendo assim, finalizando a estrutura do programa fico a disposição para maiores dúvidas.

Amanda Frambach
