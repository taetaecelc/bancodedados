-- SQLite Online Compatible Database Schema
-- Database for bookstore (Loja de Livros)

-- Drop existing tables if they exist (for clean setup)
DROP TABLE IF EXISTS Compras;
DROP TABLE IF EXISTS Clientes;

-- Create Clientes (Customers) Table
CREATE TABLE Clientes (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    nomeCliente VARCHAR(150) NOT NULL,
    emailCliente VARCHAR(150) NOT NULL UNIQUE
);

-- Create Compras (Purchases) Table
CREATE TABLE Compras (
    CompraID INTEGER PRIMARY KEY AUTOINCREMENT,
    ClienteID INTEGER NOT NULL,
    NomeLivro VARCHAR(200) NOT NULL,
    DataCompra DATE DEFAULT CURRENT_DATE,
    Quantidade INTEGER DEFAULT 1,
    PrecoUnitario DECIMAL(10, 2),
    FOREIGN KEY (ClienteID) REFERENCES Clientes(ID) ON DELETE CASCADE
);

-- Insert sample data
INSERT INTO Clientes (nomeCliente, emailCliente) VALUES 
('João Silva', 'joao@email.com'),
('Maria Santos', 'maria@email.com'),
('Pedro Oliveira', 'pedro@email.com');

INSERT INTO Compras (ClienteID, NomeLivro, Quantidade, PrecoUnitario) VALUES 
(1, 'O Cortiço', 2, 35.50),
(2, 'Memórias Póstumas de Brás Cubas', 1, 42.00),
(3, 'Grande Sertão: Veredas', 3, 55.00),
(1, '1984', 1, 38.90);

-- Query examples
SELECT * FROM Clientes;
SELECT * FROM Compras;

-- Join query: List all purchases with customer names
SELECT 
    c.nomeCliente,
    c.emailCliente,
    cp.NomeLivro,
    cp.Quantidade,
    cp.PrecoUnitario,
    (cp.Quantidade * cp.PrecoUnitario) AS TotalCompra,
    cp.DataCompra
FROM Compras cp
INNER JOIN Clientes c ON cp.ClienteID = c.ID
ORDER BY c.nomeCliente;
