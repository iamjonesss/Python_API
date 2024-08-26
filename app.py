from flask import jsonify, request
from general_config import app, conn

def init_app():
    livros = conn.get_books_json()
    

init_app()