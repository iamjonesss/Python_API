from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json

Base = declarative_base()

# Classe de conexão com o banco de dados e seus métodos
class SQL_Connection:
    """
    Classe para administrar conexão com o SQL e suas operações
    
    Atributos:
    database_url: URL de conexão com o banco de dados
    engine: sqlalchemy.engine.base.Engine
    Session: Sessão do SQLAlchemy para manipulação de dados 
    session: A sessão do SQLAlchemy
    """
    
    def __init__(self, username, password, host, port, database):
        """
        Inicializa os atributos de conexão com o banco de dados
        
        Args:
        username: Nome de usuário do banco de dados
        password: Senha do banco de dados
        host: Endereço do banco de dados
        port: Porta do banco de dados
        database: Nome do banco de dados
        """
        
        self.database_url = f'mysql://{username}:{password}@{host}:{port}/{database}'
        self.engine = create_engine(self.database_url, echo=True)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
        Base.metadata.create_all(self.engine)
        
    def add_books(self, book_name, release_date, author, genre, publisher):
        """
        Adiciona um livro ao banco de dados
        
        Args:
        book_name: Nome do livro
        release_date: Data de lançamento do livro
        author: Autor do livro
        genre: Gênero do livro
        publisher: Editora do livro
        """
        
        new_book = Book(
            name=book_name,
            release_date=release_date,
            author=author,
            genre=genre,
            publisher=publisher
        )
        
        self.session.add(new_book)
        self.session.commit()
        
    
    def get_books(self):
        """
        Retorna todos os livros do banco de dados
        
        Returns:
        books: Lista de livros
        """
        
        books = self.session.query(Book).all()
        return books
    
    
    def get_book(self, book_id):
        """
        Retorna um livro do banco de dados
        
        Args:
        book_id: Identificador do livro
        
        Returns:
        book: Livro
        """
        
        book = self.session.query(Book).filter_by(id=book_id).first()
        return book
    
    
    def delete_book(self, book_id):
        """
        Deleta um livro do banco de dados
        
        Args:
        book_id: Identificador do livro
        """
        
        book = self.session.query(Book).filter_by(id=book_id).first()
        self.session.delete(book)
        self.session.commit()
        
        
    def get_books_json(self):
        """
        Retorna todos os livros do banco de dados em formato JSON
        
        Returns:
        books_json: Lista de livros em formato JSON        
        """
        
        books = self.get_books()
        books_dict = [book.to_dict() for book in books]
        books_json = json.dumps(books_dict, ensure_ascii=False, indent=4)
        return books_json
        
class Book(Base):
    """
    Classe que representa a tabela de livros no banco de dados
    
    Atributos:
    id: Identificador do livro
    name: Nome do livro
    release_date: Data de lançamento do livro
    author: Autor do livro
    genre: Gênero do livro
    publisher: Editora do livro
    """
    
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    release_date = Column(Date, nullable=False)
    author = Column(String, nullable=False)
    genre = Column(String, nullable=False)
    publisher = Column(String, nullable=False)
    
    def to_dict(self):
        """
        Converte o objeto Book em um dicionário
        
        Returns:
        dict: Dicionário representando o livro
        """
        return {
            'id': self.id,
            'name': self.name,
            'release_date': self.release_date.isoformat(),
            'author': self.author,
            'genre': self.genre,
            'publisher': self.publisher
        }
