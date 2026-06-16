-- ===========================================================================
-- POPULANDO A BIBLIOTECA — Live Coding · Aula 04
-- ===========================================================================
INSERT INTO editoras (nome, cidade) VALUES
    ('Companhia das Letras', 'São Paulo'),
    ('Record',               'Rio de Janeiro'),
    ('Rocco',                'Rio de Janeiro'),
    ('Intrínseca',           'Rio de Janeiro');
INSERT INTO autores (nome, nacionalidade) VALUES
    ('George Orwell',     'Britânico'),
    ('Aldous Huxley',     'Britânico'),
    ('Clarice Lispector', 'Brasileira'),
    ('Machado de Assis',  'Brasileiro');
INSERT INTO generos (nome) VALUES
    ('Distopia'),
    ('Ficção Científica'),
    ('Literatura Brasileira'),
    ('Romance');
INSERT INTO usuarios (nome, email, cpf) VALUES
    ('Ana Lima',    'ana.lima@mail.com',    '11122233300'),
    ('Bruno Souza', 'bruno.souza@mail.com', '44455566600'),
    ('Carla Matos', 'carla.matos@mail.com', '77788899900');
INSERT INTO livros (titulo, isbn, ano_publicacao, id_editora) VALUES
    ('A Hora da Estrela', '9788531208751', 1977, 1),
    ('Dom Casmurro',      '9788525406477', 1899, 1),
    ('O Alienista',       '9788508106769', 1882, 2),
    ('Fahrenheit 451',    '9788501080165', 1953, 3);
INSERT INTO copias (num_tombamento, id_livro, condicao) VALUES
    ('TOM-001', 1, 'Bom'),
    ('TOM-002', 1, 'Bom'),
    ('TOM-003', 2, 'Novo'),
    ('TOM-004', 3, 'Regular'),
    ('TOM-005', 4, 'Bom');
INSERT INTO livro_autor (id_livro, id_autor) VALUES
    (1, 3),  -- A Hora da Estrela → Clarice Lispector
    (2, 4),  -- Dom Casmurro      → Machado de Assis
    (3, 4),  -- O Alienista       → Machado de Assis
    (4, 1);  -- Fahrenheit 451    → George Orwell
INSERT INTO livro_genero (id_livro, id_genero) VALUES
    (1, 3),  -- A Hora da Estrela → Literatura Brasileira
    (2, 4),  -- Dom Casmurro      → Romance
    (3, 3),  -- O Alienista       → Literatura Brasileira
    (4, 1);  -- Fahrenheit 451    → Distopia
INSERT INTO emprestimos (id_usuario, num_tombamento, data_saida, data_prevista) VALUES
    (1, 'TOM-001', CURRENT_DATE - 10, CURRENT_DATE + 5),
    (2, 'TOM-003', CURRENT_DATE - 5,  CURRENT_DATE + 10),
    (3, 'TOM-005', CURRENT_DATE,       CURRENT_DATE + 15);