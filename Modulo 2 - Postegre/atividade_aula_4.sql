--========================================
-- ATIVIDADE AULA 4 - monitor Eric Araújo
-- Paula Roberta Corrêa dos Santos Arruda
--========================================

--1. Inserir a Editora Penguin Books
insert into editoras (nome, cidade)
values ('Penguin Books', 'Londres');

select * from editoras where nome = 'Penguin Books';

--2. Inserir dois novos usuários
insert into usuarios (nome, email, cpf)
values ('Daniel Rocha', 'daniel@mail.com', '12345678912'),
('Fernanda Novais', 'nada@mail.com', '87654635248');

--3. Inserir quatro livros novos
insert into livros (titulo, isbn, ano_publicacao, id_editora)
values ('Harry Potter e a Pedra Filosofal', '9876543872345', 2000, 5),
('1984', '0987564382712', 1949, 3),
('Admiravel Mundo Novo', '1234576890345', 1932, 2),
('As Menininhas', '0923145267894', 1950, 5);

select * from livros;

--4. Criar duas cópis físicas para o livro Harry Potter
insert into copias (num_tombamento, id_livro, condicao)
values ('TOM-006', 5, 'Novo'),
('TOM-007', 5, 'Regular');

select * from copias;

--5. Vincular autores aos livros novos
insert into autores (nome, nacionalidade)
values ('J.K.Rowling', 'Britanica'),
('George Orwell', 'Indiano'),
('Louisa May AlcottLouisa May Alcott', 'Norte Americana');

select * from autores;

insert into livro_autor (id_livro, id_autor)
values
(5, 5),
(8, 7),
(6, 6);

select * from livro_autor;

--6. Registrar três emprestimos
insert into emprestimos (id_usuario, num_tombamento, data_saida, data_prevista)
values 
(1, 'TOM-006', current_date, current_date + 15),
(3, 'TOM-007', current_date, current_date + 15),
(5, 'TOM-003', current_date, current_date + 15);

select * from emprestimos;

--7. Atualizar o email do usuario
select * from usuarios;
update usuarios
set email = 'daniel.rocha@mail.com'
where id_usuario = 4;

--8. Registrar devolucao de uma cópia
update emprestimos
set data_devolucao = current_date
where id_emprestimo = 2
and num_tombamento = 'TOM-003';

-- Extra - Listar os livros emprestados e seus respectivos usuários
select l.titulo, u.nome, e.data_saida, e.data_prevista
from emprestimos e
join copias c on e.num_tombamento = c.num_tombamento
join livros l on c.id_livro = l.id_livro
join usuarios u on e.id_usuario = u.id_usuario
where e.data_devolucao is null;

--9. Marcar cópia devolvida como ˜Danificada˜
update copias
set condicao = 'Danificada'
where num_tombamento = 'TOM-007';

--10. Deletar emprestimo registrado por engano
begin;

delete from emprestimos
where id_usuario = 1
and num_tombamento = 'TOM-001'; 

commit;

 --rollback; -- se necessário para desfazer a exclusão