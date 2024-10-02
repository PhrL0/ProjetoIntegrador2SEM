import mysql.connector
import streamlit as st
import pandas as pd

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

def tabelaFiltroData(inicio,fim):

    cursor = conexao.cursor()

    comando = 'SELECT classe,dia,hora FROM dados WHERE dia BETWEEN %s AND %s;'
    cursor.execute(comando,(inicio, fim))
    resultado = cursor.fetchall()
    st.header('Consulta banco de dados')
    df = pd.DataFrame(resultado, columns=['Objeto', 'Data', 'Hora'])

    st.table(df)

def tabelaFiltroClasse(classeObj):

    cursor = conexao.cursor()

    comando = 'SELECT classe,dia,hora FROM dados WHERE classe=%s;'
    cursor.execute(comando,(classeObj,))
    resultado = cursor.fetchall()
    st.header('Consulta banco de dados')

    df = pd.DataFrame(resultado, columns=['Objeto', 'Data', 'Hora'])

    st.table(df)


def tabelaFiltroTudo(inicio,fim,classeObj):

    cursor = conexao.cursor()

    comando = 'SELECT classe,dia,hora FROM dados WHERE dia BETWEEN %s AND %s AND classe=%s;'
    cursor.execute(comando,(inicio,fim,classeObj))
    resultado = cursor.fetchall()
    st.header('Consulta banco de dados')

    df = pd.DataFrame(resultado, columns=['Objeto', 'Data', 'Hora'])

    st.table(df)











