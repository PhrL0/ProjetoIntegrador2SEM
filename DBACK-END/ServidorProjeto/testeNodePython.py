import mysql.connector
import streamlit as st

#CONSULTA BANCO
conexao = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'aluno',
        database = 'teste',
    )   

def fazConsulta(inicio,fim):
    
    cursor = conexao.cursor()

    comando = 'SELECT SUM(contador_acumulado) AS total_objetos FROM dados WHERE dia BETWEEN %s AND %s;'
    cursor.execute(comando,(inicio, fim))

    resultado = cursor.fetchall()
 
    cursor.close()
    conexao.close()

    numeroBd = resultado[0][0] 

    return numeroBd

def consultaClasse():
    cursor = conexao.cursor()

    comando = 'SELECT classe FROM dados'
    cursor.execute(comando)

    resultado = cursor.fetchall()
    
    return resultado

def tabelaClasses(inicio,fim):

    cursor = conexao.cursor()

    comando = 'SELECT classe,dia,hora FROM dados WHERE dia BETWEEN %s AND %s;'
    cursor.execute(comando,(inicio, fim))
    resultado = cursor.fetchall()
    st.title('Consultar Dados')
    colunas = st.columns([1,2,3])
    campos = ['Objeto','Data','Hora']
    for coluna, campo in zip(colunas,campos):
        coluna.write(campo)
                     
    for item in resultado:
        col1,col2,col3 = st.columns({1,2,3})
        col1.write(item[0])
        col2.write(item[1])
        col3.write(item[2])











