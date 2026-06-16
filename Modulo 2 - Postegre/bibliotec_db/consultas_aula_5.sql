-- ordem das consultas
--SELECT FROM WHERE GROUP BY HAVING ORDER BY LIMIT

-- consulta geral
select * from livros;

-- consulta de colunas especificas
select titulo, ano_publicacao from livros;

-- consulta de titulo e ano de publicação descendente
select titulo, ano_publicacao 
from livros 
order by titulo DESC;

-- consulta de titulo e ano de publicação descendente limitado a dois livros
SELECT titulo, ano_publicacao
FROM livros
ORDER BY ano_publicacao DESC
LIMIT 2;

--
select id_livro, count(*) as qtd_copias
from copias
group by id_livro;

-- consulta da quantidade de cópias
select id_livro, count(*) as qtd_copias
from copias
where id_livro between 2 and 4
group by copias.id_livro 
having count (*) > 2;

-- agrupar usuários por data de cadastro
select * from usuarios;

select data_cadastro, count (*) qtd_usuarios
from usuarios 
group by data_cadastro;

--
select * from livro_genero;

-- media de ano de publicacao
select ROUND(avg(ano_publicacao)) from livros;
