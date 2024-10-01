from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime


def criaPdf(nomeArquivo,titulo,nome,classe,observacao):
    # Crie um arquivo PDF em branco
    c = canvas.Canvas(nomeArquivo, pagesize=letter)

    # Defina o título do documento
    c.setTitle(titulo)

    # Adicione texto ao PDF
    c.drawAlignedString(100, 750, f'Relatório de Solicitação')
    c.drawString(100,700, f'Nome do Solicitante: {nome}')
    c.drawString(100,675,f'Objeto Selecionado: {classe}')
    c.drawString(100,650,f'Título: {titulo}')
    c.drawString(100,625,f'Observações:{observacao}')
    c.drawString(100,630,f' ---------------------------')
    c.drawString(100,631,f'Data: {datetime.now().strftime("%d/%m/%Y")}')

    # Salve o arquivo PDF
    c.showPage()
    c.save()

    return nomeArquivo

    
