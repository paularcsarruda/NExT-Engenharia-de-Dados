CREATE TABLE editoras (
    id_editora  SERIAL       PRIMARY KEY,
    nome        VARCHAR(150) NOT NULL,
    cidade      VARCHAR(100)
);


CREATE TABLE autores (
    id_autor      SERIAL       PRIMARY KEY,
    nome          VARCHAR(150) NOT NULL,
    nacionalidade VARCHAR(80)
);


CREATE TABLE generos (
    id_genero SERIAL       PRIMARY KEY,
    nome      VARCHAR(80)  NOT NULL UNIQUE
);

CREATE TABLE usuarios (
    id_usuario    SERIAL       PRIMARY KEY,
    nome          VARCHAR(150) NOT NULL,
    email         VARCHAR(200) NOT NULL UNIQUE,
    cpf           CHAR(11)     NOT NULL UNIQUE,
    data_cadastro DATE         NOT NULL DEFAULT CURRENT_DATE
);


CREATE TABLE livros (
    id_livro         SERIAL       PRIMARY KEY,
    titulo           VARCHAR(200) NOT NULL,
    isbn             VARCHAR(13)  UNIQUE,
    ano_publicacao   INTEGER      CHECK (ano_publicacao > 1400 AND ano_publicacao <= 2030),
    id_editora       INTEGER      NOT NULL,

    CONSTRAINT fk_livro_editora
        FOREIGN KEY (id_editora)
        REFERENCES editoras(id_editora)
);


CREATE TABLE copias (
    num_tombamento VARCHAR(20)  PRIMARY KEY,
    id_livro       INTEGER      NOT NULL,
    condicao       VARCHAR(50)  NOT NULL DEFAULT 'Bom'
                                CHECK (condicao IN ('Novo', 'Bom', 'Regular', 'Danificado')),

    CONSTRAINT fk_copia_livro
        FOREIGN KEY (id_livro)
        REFERENCES livros(id_livro)
);


CREATE TABLE livro_autor (
    id_livro  INTEGER NOT NULL,
    id_autor  INTEGER NOT NULL,

    PRIMARY KEY (id_livro, id_autor),

    CONSTRAINT fk_la_livro
        FOREIGN KEY (id_livro)
        REFERENCES livros(id_livro),

    CONSTRAINT fk_la_autor
        FOREIGN KEY (id_autor)
        REFERENCES autores(id_autor)
);

CREATE TABLE livro_genero (
    id_livro  INTEGER NOT NULL,
    id_genero INTEGER NOT NULL,

    PRIMARY KEY (id_livro, id_genero),

    CONSTRAINT fk_lg_livro
        FOREIGN KEY (id_livro)
        REFERENCES livros(id_livro),

    CONSTRAINT fk_lg_genero
        FOREIGN KEY (id_genero)
        REFERENCES generos(id_genero)
);

CREATE TABLE emprestimos (
    id_emprestimo  SERIAL  PRIMARY KEY,
    id_usuario     INTEGER NOT NULL,
    num_tombamento VARCHAR(20) NOT NULL,
    data_saida     DATE    NOT NULL DEFAULT CURRENT_DATE,
    data_prevista  DATE    NOT NULL,
    data_real      DATE,   -- NULL enquanto não devolvido

    CONSTRAINT fk_emp_usuario
        FOREIGN KEY (id_usuario)
        REFERENCES usuarios(id_usuario),

    CONSTRAINT fk_emp_copia
        FOREIGN KEY (num_tombamento)
        REFERENCES copias(num_tombamento),

    CONSTRAINT chk_datas
        CHECK (data_prevista > data_saida)
);