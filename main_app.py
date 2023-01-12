from tkinter.ttk import*
from tkinter import*
from tkinter import Tk, StringVar, ttk
from PIL import Image, ImageTk
import pyglet
from paises import *
from datetime import datetime
from pytz import country_timezones
import pytz

pyglet.font.add_file('digital-7.ttf')

#cores 
co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # branca
co2 = "#34c6eb"  # Azul
co3 = "#38576b"  # valor

#criando janela 
janela = Tk()
janela.title('')
janela.geometry('300x190')
janela.configure(background=co3)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")

janela.mainloop

#criando frames

frameCima = Frame(janela, width=300, height=50, bg=co1, relief=FLAT)
frameCima.grid(row=0, column=0, columnspan=2)

frameDireita = Frame(janela, width=300, height=390, bg=co0, relief=FLAT)
frameDireita.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

# Abrindo imagem 
app_img = Image.open('./icon.png')
app_img = app_img.resize((40,40))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, text=' Relogio mundial', 
width=920, compound=LEFT, relief=FLAT, anchor=NW, font=('digital-725'), bg=co1, fg=co0)

app_logo.place(x=0, y=0)

frameDireita_conteudo_0 = Frame(frameDireita, width=300, height=35, 
bg=co1, relief=RAISED)

frameDireita_conteudo_0.grid(row= 0, column=0, padx=0, pady=0,sticky=NSEW)

frameDireita_conteudo_1 = Frame(frameDireita, width=300,  height=155, bg=co1, relief=FLAT)

frameDireita_conteudo_1.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

#trabalhando com o frame conteudo 1 -----------------------------------------------------

l_zona = Label(frameDireita_conteudo_0, text="Fuso horario *", width=35, height=1, anchor=NW, font=('Ivy 10 '), bg=co1, fg=co0)
l_zona.place(x=10, y=10)

c_zona = Combobox(frameDireita_conteudo_0, width=25)
# recebendo as zonas


#recebendo as zonas

c_zona.set('Asia/Kolkata')
c_zona.place(x=123, y=10)

c_zona = Combobox(frameDireita_conteudo_0, width=25)

#recebendo as zonas
c_zona.set('Asia/Kolkata')
c_zona.place(x=123, y=10)

#Trabalhando no frame conteudo 2 ----------------------------------------------------------

l_cidade = Label(frameDireita_conteudo_1, text='New York', anchor=NW,
 font=('Arial 10 '), bg=co1, fg=co0)

l_cidade.place(x=10, y=8)

l_pais = Label(frameDireita_conteudo_1, text='USA', anchor=NW,
 font=('Arial  10 '), bg=co1, fg=co0)

l_pais.place(x=10, y=28)
 
l_horas = Label(frameDireita_conteudo_1, text="10:05:05", font=('digital-7  25 bold'), bg=co1, fg=co2)

l_horas.place(x=10, y=45)

l_periodo = Label(frameDireita_conteudo_1, text="PM", anchor=NW, font=('Verdana 10'), bg=co1, fg=co2)

l_periodo.place(x=120, y=60)

l_data = Label(frameDireita_conteudo_1, font=('Arial 8'), bg=co1, fg=co0)

l_data.place(x=10, y=79)

# codigo a parte para obter zonas de fuso horario -----------------

 

# obtendo  Zonas com abreviacao do pais                          

timezone_country = {}          

for countrycode in country_timezones:

    timezones = country_timezones[countrycode]

    for timezone in timezones:

        timezone_country[timezone] = countrycode

# lista das zonas ( fuso horarios )

zonas = []

for i in timezone_country.keys():

    zonas.append(i)

# recebendo as zonas

c_zona['values']= (zonas)

# funcoes ---------------------------------------------------------

 

# definindo algumas variaveis globais

global l_icon, img_bandeira

 

def relogio():

    global l_icon, img_bandeira

   

    zona = c_zona.get()

   

    # convertendo a zona selecionada no formato de timezone  

    zona_selecionada = pytz.timezone(zona)

   

    # obtendo a hora da zona selecionada

    country_time = datetime.now(zona_selecionada)

   

    # variavel que tera o simbolo do pais

    simbol_do_pais = [timezone_country[zona]]

 

    for i in paises.keys():

        simbol_do_pais.append(i.lower())

 

    # usando format para obter o caminho da imagem ( bandeira do pais)

    imagem = "./png250px/{}.{}".format(simbol_do_pais[0],'png').lower()

 

    # obtendo o key do pais em letra maiusculas

    key = simbol_do_pais[0].upper()

 

    # obtendo o nome do pais

    nome_do_pais = paises[key]

   

    tempo = country_time

    horas = tempo.strftime("%H:%M:%S")

    dia_da_semana = tempo.strftime("%A")

    dia = tempo.day

    mes = tempo.strftime("%B")

    ano = tempo.strftime("%Y")

    periodo = tempo.strftime("%p")
# passando os dados pelas labels

    l_cidade.config(text=zona)

    l_pais.config(text=nome_do_pais)

    l_horas.config(text=horas)

    l_data.config(text=dia_da_semana +", "+ "" + str(dia) + " " + str(mes) + " " + (ano) + " " + (periodo))

    l_periodo.config(text=(periodo))
    # imagem bandeira

    img_bandeira = Image.open(imagem)

    img_bandeira = img_bandeira.resize((105, 64))

    img_bandeira = ImageTk.PhotoImage(img_bandeira)

 

    l_icon = Label(frameDireita_conteudo_1,image=img_bandeira, bg=co0, relief='solid')

    l_icon.place(x=185, y=25)
    # reiniciando a funcao apos 1segundo

    l_horas.after(200, relogio)

 # Executando a funcao Relogio

relogio()

janela.mainloop()