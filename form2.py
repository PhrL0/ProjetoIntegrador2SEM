import streamlit as st
import mysql.connector

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'aluno',
    database = 'clientes',
)
cursor = conexao.cursor()

comando = f'SELECT * FROM cliente'
cursor.execute(comando)
resultado = cursor.fetchall() #ler banco de dados

def consultar(): 
    st.title('Consultar Dados')
    colunas = st.columns({1,2,3,4,5})
    campos = ['id','Nome','Idade','Profissão','Admissão']
    for coluna, campo in zip(colunas,campos):
        coluna.write(campo)
                     
    for item in resultado:
        col1,col2,col3,col4,col5 = st.columns({1,2,3,4,5})
        col1.write(item[0])
        col2.write(item[1])
        col3.write(item[2])
        col4.write(item[3])
        col5.write(item[4])

consultar()