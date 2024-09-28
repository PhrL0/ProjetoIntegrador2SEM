from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def criaPdf(num,nomeArquivo):
    # Crie um arquivo PDF em branco
    parse = str(num)
    c = canvas.Canvas(nomeArquivo, pagesize=letter)

    # Defina o título do documento
    c.setTitle("Meu Documento PDF")

    # Adicione texto ao PDF
    c.drawString(100, 750, f'Objetos contados hoje:{parse}')

    # Salve o arquivo PDF
    c.showPage()
    c.save()

    return nomeArquivo

    
