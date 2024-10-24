import mysql.connector
import json

# Configuração da conexão
def create_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='aluno',
        database='projintegradorbd'
    )


def fazConsulta():
    try:
        conexao = create_connection()
        cursor = conexao.cursor(dictionary=True)  # Cursor com dicionário

        comando = 'SELECT * FROM DADOS;'
        cursor.execute(comando)

        resultado = cursor.fetchall()
        
        # Converte o resultado diretamente em JSON
        jsonData = json.dumps(resultado)

        return jsonData


    except mysql.connector.Error as e:
        print(f"Erro ao consultar o banco de dados: {e}")
    
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()


