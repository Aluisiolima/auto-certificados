from tkinter import Frame, Button, scrolledtext, ttk, Label, filedialog, END
from threading import Thread
from pandas import read_excel, DataFrame
from src.certificado import Certificado
import os
import gc

class Tela(Frame):
    def __init__(self, master):
        super().__init__(master=master, bg='#3CCAE0')
        self.label_procetual = None
        self.barra_progresso = None
        self.caixa_detalhes = None
        self.total_linhas = 0
        self.caminho_pdfs = os.path.join('.', 'pdfs')
        self.caminho_certificados = os.path.join('.', 'certificados')
        self.criar_widgets()
        self.verificar_se_pasta_existe()
    
    def criar_widgets(self):
        Button(self, text="Gerar Certificados", command=self.selecionar_planilha, bg='green', fg='white', width=30, height=2).pack(pady=20)
        self.caixa_detalhes = scrolledtext.ScrolledText(self, width=60, height=12, wrap='word', bg='black', fg='white')
        self.caixa_detalhes.tag_config('verde', background='green')
        self.caixa_detalhes.tag_config('vermelho', background='red')
        self.caixa_detalhes.pack(pady=10)
        self.barra_progresso = ttk.Progressbar(self, orient='horizontal', length=300, mode='determinate')
        self.barra_progresso.pack()

        self.label_percentual = Label(self, text="0%")
        self.label_percentual.pack(pady=10)

    def atualizar_progresso(self, valor: float):
        if valor > 100:
            valor = 100
        self.barra_progresso['value'] = valor
        self.label_percentual.config(text=f"{int(valor)}%")
        self.update()

    def exibir_mensagem(self, mensagem: str, cor: str='verde'):
        self.caixa_detalhes.insert('end', mensagem + '\n', cor)
        self.caixa_detalhes.see('end')
        self.update()

    def limpar_caixa_detalhes(self):
        self.caixa_detalhes.delete('1.0', 'end')
        self.caixa_detalhes.tag_remove('verde', '1.0', 'end')
        self.caixa_detalhes.tag_remove('vermelho', '1.0', 'end')
        self.barra_progresso['value'] = 0
        self.label_percentual.config(text="0%")

    def gerar_certificados(self, df: DataFrame):
        try:
            self.exibir_mensagem("Iniciando o processo de geração de certificados...", 'verde')
            for index, row in df.iterrows():
            
                dados = dict(row)
                certificado = Certificado(
                    nameAluno=dados['Alunos'],
                    nameCurso=dados['nome curso'],
                    dataInit=dados['data de inicio'],
                    dataFinally=dados['data de termino'],
                    cargaHoraria=dados['carga horaria']
                )
                nome_arquivo = f"certificado-{dados['Alunos'].strip()}.pdf"
                caminho_pdf = os.path.join(self.caminho_pdfs, nome_arquivo)
                image_path = certificado.gera_certificado(output_pdf_path=caminho_pdf)
                self.exibir_mensagem(f"Certificado criado: {dados['Alunos']} ({image_path})", 'verde')
                self.exibir_mensagem(f"Arquivo PDF salvo em: {caminho_pdf}", 'verde')
                progresso = ((index + 1) / self.total) * 100
                self.atualizar_progresso(progresso)
                self.update()

                df = None
                gc.collect() 

        except Exception as erro_individual:
            self.exibir_mensagem(f"Erro com {dados.get('Alunos', 'Aluno desconhecido')}: {erro_individual}\n", 'vermelho')

    def ler_planilha(self, caminho_arquivo: str):
        try:
            df = read_excel(caminho_arquivo, engine='openpyxl')
            self.total = len(df)
            self.gerar_certificados(df)
        except Exception as e:
            self.exibir_mensagem(f"Erro ao carregar a planilha: {e}\n", 'vermelho')
            return


    def selecionar_planilha(self):
        self.limpar_caixa_detalhes()
        caminho_arquivo = filedialog.askopenfilename(
            title="Selecione um arquivo Excel",
            filetypes=[("Arquivos Excel", "*.xlsx;*.xls"),
                       ("Todos os arquivos", "*.*")]
        )
        if caminho_arquivo:
            thread = Thread(target=self.ler_planilha, args=(caminho_arquivo,))
            thread.start()

    def verificar_se_pasta_existe(self):
        for caminho in [self.caminho_pdfs, self.caminho_certificados]:
            if not os.path.isdir(caminho):
                os.makedirs(caminho, exist_ok=True)
                self.exibir_mensagem(f"Pasta '{caminho}' criada com sucesso!", 'verde')

