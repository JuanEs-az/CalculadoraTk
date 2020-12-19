from tkinter import *
from PIL import Image,ImageTk
from funcionCalc import calc,EndWith3Div
##VARIABLES GLOBALES##
i = 0 #ITERABLE DE COLUMNAS
dim = (50,50) #DIMENCIONES PREDETERMINADAS
Bg = "DarkSlateGrey" # COLOR DE FONDO
labels = [] #LISTA PARA EL CONTROL DE LABELS
numeros = ["",""] #STRING CONTENEDOR DE LA OPERACIÓN
indiceNumero = 0
labelOperacion = "" #LABEL EN EL QUE SE PONE LA OPERACIÓN
Operacion = ""
urlLayout = "C" + __file__[1:].replace("main.py","") + "/Image/"
#"C:/Users/famia/Desktop/Stuff/CODING/PYTHON/Proyectos/Tk/Calc-ImgTk/Image/"
##VENTANA##
ventana = Tk()
ventana.title("Calculadora++")
ventana.iconbitmap(urlLayout + "Icono.ico")
ventana.geometry("500x500")
ventana.resizable(0,0)
ventana.config(bg = Bg)
##IMAGENES##   
images=(
    ImageTk.PhotoImage(Image.open(urlLayout + "Zero.png").resize(dim)),
    ImageTk.PhotoImage(Image.open(urlLayout + "1.jpg").resize(dim)),
    ImageTk.PhotoImage(Image.open(urlLayout + "2.png").resize(dim)),
    ImageTk.PhotoImage(Image.open(urlLayout + "3.jpg").resize(dim)),
    ImageTk.PhotoImage(Image.open(urlLayout + "4.png").resize(dim)),
    ImageTk.PhotoImage(Image.open(urlLayout + "5.jpg").resize(dim)),
    ImageTk.PhotoImage(Image.open(urlLayout + "6.png").resize(dim)),
    ImageTk.PhotoImage(Image.open(urlLayout + "7.jpg").resize(dim)),
    ImageTk.PhotoImage(Image.open(urlLayout + "8.png").resize(dim)),
    ImageTk.PhotoImage(Image.open(urlLayout + "9.jpg").resize(dim)),
    {
        #IMAGENES DE LOS SIGNOS
       "*" : ImageTk.PhotoImage(Image.open(urlLayout + "x.jpg").resize(dim)),
       "+" : ImageTk.PhotoImage(Image.open(urlLayout + "+.jpg").resize(dim)), 
       "-" : ImageTk.PhotoImage(Image.open(urlLayout + "-.png").resize(dim)),
       "/" : ImageTk.PhotoImage(Image.open(urlLayout + "div.png").resize(dim))
    },
    #EASTER EGG
    ImageTk.PhotoImage(Image.open(urlLayout + "777.jpg").resize(dim)),
    ImageTk.PhotoImage(Image.open(urlLayout + "punto.jpg").resize(dim))
)
##TITULO##
tit = Label(ventana, text = "CALCULADORA ++")
tit.config(
    bg = "SlateGrey",
    fg = Bg,
    font = ("Consolas",30)
)
tit.grid(
    column = 0,
    row = 0,
    ipadx = 118,
    sticky = W
)
##FRAME NUMEROS##
Out = Frame(ventana,width = 500,height = 50)
Out.config(
    bg = Bg,
    relief  = "solid"
)
Out.grid(
    column = 0,
    row = 1,
    columnspan = 1,
    sticky = W,
)
##FRAME TECLAS##
teclas = Frame(ventana ,width=500, height = 400)
teclas.config(bg = "Grey")
teclas.grid(column = 0, row = 2,sticky = W)
##AÑADIR IMG##
def add_label(Index):
    #VARIABLES A USAR
    global numeros 
    global indiceNumero
    global i
    global labelOperacion
    global labels
    renderIndex = Index
    #VERIFICAR SI HAY LABELS DE OPERACIONES PARA BORRARLOS
    if Index == ".":
        renderIndex = 12
    if isinstance(labelOperacion,Label):
        labelOperacion.grid_remove()
    #AÑADE EL NUMERO Y CARGA EL RENDER EN EL LABEL
    numeros[indiceNumero] += str(renderIndex)
    render = images[renderIndex]
    lb = Label(Out,image = render)
    lb.config(
        bd = 1,
    )
    labels.append(lb)
    #CASO 777 (EASTER EGG)
                    # CONDICION UTIL PERO NO PERFECTA : strOp.endswith("777") and strOp.count("7") % 3 == 0
    #CAMBIAR CONDICION EVALUAR SI TERMINA POR UN NUMERO DE 7 MULTIPLO DE 3
    if EndWith3Div(numeros[indiceNumero],"7") :
        labels[len(labels)-1].grid_remove()
        labels[len(labels)-2].grid_remove()
        labels[len(labels)-3].grid_remove()
        labels = labels[0:-3]
        lb = Label(Out,image = images[11])
        labels.append(lb)


    lb.grid(
    sticky = E,
    padx = 1,
    row = 1,
    column = i
   )
    i += 1
    print(numeros[indiceNumero])
##OPCIONES ESPECIALES##
def BorrarTodo():
    #VARIABLES A USAR
    global Operacion
    global numeros
    #RECORRE CADA LABEL LIMPIANDO EL OUT
    for label in labels:
        label.grid_remove()
    #SI EL LABEL DE OPERACION ES UN LABEL Y NO UNA CADENA LO BORRA IGUALMENTE
    if isinstance(labelOperacion,Label):
        labelOperacion.grid_remove()
    #LIMPIA LA LISTA Y BORRA TODO 
    labels.clear()
    numeros[0] = ""
    numeros[1] = ""
    Operacion = ""

def BorrarUltimo():
    #VARIABLES A USAR
    global indiceNumero
    global i
    #SI LOS LA CANTIDAD DE LABEL ES AL MENOS UNO BORRA EL ULTIMO LABEL
    if len(labels) > 0:
        #DEFINIR SI LO ULTIMO ES OPERACION O NUMERO
        labels[len(labels)-1].grid_remove()
        labels.pop()
        #CASO 777 (EASTER EGG)
        #CAMBIAR CONDICION
        if EndWith3Div(numeros[indiceNumero],"7"):
            add_label(7)
            add_label(7)
            numeros[indiceNumero] = numeros[indiceNumero][0:-2]
        numeros[indiceNumero] = numeros[indiceNumero][0:-1]
##OPERADORES##
def OperacionF(simbolo):
    #VARIABLES A USAR
    global Operacion
    global indiceNumero
    global labelOperacion
    #QUITAMOS LOS LABELS DE PANTALLA
    operacion = simbolo
    for label in labels:
        label.grid_remove()
    #DEFINIMOS SI HAY NUMEROS ANTES DEL SIGNO
    if len(numeros[indiceNumero]) >= 1:
        #ESTABLECEMOS LA IMAGEN A IMPRIMIR SEGUN EL SIGNO
        if simbolo == "+":
            imagen = images[10]["+"]
        elif simbolo == "-":
            imagen = images[10]["-"]
        elif simbolo == "*":
            imagen = images[10]["*"]
        elif simbolo == "/":
            imagen = images[10]["/"]
        Operacion = simbolo
        labelOperacion = Label(Out,image = imagen)
        labelOperacion.grid(column = 0,row = 0)
        indiceNumero += 1
        labels.clear()
def MostrarResultado():
    global indiceNumero
    global numeros
    global Operacion
    resultado = str(calc(numeros[0],Operacion,numeros[1]))
    BorrarTodo()
    for car in resultado:
        add_label(int(car) if car.isnumeric() else car)
    numeros [0] = resultado
    numeros [1] = ""
    indiceNumero = 0
    Operacion = ""

##BOTONES##

#NUMEROS##
Button(teclas,text = "0",command = lambda:add_label(0),padx = 50,pady = 33).grid(sticky = W,column = 0,row = 0)
Button(teclas,text = "1",command = lambda:add_label(1),padx = 50,pady = 33).grid(sticky = W,column = 1,row = 0)
Button(teclas,text = "2",command = lambda:add_label(2),padx = 50,pady = 33).grid(sticky = W,column = 2,row = 0)
Button(teclas,text = "3",command = lambda:add_label(3),padx = 50,pady = 33).grid(sticky = W,column = 0,row = 1)
Button(teclas,text = "4",command = lambda:add_label(4),padx = 50,pady = 33).grid(sticky = W,column = 1,row = 1)
Button(teclas,text = "5",command = lambda:add_label(5),padx = 50,pady = 33).grid(sticky = W,column = 2,row = 1)
Button(teclas,text = "6",command = lambda:add_label(6),padx = 50,pady = 33).grid(sticky = W,column = 0,row = 2)
Button(teclas,text = "7",command = lambda:add_label(7),padx = 50,pady = 33).grid(sticky = W,column = 1,row = 2)
Button(teclas,text = "8",command = lambda:add_label(8),padx = 50,pady = 33).grid(sticky = W,column = 2,row = 2)
Button(teclas,text = "9",command = lambda:add_label(9),padx = 50,pady = 33).grid(sticky = W,column = 1,row = 3)
##SIMBOLOS##
Button(teclas,text = "+",command = lambda:OperacionF("+"),padx = 50,pady = 33).grid(sticky = W,column = 3,row = 0)
Button(teclas,text = "-",command = lambda:OperacionF("-"),padx = 50,pady = 33).grid(sticky = W,column = 3,row = 1)
Button(teclas,text = "x",command = lambda:OperacionF("*"),padx = 50,pady = 33).grid(sticky = W,column = 3,row = 2)
Button(teclas,text = "/",command = lambda:OperacionF("/"),padx = 50,pady = 33).grid(sticky = W,column = 3,row = 3)
Button(teclas,text = "=",command = MostrarResultado,padx = 221,pady = 10).grid(sticky = W,column = 0,columnspan = 4,row = 4)
##OPCIONES ESPECIALES##
Button(teclas,text = "DEL",command = BorrarUltimo,padx = 43,pady = 33).grid(sticky = W,column = 0,row = 3)
Button(teclas,text = "AC",command = BorrarTodo,padx = 45,pady = 33).grid(sticky = W,column = 2,row = 3)
ventana.mainloop()
#EASTER EGG: CON TRES SIETES LA IMAGEN DE VEGETTA 