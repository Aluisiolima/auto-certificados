from PIL import Image, ImageDraw, ImageFont

#texto = str(input("texto:"))

class Certificado:
    def __init__(self,* ,nameAluno,cargaHoraria = None,dataInit = None,dataFinally = None,nameCurso = None,ano = None):
        self.nameAluno = nameAluno
        self.cargaHoraria = cargaHoraria
        self.dataInit = dataInit
        self.dataFinally = dataFinally
        self.nameCurso = nameCurso   
        self.ano = ano
        self.img = Image.open('certificado.png')
        self.draw = draw = ImageDraw.Draw(self.img)

       
    def geraAluno(self):
        draw = self.draw
        nome = self.nameAluno
        img = self.img

        font = ImageFont.truetype("fontes/GreatVibes-Regular.ttf", 150)

        quadrado = [(627, 1184),(2872, 1434)]  

        draw.rectangle(quadrado,width=0,fill="#fbfbfb")
        cor = (0,0,0) 


        bbox = draw.textbbox((0, 0), nome, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        # Calculando as coordenadas para centralizar o texto
        x = (quadrado[0][0] + quadrado[1][0] - text_width) // 2
        y = (quadrado[0][1] + quadrado[1][1] - text_height) // 2

        draw.text((x,y), nome.capitalize(), font=font, fill=cor)
        # Salvando a imagem com o texto
        img_path = f'certificados/imagem_com_texto_{nome}.png'
        img.save(img_path)
        return img_path


    
    




# def cargaHoraria(cargaHoraria){

# }


