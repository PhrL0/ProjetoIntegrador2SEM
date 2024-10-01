import streamlit as st
import schedule
import time
import threading
import datetime
from enviarEmail import enviaEmail
from testePdf import criaPdf
from testeNodePython import tabelaClasses

import os

def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

# Inicializando a thread para o agendamento
scheduler_thread = threading.Thread(target=run_scheduler, daemon=True)
scheduler_thread.start()

# Simulação de login (ajuste de acordo com o sistema real)
login = True

# Inicializando o estado da sessão
if 'login' not in st.session_state:
    st.session_state['login'] = True

# Se o usuário ainda não estiver logado, mostrar a tela de login
if not st.session_state['login']:
    st.title("Página de Login")
    
    # Campos para o usuário inserir nome e senha
    username = st.text_input("Usuário")
    password = st.text_input("Senha", type="password")
    
    # Botão para realizar o login
    if st.button("Login"):
        if login:
            st.session_state['login'] = True
            st.success("Login realizado com sucesso!")
        else:
            st.error("Usuário ou senha incorretos.")
else:
    st.header("Bem-vindo à página de administração")

    st.sidebar.header("Menu")
    opcao = st.sidebar.selectbox("Escolha uma opção:", ["Relatório", "Email","Consulta"])

    if opcao == "Relatório":
        st.subheader("Relatório")
        tipoRelatorio = st.selectbox("Deseja gerar um relatório ou importar um relátorio?", ["Gerar", "Importar"])

        if tipoRelatorio == "Gerar":
            col1, col2, col3 = st.columns(3)

            # Início do formulário
            with st.form(key='form1'):
                with col1:
                    # Input de texto
                    nome = st.text_input("Nome:")
                with col2:
                    # Input de e-mail
                    email = st.text_input("E-mail:")
                with col3:
                    objetos = st.selectbox("Selecione a classe:", ["Cadarço", "Palmilha", "Tênis"])
            nomePdf = st.text_input("Nome Arquivo:")
            titulo = st.text_input("Título:")
            observacao = st.text_input("Observação:")
            if st.button("Gerar Relatório"):
                with st.spinner("Carregando... por favor aguarde"):
                    criaPdf(nomePdf,titulo,nome,objetos,observacao)
                    pathDestino = "pdf/"
                    # Salvar o arquivo no diretório especificado
                    salvarArquivo = os.path.join(pathDestino, nomePdf)
                    with open(salvarArquivo, "w") as file:
                        file.write("Este é o conteúdo do relatório.")
                st.success("Relatório gerado com sucesso")

        if tipoRelatorio == "Importar":
            # Upload de um arquivo de texto ou CSV
            uploaded_file = st.file_uploader("Escolha um arquivo pdf", type=["pdf"])
            if st.button("Enviar"):
                pathDestino = "pdf/"
                # Salvar o arquivo no diretório especificado
                with open(os.path.join(pathDestino, uploaded_file.name), "wb") as f:
                    f.write(uploaded_file.getbuffer())
                st.success("Arquivo enviado com sucesso!")

    if opcao == "Email":
        st.subheader("Email")
        tipoEmail = st.selectbox("Deseja enviar um email agora ou agendar?", ["Agora", "Agendar"])

        if tipoEmail == "Agora":
            # Início do formulário
            with st.form(key='form2', clear_on_submit=True):
                # Input de email
                nomeRemetente = st.text_input("Email Remetente")
                nomeDestinatario = st.text_input("Email Destinatário")
                assunto = st.text_input("Assunto")
                corpo = st.text_area("Mensagem")

                # Upload de um arquivo PDF
                uploaded_file = st.file_uploader("Escolha um arquivo pdf", type=["pdf"])
                nomeArquivo = uploaded_file.name if uploaded_file else None
                
                if st.form_submit_button("Enviar"):
                    with st.spinner("Carregando... por favor aguarde"):
                        enviaEmail(nomeRemetente, nomeDestinatario, assunto, corpo, nomeArquivo)
                        st.success("Email enviado com sucesso!")

        if tipoEmail == "Agendar":
            with st.form(key='form3', clear_on_submit=True):
                col1, col2, col3 = st.columns(3)

                dias_da_semana = {
                    "Segunda-feira": schedule.every().monday,
                    "Terça-feira": schedule.every().tuesday,
                    "Quarta-feira": schedule.every().wednesday,
                    "Quinta-feira": schedule.every().thursday,
                    "Sexta-feira": schedule.every().friday,
                    "Sábado": schedule.every().saturday,
                    "Domingo": schedule.every().sunday
                }

                nomeRemetente = st.text_input("Email Remetente")
                nomeDestinatario = st.text_input("Email Destinatário")
                assunto = st.text_input("Assunto")
                corpo = st.text_area("Mensagem")

                with col1:
                    dia_selecionado = st.selectbox("Escolha um dia da semana:", list(dias_da_semana.keys()))
                    hora = st.time_input("Selecione o horário do envio")
                    hora_formatada = hora.strftime("%H:%M")

                uploaded_file = st.file_uploader("Escolha um arquivo pdf", type=["pdf"])
                nomeArquivo = uploaded_file.name if uploaded_file else None

                if st.form_submit_button("Agendar"):
                    dia = dias_da_semana[dia_selecionado]
                    
                    # Usar lambda para passar a função com parâmetros
                    dia.at(hora_formatada).do(lambda: enviaEmail(nomeRemetente, nomeDestinatario, assunto, corpo, nomeArquivo))
                    st.success(f"Email agendado para {dia_selecionado} às {hora_formatada}")
    if opcao == "Consulta":
        st.subheader("Consultas")
        escolha = st.radio("Filtrar por:", ("Data","Classe","Tudo"))
        if escolha == "Data":
            dataIncioConsulta = st.date_input("Data Inicio:")
            dataTerminoConsulta = st.date_input("Data Termino:")
            if dataIncioConsulta and dataTerminoConsulta:
                tabelaClasses(dataIncioConsulta,dataTerminoConsulta)
        if escolha == "Classe":
            classeConsulta = st.text_input