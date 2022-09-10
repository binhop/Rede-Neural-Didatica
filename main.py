from neuronio import Neuronio
import random
import tkinter as tk

## DEFINIÇÕES DO TKINTER
# CORES
corazul = "#5c88da"
corbranca = "#edeff2"
coramarela = "#FFF133"
corcinza = "#bdc3c7"
corazulescuro = "#004c98"
# CONFIGURAÇÕES DA TELA
window = tk.Tk()

window.resizable(width=False, height=False)
window.configure(background=corbranca)
window.option_add("*Font", "Consolas 20")
window.title("Rede Neural Artificial") #Nome que fica em cima na janela

# Define o tamanho e a posição do programa
w = 800 # Largura do programa
h = 500 # Altura do programa

ws = window.winfo_screenwidth()
hs = window.winfo_screenheight()

x = (ws/2) - (w/2)
y = (hs/2) - (h/2) - 40

window.geometry('%dx%d+%d+%d' % (w, h, x, y))

# IMAGENS
fantasma = tk.PhotoImage() #Imagem fantasma para colocar no botao para mudar o tamanho dele em pixels
imagem_neuronio = tk.PhotoImage(file="neuronio.png")
imagem_sigmoide = tk.PhotoImage(file="sigmoide.png")

# Fonte
fonte = "Consolas" #Fonte padrao

# Cria o neuronio
neuronio = Neuronio()

def comando_aleatorizar():
    global parametros
    
    neuronio.aleatorizar()
    parametros[0].configure(text = "w1 = %.2f"%(neuronio.w1))
    parametros[1].configure(text = "w2 = %.2f"%(neuronio.w2))
    parametros[2].configure(text = "w3 = %.2f"%(neuronio.w3))
    parametros[3].configure(text = "b = %.2f"%(neuronio.b))

def comando_novos_valores():
    global valores, frames
    
    neuronio.novos_valores()

    valores[0].configure(text = "X1 = %.2f"%(neuronio.x[0][0]))
    valores[1].configure(text = "X2 = %.2f"%(neuronio.x[0][1]))
    valores[2].configure(text = "X3 = %.2f"%(neuronio.x[0][2]))
    valores[3].configure(text = "z1 = %.2f"%(neuronio.z[0]))
    valores[4].configure(text = "a1 = %.4f"%(neuronio.a[0]))
    
    valores[5].configure(text = "X1 = %.2f"%(neuronio.x[1][0]))
    valores[6].configure(text = "X2 = %.2f"%(neuronio.x[1][1]))
    valores[7].configure(text = "X3 = %.2f"%(neuronio.x[1][2]))
    valores[8].configure(text = "z2 = %.2f"%(neuronio.z[1]))
    valores[9].configure(text = "a2 = %.4f"%(neuronio.a[1]))

    valores[10].configure(text = "X1 = %.2f"%(neuronio.x[2][0]))
    valores[11].configure(text = "X2 = %.2f"%(neuronio.x[2][1]))
    valores[12].configure(text = "X3 = %.2f"%(neuronio.x[2][2]))
    valores[13].configure(text = "z3 = %.2f"%(neuronio.z[2]))
    valores[14].configure(text = "a3 = %.4f"%(neuronio.a[2]))

    # Colore a borda dos frames de acordo com o acerto da previsão
    for i in range(3):
        if(neuronio.yreal[i] == int(round(neuronio.a[i]))):
            frames[i].configure(highlightbackground="green")
        else:
            frames[i].configure(highlightbackground="red")

def comando_treinar(epochs = 1):
    global valores, parametros, frames

    neuronio.treinar(epoch = epochs)
    
    parametros[0].configure(text = "w1 = %.2f"%(neuronio.w1))
    parametros[1].configure(text = "w2 = %.2f"%(neuronio.w2))
    parametros[2].configure(text = "w3 = %.2f"%(neuronio.w3))
    parametros[3].configure(text = "b = %.2f"%(neuronio.b))
    
    valores[3].configure(text = "z1 = %.2f"%(neuronio.z[0]))
    valores[4].configure(text = "a1 = %.4f"%(neuronio.a[0]))
    valores[8].configure(text = "z2 = %.2f"%(neuronio.z[1]))
    valores[9].configure(text = "a2 = %.4f"%(neuronio.a[1]))
    valores[13].configure(text = "z3 = %.2f"%(neuronio.z[2]))
    valores[14].configure(text = "a3 = %.4f"%(neuronio.a[2]))

    # Colore a borda dos frames de acordo com o acerto da previsão
    for i in range(3):
        if(neuronio.yreal[i] == int(round(neuronio.a[i]))):
            frames[i].configure(highlightbackground="green")
        else:
            frames[i].configure(highlightbackground="red")


def criar_base():
    global valores, parametros, frames

    # Elementos principais (imagens)
    neuronio = tk.Label(window, image=imagem_neuronio)
    neuronio.place(x=w, y=50, anchor=tk.NE)

    formulaa = tk.Label(window, image=imagem_sigmoide)
    formulaa.place(x=w-5, y=h//2 - 20, anchor=tk.NE)

    # Elementos dos valores de entrada/saida do neuronio
    yi = 0
    xi = 0
    frame1 = tk.Frame(window, highlightthickness=2, width=175, height=30*5 + 15)
    frame1.place(x=xi, y=yi, anchor=tk.NW)
    texto_x11 = tk.Label(frame1, text="X1 = ")
    texto_x11.place(x=xi, y=yi, anchor=tk.NW)

    texto_x21 = tk.Label(frame1, text="X2 =")
    texto_x21.place(x=xi, y=yi+30*1, anchor=tk.NW)

    texto_x31 = tk.Label(frame1, text="X3 =")
    texto_x31.place(x=xi, y=yi+30*2, anchor=tk.NW) 

    texto_z1 = tk.Label(frame1, text="z1 = ")
    texto_z1.place(x=xi, y=yi+30*3, anchor=tk.NW)

    texto_a1 = tk.Label(frame1, text="a1 = ")
    texto_a1.place(x=xi, y=yi+30*4, anchor=tk.NW)


    frame2 = tk.Frame(window, highlightthickness=2, width=175, height=30*5 + 15)
    frame2.place(x=xi, y=yi+30*5 + 15, anchor=tk.NW)
    texto_x12 = tk.Label(frame2, text="X1 = ")
    texto_x12.place(x=xi, y=yi, anchor=tk.NW)

    texto_x22 = tk.Label(frame2, text="X2 =")
    texto_x22.place(x=xi, y=yi+30*1, anchor=tk.NW)

    texto_x32 = tk.Label(frame2, text="X3 =")
    texto_x32.place(x=xi, y=yi+30*2, anchor=tk.NW) 

    texto_z2 = tk.Label(frame2, text="z2 = ")
    texto_z2.place(x=xi, y=yi+30*3, anchor=tk.NW)

    texto_a2 = tk.Label(frame2, text="a2 = ")
    texto_a2.place(x=xi, y=yi+30*4, anchor=tk.NW)


    frame3 = tk.Frame(window, highlightthickness=2, width=175, height=30*5 + 15)
    frame3.place(x=xi, y=yi+30*10 + 30, anchor=tk.NW)
    texto_x13 = tk.Label(frame3, text="X1 = ")
    texto_x13.place(x=xi, y=yi, anchor=tk.NW)

    texto_x23 = tk.Label(frame3, text="X2 =")
    texto_x23.place(x=xi, y=yi+30*1, anchor=tk.NW)

    texto_x33 = tk.Label(frame3, text="X3 =")
    texto_x33.place(x=xi, y=yi+30*2, anchor=tk.NW) 

    texto_z3 = tk.Label(frame3, text="z3 = ")
    texto_z3.place(x=xi, y=yi+30*3, anchor=tk.NW)

    texto_a3 = tk.Label(frame3, text="a3 = ")
    texto_a3.place(x=xi, y=yi+30*4, anchor=tk.NW)

    ## Guarda os textos em uma lista para editá-los
    valores = [texto_x11, texto_x21, texto_x31, texto_z1, texto_a1,
               texto_x12, texto_x22, texto_x32, texto_z2, texto_a2,
               texto_x13, texto_x23, texto_x33, texto_z3, texto_a3]

    frames = [frame1, frame2, frame3]


    # Elementos dos parâmetros
    texto_w1 = tk.Label(window, text="w1 = ")
    texto_w1.place(x=300, y=0, anchor=tk.N)

    texto_w2 = tk.Label(window, text="w2 = ")
    texto_w2.place(x=300+170, y=0, anchor=tk.N)

    texto_w3 = tk.Label(window, text="w3 = ")
    texto_w3.place(x=300+170*2, y=0, anchor=tk.N)

    texto_b = tk.Label(window, text="b = ")
    texto_b.place(x=300+160, y=30, anchor=tk.N)

    parametros = [texto_w1, texto_w2, texto_w3, texto_b]
    

    botao_novos_valores = tk.Button(window, text="Novos valores", font=(fonte, 16),
                              bg=corazulescuro, fg=corbranca, command=comando_novos_valores)
    botao_novos_valores.place(x=w-190, y=h-40, anchor=tk.E)

    botao_aleatorizar = tk.Button(window, text="Aleatorizar", font=(fonte, 16),
                              bg=corazulescuro, fg=corbranca, command=comando_aleatorizar)
    botao_aleatorizar.place(x=w-20, y=h-40, anchor=tk.E)
    comando_aleatorizar()
    
    botao_treinar = tk.Button(window, text="Treinar", font=(fonte, 16),
                              bg=corazulescuro, fg=corbranca, command=comando_treinar)
    botao_treinar.place(x=w-190*2-115, y=h-40, anchor=tk.E)

    botao_treinar_10 = tk.Button(window, text="x10", font=(fonte, 16),
                              bg=corazulescuro, fg=corbranca, command=lambda:comando_treinar(10))
    botao_treinar_10.place(x=w-190*2-65, y=h-40, anchor=tk.E)

    botao_treinar_100 = tk.Button(window, text="x100", font=(fonte, 16),
                              bg=corazulescuro, fg=corbranca, command=lambda:comando_treinar(100))
    botao_treinar_100.place(x=w-190*2, y=h-40, anchor=tk.E)



criar_base()
comando_novos_valores()
