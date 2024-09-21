from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

class Certificado:

    def __init__(self,* ,nameAluno : str,cargaHoraria : str, dataInit : str, dataFinally : str, nameCurso : str):
        self.nameAluno = nameAluno
        self.cargaHoraria = cargaHoraria
        self.dataInit = dataInit
        self.dataFinally = dataFinally
        self.nameCurso = nameCurso   
        self.img = Image.open('certificado.png')
        self.draw = ImageDraw.Draw(self.img)

    def verificacao_name(self,nome2):
        ligacoes = ['de', 'do', 'da', 'dos', 'das', "d'", 'di', 'del', 'du', 'von', 'van', 'a', 'à', 'e', 'com']

        if nome2 in ligacoes:
            return False
        
        return True





    def gera_aluno_name(self):
        draw = self.draw
        nome = self.nameAluno

        nome2 = nome.split()
        nomeM = [nome2.capitalize() if self.verificacao_name(nome2) else nome2.lower() for nome2 in nome2]
        nomeEspacamento = (' ' * 2).join(nomeM)

        font = ImageFont.truetype("fontes/GreatVibes-Regular/GreatVibes-Regular.ttf", 150)

        quadrado = [(627, 1184),(2872, 1434)]  

        draw.rectangle(quadrado,width=0)
        cor = "#334166" 


        bbox = draw.textbbox((0, 0), nomeEspacamento, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        # Calculando as coordenadas para centralizar o texto
        x = (quadrado[0][0] + quadrado[1][0] - text_width) // 2
        y = (quadrado[0][1] + quadrado[1][1] - text_height) // 2

        draw.text((x,y), nomeEspacamento, font=font, fill=cor)
        
        
    def gera_text_aluno(self):
        draw = self.draw
        color_text = "#334166"

        # Definindo as coordenadas do retângulo
        quadrado = [(627, 1490), (2875, 1762)]

        text1 = f'CONCLUIU COM EXCELENTE APROVEITAMENTO O CURSO DE {self.nameCurso},'
        text2 = f'NA MODALIDADE PRESENCIAL, EM NOSSA INSTITUIÇÃO DE ENSINO, ATINGINDO UM TOTAL'
        text3 = f'DE {int(self.cargaHoraria)} HORAS DE AULAS NO PERÍODO DE {self.dataInit} À {self.dataFinally}.'

        font = ImageFont.truetype("fontes/OpenSans/static/OpenSans_Condensed-ExtraBold.ttf", 60)

        # Desenhando o retângulo 
        draw.rectangle(quadrado, width=0)

         # Função para calcular a posição do texto horizontamente
        def calcula_posicao_texto(texto, posicao_y):
            bbox = draw.textbbox((0, 0), texto, font=font)
            text_width = bbox[2] - bbox[0]
                    
            x = (quadrado[0][0] + quadrado[1][0] - text_width) // 2
            y = posicao_y

            return (x, y)

        # Definindo a posição inicial do texto e o espaçamento entre linhas
        margin_top = quadrado[0][1] + 10  # Margem superior do retângulo
        espaco_entre_line = 10  # Espaçamento entre linhas


        x1, y1 = calcula_posicao_texto(text1, margin_top)
        draw.text((x1, y1), text1.upper(), font=font, fill=color_text)

        margin_top += draw.textbbox((0, 0), text1, font=font)[3] - draw.textbbox((0, 0), text1, font=font)[1] + espaco_entre_line
        x2, y2 = calcula_posicao_texto(text2, margin_top)
        draw.text((x2, y2), text2.upper(), font=font, fill=color_text)

        margin_top += draw.textbbox((0, 0), text2, font=font)[3] - draw.textbbox((0, 0), text2, font=font)[1] + espaco_entre_line
        x3, y3 = calcula_posicao_texto(text3, margin_top)
        draw.text((x3, y3), text3.upper(), font=font, fill=color_text)


    def ano_gerado(self):
        draw = self.draw
        ano = datetime.now().year
        # Definindo as coordenadas do retângulo
        quadrado = (1500, 2125)
        font = ImageFont.truetype("./fontes/OpenSans/static/OpenSans-ExtraBold.ttf", 120)

        # Desenhando o retângulo sem borda (sem outline)
        draw.rectangle(quadrado,width=0)
        draw.text(quadrado, str(ano), fill="#334166",font=font)


    def gera_certificado(self,output_pdf_path):
        self.gera_aluno_name()
        self.gera_text_aluno()
        self.ano_gerado()

        img_path = f'certificados/certificado-{self.nameAluno}.png'
        self.img.save(img_path)
        self.img.convert('RGB').save(output_pdf_path, save_all=True, resolution=100.0)

        
        return img_path






