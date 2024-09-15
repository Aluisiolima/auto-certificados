from PIL import Image, ImageDraw, ImageFont

img = Image.open('certificado.png')
draw = ImageDraw.Draw(img)
color_text = "#334166"
        # Definindo as coordenadas do retângulo
quadrado = [(627, 1490), (2875, 1762)]
        
        # Texto a ser adicionado
text1 = 'CONCLUIU COM EXCELENTE APROVEITAMENTO O CURSO DE {self.nameCurso},'
text2 = 'NA MODALIDADE PRESENCIAL, EM NOSSA INSTITUIÇÃO DE ENSINO, ATINGINDO UM TOTAL'
text3 = 'DE {int(self.cargaHoraria)} HORAS DE AULAS NO PERÍODO DE {self.dataInit} À {self.dataFinally}.'

font = ImageFont.truetype("./fontes/OpenSans/static/OpenSans_Condensed-ExtraBold.ttf", 55)

        # Desenhando o retângulo sem borda (sem outline)
draw.rectangle(quadrado, width=0)

        # Função para calcular a posição do texto
def calcula_posicao_texto(texto, posicao_y):
    bbox = draw.textbbox((0, 0), texto, font=font)
    text_width = bbox[2] - bbox[0]
            
    x = (quadrado[0][0] + quadrado[1][0] - text_width) // 2
    y = posicao_y

    return (x, y)

        # Definindo a posição inicial do texto e o espaçamento entre linhas
margin_top = quadrado[0][1] + 10  # Margem superior do retângulo
espaco_entre_line = 10  # Espaçamento entre linhas

        # Calculando e desenhando cada linha de texto
x1, y1 = calcula_posicao_texto(text1, margin_top)
draw.text((x1, y1), text1.upper(), font=font, fill=color_text)

margin_top += draw.textbbox((0, 0), text1, font=font)[3] - draw.textbbox((0, 0), text1, font=font)[1] + espaco_entre_line
x2, y2 = calcula_posicao_texto(text2, margin_top)
draw.text((x2, y2), text2.upper(), font=font, fill=color_text)

margin_top += draw.textbbox((0, 0), text2, font=font)[3] - draw.textbbox((0, 0), text2, font=font)[1] + espaco_entre_line
x3, y3 = calcula_posicao_texto(text3, margin_top)
draw.text((x3, y3), text3.upper(), font=font, fill=color_text)

img_path = f'certificados/certificado.png'
img.save(img_path)
img.show(img_path)
