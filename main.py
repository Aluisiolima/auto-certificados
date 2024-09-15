import os
import pandas as pd
from fpdf import FPDF
from tkinter import filedialog
from tkinter import ttk
import tkinter as tk
from mudandoImg import Certificado 


def main(planilha):
    mensagem_init = tk.Label(janela, text="carrengando a planilha!!!" ,fg='white', bg='#3CCAE0')
    mensagem_init.pack(pady=10)
    
   
    # Carregar o arquivo Excel
    arquivo_excel = planilha
    df = pd.read_excel(arquivo_excel, engine='openpyxl')



    caminhoPdfs = './pdfs'
    caminhoCertificados = './certificados'

    if not os.path.isdir(caminhoCertificados):
        
        mensagem_create_diretorio_certificados = tk.Label(janela, text="O diretório de certificados não existe. Criando..." ,fg='white', bg='#3CCAE0')
        mensagem_create_diretorio_certificados.pack(pady=10)
        
        os.makedirs(caminhoCertificados, exist_ok=True)

    if not os.path.isdir(caminhoPdfs):
       
        mensagem_create_diretorio_pdfs = tk.Label(janela, text="O diretório de pdf não existe. Criando..." ,fg='white', bg='#3CCAE0')
        mensagem_create_diretorio_pdfs.pack(pady=10)

        os.makedirs(caminhoPdfs, exist_ok=True)


    # Escrever os dados no PDF
    for index, row in df.iterrows():
        inf = dict(row)
        #criado obejeto Certificado
        certificado = Certificado(
            nameAluno=inf['Alunos'],
            nameCurso=inf['nome curso'],
            dataInit=inf['data de inicio'],
            dataFinally=inf['data de termino'],
            cargaHoraria=inf['carga horaria']
                                  )
        #Criar um objeto FPDF
        pdf = FPDF()
        pdf.add_page()

        image_path = certificado.gera_certificado()  # Substitua pelo caminho da sua imagem
        pdf.image(image_path, x=10, y=10, w=190)  # Ajuste a posição e o tamanho da imagem

        pdf_output = f'pdfs/cetificado-{inf['Alunos']}.pdf'
        pdf.output(pdf_output)
        print(pdf_output)
        
    print(f"terminou")




# Função para carregar e exibir o conteúdo do arquivo Excel
# Função para carregar o caminho do arquivo Excel
def carregar_caminho():
    # Abrir caixa de diálogo para seleção do arquivo
    caminho_arquivo = filedialog.askopenfilename(
        title="Selecione um arquivo Excel",
        filetypes=[("Arquivos Excel", "*.xlsx;*.xls")]
    )
    
    if caminho_arquivo:
        label['text'] = 'carrengando a planilha'
        main(caminho_arquivo)
        
        
def app():
    global janela
    # Criando a janela principal
    janela = tk.Tk()
    janela.title("auto-certificação")

    janela.configure(bg='#3CCAE0')

    # Definindo o tamanho da janela
    janela.geometry("600x400")
    janela.iconbitmap("./ico/picture.ico")


    botao = tk.Button(janela, text="carregar planilha excel", command=carregar_caminho)
    botao.pack(padx=100, pady=100)  # O método pack() organiza o widget na janela

    # Adicionando um rótulo (label)
    

    # Inicializando a variável de progresso
    progresso = 0

    # Adicionando a barra de progresso
    barra_progresso = ttk.Progressbar(janela, orient='horizontal', length=300, mode='determinate')
    barra_progresso.pack(pady=10)

    # Adicionando a label para exibir a porcentagem
    label_percentual = tk.Label(janela, text="0%")
    label_percentual.pack(pady=10)

    # Iniciando o loop da interface gráfica
    janela.mainloop()


if __name__ == '__main__':
    app()