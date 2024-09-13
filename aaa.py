from PIL import Image, ImageDraw

img = Image.open('certificado.png')
draw = ImageDraw.Draw(img)



# Definindo as coordenadas do retângulo
quadrado = [(1400, 2090),(1800, 2250)]

# Desenhando o retângulo sem borda (sem outline)
draw.rectangle(quadrado,outline='black', fill="blue")

# Salvando a imagem
img.save("retangulo_sem_borda.png")
img.show()
# def adicionar_espaco_entre_palavras(texto, espaco_extra):
#     palavras = texto.split()
#     texto_espacado = (' ' * espaco_extra).join(palavras)
#     return texto_espacado

# texto = "Olá mundo, como vai você?"
# espaco_extra = 2  # Espaçamento extra entre palavras

# texto_espacado = adicionar_espaco_entre_palavras(texto, espaco_extra)
# print(texto_espacado)
