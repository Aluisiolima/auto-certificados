import pandas as pd
from fpdf import FPDF

# Carregar o arquivo Excel
arquivo_excel = 'Pasta1.xlsx'
df = pd.read_excel(arquivo_excel, engine='openpyxl')



# Escrever os dados no PDF
for index, row in df.iterrows():
    # Criar um objeto FPDF
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Definir a fonte para o PDF
    pdf.set_font("Arial", size=12)
    linha = f"Linha {index}: {', '.join([str(val) for val in row])}"
    pdf.cell(200, 10, txt=linha, ln=True)
    pdf_output = f'pdfs/dados_excel{index}.pdf'
    pdf.output(pdf_output)

# Salvar o PDF

print(f"Dados escritos no arquivo PDF: {pdf_output}")
