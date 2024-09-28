import streamlit as st
import pandas as pd
import numpy as np
import testeNodePython
from testeNodePython import fazConsulta
from testePdf import criaPdf
from enviarEmail import email

# Definir as opções do Selectbox
opcoes = ["Enviar Email", "Buscar por data"]

# Selectbox
selecao = st.selectbox("Escolha uma opção:", opcoes)

if selecao == "Buscar por data":
    dateInicio = st.date_input("Escola a data de inicio:")
    dateFinal = st.date_input("Escolha a data de termino:")
    numeroConsulta = fazConsulta(dateInicio,dateFinal)
    if dateInicio and dateFinal:
        nomePdf = st.text_input("Digite o nome do arquivo pdf:")
        if st.button("Enviar"):
            st.write(numeroConsulta)
            email(criaPdf(numeroConsulta,nomePdf))
            st.success("Arquivo enviado com sucesso!")


    
