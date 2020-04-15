# DMSLOG

Clientes que solicitaram serviço:

SELECT Cliente, contato from Cadastro

--------------------------------------------------------------------------

Total de Custos:

SELECT SUM(Custo)FROM Cadastro

---------------------------------------------------------------------------

Total de Lucro:

select Custo, Preço, (Custo - Preço) as Lucro  From Cadastro

