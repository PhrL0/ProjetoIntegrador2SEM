import mysql.connector

#DEPENDENCIAS PDF
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

#CONSULTA BANCO
conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'aluno',
    database = 'teste',
)

cursor = conexao.cursor()

comando = f'SELECT SUM(contador_acumulado) AS total_objetos FROM dados;'
cursor.execute(comando)

resultado = cursor.fetchall()

numeroBd = resultado[0][0]  

print(numeroBd)
cursor.close()
conexao.close()

###########################################################
#GERA PDF 

# Crie um arquivo PDF em branco
c = canvas.Canvas("exemplo.pdf", pagesize=letter)

# Defina o título do documento
c.setTitle("Meu Documento PDF")

# Adicione texto ao PDF
c.drawString("Olá, Sophia!",numeroBd)

# Salve o arquivo PDF
c.showPage()
c.save()
print("PDF criado com sucesso.")


