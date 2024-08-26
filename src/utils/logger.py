from datetime import datetime
import traceback

class Logger:
    
    @staticmethod
    def log_error(message, error):
        """
        Registra um erro no log
        
        Args:
        message: Mensagem de erro
        """
        
        data_atual = datetime.now()
        data_format = data_atual.strftime("%d/%m/%Y %H:%M:%S")
        
        print(f'Error: {message} | {data_format} | {__file__} | {error}')
        
try:
    numeros = ['1', '2', '3']
    for numero in numeros:
        print(numero ** 2)
except Exception:
    Logger.log_error('Erro ao adicionar livro', traceback.format_exc())