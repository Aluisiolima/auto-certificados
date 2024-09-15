import os
import pandas as pd
from fpdf import FPDF
from tkinter import filedialog, scrolledtext, ttk
import tkinter as tk
import threading
from mudandoImg import Certificado 



def main(planilha):
    caixa_detalhes.insert(tk.END, f"carrengando a planilha!!!\n",'verde')
    caixa_detalhes.see(tk.END) 
    janela.update()   
    # Carregar o arquivo Excel
    arquivo_excel = planilha
    df = pd.read_excel(arquivo_excel, engine='openpyxl')



    caminhoPdfs = './pdfs'
    caminhoCertificados = './certificados'

    if not os.path.isdir(caminhoCertificados):

        caixa_detalhes.insert(tk.END, f"O diretório de certificados não existe. Criando...\n", 'true')
        caixa_detalhes.see(tk.END) 
        os.makedirs(caminhoCertificados, exist_ok=True)
        janela.update()  


    if not os.path.isdir(caminhoPdfs):
        caixa_detalhes.insert(tk.END, f"O diretório de pdf não existe. Criando...\n", 'true')
        caixa_detalhes.see(tk.END) 

        os.makedirs(caminhoPdfs, exist_ok=True)
        janela.update()  


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

        caixa_detalhes.insert(tk.END, f"criado o certificado da: {inf['Alunos']}\n", 'true')
        caixa_detalhes.see(tk.END) 

        janela.update()  

    caixa_detalhes.insert(tk.END, f"terminou agora e so imprimir!!!\n", 'true')
    caixa_detalhes.see(tk.END) 
    janela.update()   
    




# Função para carregar e exibir o conteúdo do arquivo Excel
# Função para carregar o caminho do arquivo Excel
def carregar_caminho():
    try:
        # Abrir caixa de diálogo para seleção do arquivo
        caminho_arquivo = filedialog.askopenfilename(
            title="Selecione um arquivo Excel",
            filetypes=[("Arquivos Excel", "*.xlsx;*.xls")]
        )
        
        if caminho_arquivo:
            gerador = threading.Thread(target=main, args=(caminho_arquivo,))
            gerador.start()
            

    except Exception as e :
        caixa_detalhes.insert(tk.END, f"Ocorreu um ERROR!!!:{e}\n", 'false')
        caixa_detalhes.see(tk.END)
    
    
        
def app():
    global janela,caixa_detalhes
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
    #progresso = 0

    # Adicionando a barra de progresso
    barra_progresso = ttk.Progressbar(janela, orient='horizontal', length=300, mode='determinate')
    barra_progresso.pack(pady=10)

    # Adicionando a label para exibir a porcentagem
    label_percentual = tk.Label(janela, text="0%")
    label_percentual.pack(pady=10)

    caixa_detalhes = scrolledtext.ScrolledText(janela, width=50, height=10, wrap=tk.WORD,bg='black',fg='white')
    caixa_detalhes.tag_config('true',background='green')
    caixa_detalhes.tag_config('false',background='red')
    caixa_detalhes.pack(pady=10)

    # Iniciando o loop da interface gráfica
    janela.mainloop()


if __name__ == '__main__':
    app()