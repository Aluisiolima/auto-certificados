from PIL import Image, ImageDraw, ImageFont

# Abrindo uma imagem
img = Image.open('certificado.png')
texto = str(input("texto:"))

def nameAluno():
    # Inicializando o objeto para desenhar na imagem
    draw = ImageDraw.Draw(img)

    # Definindo a fonte (você pode usar uma fonte .ttf externa se preferir)
    # Exemplo com fonte externa: ImageFont.truetype("caminho_da_fonte.ttf", tamanho)
    font = ImageFont.truetype("fontes/GreatVibes-Regular.ttf", 80)

    quadrado = [(264, 446),(1125,566)]  # coordenadas X e Y

    draw.rectangle(quadrado,width=0)
    cor = (0,0,0)  # cor do texto (branco)

    # Usando textbbox para calcular o tamanho do texto
    bbox = draw.textbbox((0, 0), texto, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # Calculando as coordenadas para centralizar o texto
    x = (quadrado[0][0] + quadrado[1][0] - text_width) // 2
    y = (quadrado[0][1] + quadrado[1][1] - text_height) // 2

    draw.text((x,y), texto.capitalize(), font=font, fill=cor)

nameAluno()
# Salvando a imagem com o texto
img.save(f'certificados/imagem_com_texto_{texto}.png')

# Mostrando a imagem com o texto (opcional)
img.show()


