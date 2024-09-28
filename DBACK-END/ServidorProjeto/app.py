import streamlit as st
import pandas as pd
import numpy as np
import os
from enviarEmail import enviaEmail
import schedule
import time
import threading
import datetime

def run_scheduler():
    while True:
        schedule.run_pending()  # Executa as tarefas agendadas
        time.sleep(1)  # Aguarda um segundo antes de verificar novamente

st.header("Bem-vindo à página de administração")

st.sidebar.header("Menu")
opcao = st.sidebar.selectbox("Escolha uma opção:", ["Relatório", "Email"])

if opcao == "Relatório":

    st.subheader("Relatório")

    tipoRelatorio = st.selectbox("Deseja gerar um relatório ou importar um relátorio?", ["Gerar", "Importar"])

    
    if tipoRelatorio == "Gerar":

        col1,col2,col3 = st.columns(3)

        # Início do formulário
        with st.form(key='form1'):
            
            with col1:
                # Input de texto
                nomeSolicitante = st.text_input("Nome Solicitante")
            with col2:
                # Input de e-mail
                email = st.text_input("E-mail")
            with col3:
                objetos = st.selectbox("Selecione a classe:",["obj1","obj2","Todos"])
        if st.button("Gerar Relatório"):
            with st.spinner("Carregando... por favor aguarde"):
                time.sleep(3)
            st.success("Relatório gerado com sucesso")

    if tipoRelatorio == "Importar":

        # Upload de um arquivo de texto ou CSV
        uploaded_file = st.file_uploader("Escolha um arquivo pdf", type=["pdf"])
        if st.button("Enviar"):
            pathDestino = "pdf/"
if opcao == "Email":

    st.subheader("Email")

    tipoEmail= st.selectbox("Deseja enviar um email agora ou agendar?", ["Agora", "Agendar"])

    if tipoEmail == "Agora":

        # Início do formulário
        with st.form(key='form2', clear_on_submit=True):
            
            # Input de email
            nomeRemetente = st.text_input("Email Remetente")
            nomeDestinatario = st.text_input("Email Destinatario")
         
            # Input de texto
            assunto = st.text_input("Assunto")
            corpo = st.text_area("Mensagem")

            # Upload de um arquivo de texto ou CSV
            uploaded_file = st.file_uploader("Escolha um arquivo pdf", type=["pdf"])
            if uploaded_file is not None:
                nomeArquivo = uploaded_file.name
            
            
            if st.form_submit_button("Enviar"):
                with st.spinner("Carregando... por favor aguarde"):
                    enviaEmail(nomeRemetente,nomeDestinatario,assunto,corpo,nomeArquivo)
                    st.success("Email enviado com sucesso!")

    if tipoEmail == "Agendar":

        # Início do formulário
        with st.form(key='form3', clear_on_submit=True):

            col1,col2,col3 = st.columns(3)
            
            # Input de email
            nomeRemetente = st.text_input("Email Remetente")
            nomeDestinatario = st.text_input("Email Destinatario")
         
            # Input de texto
            assunto = st.text_input("Assunto")
            corpo = st.text_area("Mensagem")

            with col1:
                dia = st.date_input("Selecione o dia do agendamento")
                hora = st.time_input("Selecione o horário do envio")
                data_hora_agendada = datetime.datetime.combine(dia, hora)

            # Upload de um arquivo de texto ou CSV
            uploaded_file = st.file_uploader("Escolha um arquivo pdf", type=["pdf"])

            if uploaded_file is not None:
                nomeArquivo = uploaded_file.name
            
            
            if st.form_submit_button("Enviar"):
                schedule.every().day.at(data_hora_agendada.strftime("%H:%M")).do(enviaEmail(nomeRemetente,nomeDestinatario,assunto,corpo,nomeArquivo))

                # Iniciar o scheduler em uma nova thread
                threading.Thread(target=run_scheduler, daemon=True).start()
                

        






    
            

