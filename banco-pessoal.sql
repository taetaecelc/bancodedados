CREATE TABLE Livros (
    ID_Livro INT PRIMARY KEY,
    Titulo_Livro VARCHAR(100) NOT NULL,
    Preco_Venda DECIMAL(10, 2) NOT NULL,
    Sinopse TEXT
);
SELECT * FROM Livros;
