from tkinter import Tk
from src.tela import Tela

class Application(Tk):
    def __init__(self):
        super().__init__()
        self.title("Gerador de Certificados")
        self.geometry("800x600")
        self.configure(bg='#3CCAE0')

        self.tela = Tela(self)
        self.tela.pack(expand=True, fill='both')

