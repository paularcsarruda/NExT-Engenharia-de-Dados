-- Qual o total de livros, autores, editora e usuários?
-- Filtro: não possui.
-- tabelas: autores, livros, editoras e usuários.
select
    (select count(*) from livros) as total_livros,
    (select count(distinct autores) from autores) as total_autores,
    (select count(*) from editoras) as total_editoras,
    (select count(*) from usuarios) as total_usuarios;

-- Quais usuários mais pegaram livros emprestados?
-- Tabelas: emprestimos e usuarios.
-- Filtro: não possui filtro.
select 
	e.id_usuario,
	u.nome,
	count (*) as total_emprestimos
from emprestimos e
join usuarios u
	on e.id_usuario = u.id_usuario
group by e.id_usuario, u.nome
order by total_emprestimos desc
limit 3;

-- Quantos emprestimos estão em atraso hoje?
-- Tabela: emprestimos.
-- Filtro: data prevista menor que a data atual e devolução ainda não realizada.
select count(*) as emprestimos_atraso
from emprestimos
where data_prevista < current_date
	and data_real is null;

-- Qual editora tem mais livros no acervo?
-- Filtro: não possui filtro específico.
-- Tabelas: editoras e livros.
select
    l.id_editora,
    e.nome,
    count (*) as total_livros
from livros l
join editoras e
    on l.id_editora = e.id_editora
group by l.id_editora, e.nome
order by total_livros desc
limit 1;

-- Quais livros têm mais de uma cópia no acervo??? 
-- Tabela: copias.
-- Filtro: somente livros com quantidade de cópias maior que 1.
select id_livro, count(*) as total_copias
from copias
group by id_livro
having count(*) > 1;

-- Quais cópias específicas são as mais emprestadas (do mais para o menos movimentado)?
-- Tabela: emprestimos.
-- Filtro: não possui.
select num_tombamento, count(*) as livros_mais_emprestados
from emprestimos e
group by e.num_tombamento
order by livros_mais_emprestados desc;


-- Quantos generos diferentes estão cadastrados no sistema?
-- Tabela: generos.
-- Filtro: não possui.
select count(*) generos_cadastrados
from generos;

