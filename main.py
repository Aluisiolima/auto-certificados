import pandas as pd
from fpdf import FPDF
import mudandoImg as imgs

# Carregar o arquivo Excel
arquivo_excel = 'Pasta1.xlsx'
df = pd.read_excel(arquivo_excel, engine='openpyxl')



# Escrever os dados no PDF
for index, row in df.iterrows():
    #criado obejeto Certificado
    certificado = imgs.Certificado(nameAluno=dict(row)['Alunos'])
    # Criar um objeto FPDF
    pdf = FPDF()
    pdf.add_page()

    image_path = certificado.geraAluno()  # Substitua pelo caminho da sua imagem
    pdf.image(image_path, x=10, y=10, w=190)  # Ajuste a posição e o tamanho da imagem

    pdf_output = f'pdfs/cetificado-{dict(row)['Alunos']}.pdf'
    pdf.output(pdf_output)
    print(pdf_output)
    

# Salvar o PDF

#print(f"Dados escritos no arquivo PDF: {pdf_output}")
