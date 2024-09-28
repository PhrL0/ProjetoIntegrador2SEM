import mysql.connector

#CONSULTA BANCO
def fazConsulta(inicio,fim):
    conexao = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'aluno',
        database = 'teste',
    )   

    cursor = conexao.cursor()

    comando = 'SELECT SUM(contador_acumulado) AS total_objetos FROM dados WHERE dia BETWEEN %s AND %s;'
    cursor.execute(comando,(inicio, fim))

    resultado = cursor.fetchall()
 
    cursor.close()
    conexao.close()

    numeroBd = resultado[0][0] 

    return numeroBd








