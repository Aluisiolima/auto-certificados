# from PIL import Image, ImageDraw

# # Criando uma imagem em branco
# image = Image.new("RGB", (300, 300), (255, 255, 255))  # Fundo branco
# draw = ImageDraw.Draw(image)

# # Definindo as coordenadas do retângulo
# quadrado = [(50, 50), (250, 250)]

# # Desenhando o retângulo sem borda (sem outline)
# draw.rectangle(quadrado,outline='black', fill="blue")

# # Salvando a imagem
# image.save("retangulo_sem_borda.png")
# image.show()
def adicionar_espaco_entre_palavras(texto, espaco_extra):
    palavras = texto.split()
    texto_espacado = (' ' * espaco_extra).join(palavras)
    return texto_espacado

texto = "Olá mundo, como vai você?"
espaco_extra = 2  # Espaçamento extra entre palavras

texto_espacado = adicionar_espaco_entre_palavras(texto, espaco_extra)
print(texto_espacado)
