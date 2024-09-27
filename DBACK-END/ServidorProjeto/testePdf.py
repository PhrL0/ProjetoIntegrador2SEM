from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Crie um arquivo PDF em branco
c = canvas.Canvas("exemplo.pdf", pagesize=letter)

# Defina o título do documento
c.setTitle("Meu Documento PDF")

# Adicione texto ao PDF
c.drawString(100, 750, "Olá, Sophia!")

# Salve o arquivo PDF
c.showPage()
c.save()
print("PDF criado com sucesso.")