import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def enviaEmail(nomeRemetente,nomeDestinatario,assunto,mesagem,nomePdf):
    # Configurações do e-mail
    remetente = nomeRemetente
    destinatario = nomeDestinatario
    senha = 'okyb kimo iqmb pwka'  # Certifique-se de usar uma senha de app ou de estar com autenticação correta

    # Criar o objeto da mensagem
    msg = MIMEMultipart()

    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subject'] = assunto

    # Corpo do e-mail
    corpo = mesagem
    msg.attach(MIMEText(corpo, 'plain'))

    # Anexar o PDF
    nome_arquivo = nomePdf  # Caminho para o PDF que você gerou
    with open(nome_arquivo, 'rb') as arquivo:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(arquivo.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename={nome_arquivo}')
        msg.attach(part)

    # Conectar ao servidor SMTP do Gmail
    try:
        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        servidor.starttls()  # Usar TLS para a conexão segura
        servidor.login(remetente, senha)

        # Converter o objeto da mensagem para string e enviar o e-mail
        texto = msg.as_string()
        servidor.sendmail(remetente, destinatario, texto)
        print('E-mail enviado com sucesso!')
    except Exception as e:
        print(f'Erro ao enviar o e-mail: {e}')
    finally:
        servidor.quit()
