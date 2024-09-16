import os
import pandas as pd
from tkinter import filedialog, scrolledtext, ttk
import tkinter as tk
import threading
from mudandoImg import Certificado 



def main(planilha):
    global barra_progresso, label_percentual
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

   # Adicionando a barra de progresso
    barra_progresso = ttk.Progressbar(janela, orient='horizontal', length=300, mode='determinate')
    barra_progresso.pack()

    # Adicionando a label para exibir a porcentagem
    label_percentual = tk.Label(janela, text="0%")
    label_percentual.pack(pady=10) 

    janela.update() 
    # Escrever os dados no PDF
    for index, row in df.iterrows():
        inf = dict(row)
        pocentagem_total = (100 / len(df)) * (index + 1)
        #criado obejeto Certificado
        certificado = Certificado(
            nameAluno=inf['Alunos'],
            nameCurso=inf['nome curso'],
            dataInit=inf['data de inicio'],
            dataFinally=inf['data de termino'],
            cargaHoraria=inf['carga horaria']
                                  )
        #Criar um objeto FPDF

        pdf_output = f'pdfs/cetificado-{inf['Alunos']}.pdf'
        image_path = certificado.gera_certificado(output_pdf_path=pdf_output)  # Substitua pelo caminho da sua image

        caixa_detalhes.insert(tk.END, f"criado o certificado da: {inf['Alunos']} e tambem {image_path}\n", 'true')
        caixa_detalhes.see(tk.END) 
        
        atualizar_progresso(pocentagem_total)

        janela.update()  

    caixa_detalhes.insert(tk.END, f"terminou agora e so imprimir!!!\n")
    caixa_detalhes.see(tk.END) 
    janela.update()   
    

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


def atualizar_progresso(progresso):

    if progresso > 100:
        progresso = 100

    # Atualiza a barra de progresso
    barra_progresso['value'] = progresso

    # Atualiza a label de porcentagem
    label_percentual.config(text=f"{int(progresso)}%")
 
        
def app():
    global janela,caixa_detalhes,label_percentual,barra_progresso
    # Criando a janela principal
    janela = tk.Tk()
    janela.title("auto-certificação")

    janela.configure(bg='#3CCAE0')

    # Definindo o tamanho da janela
    janela.geometry("600x400")
    janela.iconbitmap("./ico/picture.ico")

    botao = tk.Button(janela, text="carregar planilha excel", command=carregar_caminho,width=30,height=2,bg='green',font=16,fg='white')
    botao.pack(padx=50, pady=50)  


    caixa_detalhes = scrolledtext.ScrolledText(janela, width=50, height=10, wrap=tk.WORD,bg='black',fg='white')
    caixa_detalhes.tag_config('true',background='green')
    caixa_detalhes.tag_config('false',background='red')
    caixa_detalhes.pack(pady=10)
    # Iniciando o loop da interface gráfica
    janela.mainloop()


if __name__ == '__main__':
    app()
    