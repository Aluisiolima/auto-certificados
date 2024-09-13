from PIL import Image, ImageDraw, ImageFont

#texto = str(input("texto:"))

class Certificado:

    def __init__(self,* ,nameAluno : str,cargaHoraria : str, dataInit : str, dataFinally : str, nameCurso : str,ano = None):
        self.nameAluno = nameAluno
        self.cargaHoraria = cargaHoraria
        self.dataInit = dataInit
        self.dataFinally = dataFinally
        self.nameCurso = nameCurso   
        self.ano = ano
        self.img = Image.open('certificado.png')
        self.draw = ImageDraw.Draw(self.img)

       
    def gera_aluno_name(self):
        draw = self.draw
        nome = self.nameAluno
        img = self.img

        nome2 = nome.split()
        nomeM = [nome2.capitalize() if len(nome2) > 2 else nome2.lower() for nome2 in nome2]
        nomeEspacamento = (' ' * 2).join(nomeM)

        font = ImageFont.truetype("./fontes/GreatVibes-Regular/GreatVibes-Regular.ttf", 150)

        quadrado = [(627, 1184),(2872, 1434)]  

        draw.rectangle(quadrado,width=0,fill="#fbfbfb")
        cor = (0,0,0) 


        bbox = draw.textbbox((0, 0), nomeEspacamento, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        # Calculando as coordenadas para centralizar o texto
        x = (quadrado[0][0] + quadrado[1][0] - text_width) // 2
        y = (quadrado[0][1] + quadrado[1][1] - text_height) // 2

        draw.text((x,y), nomeEspacamento, font=font, fill=cor)
        
        
    def gera_text_aluno(self):
        draw = self.draw
        img = self.img
        # Definindo as coordenadas do retângulo
        quadrado = [(627, 1490), (2875, 1762)]
        
        # Texto a ser adicionado
        text1 = f'CONCLUIU COM EXCELENTE APROVEITAMENTO O CURSO DE {self.nameCurso},'
        text2 = f'NA MODALIDADE PRESENCIAL, EM NOSSA INSTITUIÇÃO DE ENSINO, ATINGINDO UM TOTAL'
        text3 = f'DE {self.cargaHoraria} HORAS DE AULAS NO PERÍODO DE {self.dataInit} À {self.dataFinally}.'

        font = ImageFont.truetype("./fontes/OpenSans/OpenSans-VariableFont_wdth,wght.ttf", 55)

        # Desenhando o retângulo sem borda (sem outline)
        draw.rectangle(quadrado, fill="#fbfbfb")

        # Função para calcular a posição do texto
        def calcula_posicao_texto(texto, y_offset):
            bbox = draw.textbbox((0, 0), texto, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            
            x = (quadrado[0][0] + quadrado[1][0] - text_width) // 2
            y = y_offset

            return (x, y)

        # Definindo a posição inicial do texto e o espaçamento entre linhas
        start_y = quadrado[0][1] + 10  # Margem superior do retângulo
        line_spacing = 10  # Espaçamento entre linhas

        # Calculando e desenhando cada linha de texto
        x1, y1 = calcula_posicao_texto(text1, start_y)
        draw.text((x1, y1), text1.upper(), font=font, fill="black")

        start_y += draw.textbbox((0, 0), text1, font=font)[3] - draw.textbbox((0, 0), text1, font=font)[1] + line_spacing
        x2, y2 = calcula_posicao_texto(text2, start_y)
        draw.text((x2, y2), text2.upper(), font=font, fill="black")

        start_y += draw.textbbox((0, 0), text2, font=font)[3] - draw.textbbox((0, 0), text2, font=font)[1] + line_spacing
        x3, y3 = calcula_posicao_texto(text3, start_y)
        draw.text((x3, y3), text3.upper(), font=font, fill="black")

        # Salva a imagem
        
            
    def gera_ano_certificado(self):
        draw = self.draw
        img = self.img
        # Definindo as coordenadas do retângulo
        quadrado = [(627, 1490), (2875, 1762)]

    def gera_certificado(self):
        self.gera_aluno_name()
        self.gera_text_aluno()

        img_path = f'certificados/certificado-{self.nameAluno}.png'
        self.img.save(img_path)
        
        return img_path






