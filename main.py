from tkinter import *
from PIL import Image,ImageTk
from funcionCalc import calc,EndWith3Div
##VARIABLES GLOBALES##
i = 0 #ITERABLE DE COLUMNAS
tamanoImg = (50,50) #DIMENCIONES PREDETERMINADAS
Bg = "DarkSlateGrey" # COLOR DE FONDO
numLabels = [] #LISTA PARA EL CONTROL DE LABELS
operacion = ""
contadorCol = 0
urlLayout = "C" + __file__[1:].replace("main.py","") + "/Image/"

##VENTANA##
ventana = Tk()
ventana.title("Calculadora++")
ventana.iconbitmap(urlLayout + "Icono.ico")
ventana.geometry("500x500")
ventana.resizable(0,0)
ventana.config(bg = Bg)

##IMAGENES##   
images = {
    "0" : ImageTk.PhotoImage(Image.open(urlLayout + "Zero.png").resize(tamanoImg)),
    "1" : ImageTk.PhotoImage(Image.open(urlLayout + "1.jpg").resize(tamanoImg)),
    "2" : ImageTk.PhotoImage(Image.open(urlLayout + "2.png").resize(tamanoImg)),
    "3" : ImageTk.PhotoImage(Image.open(urlLayout + "3.jpg").resize(tamanoImg)),
    "4" : ImageTk.PhotoImage(Image.open(urlLayout + "4.png").resize(tamanoImg)),
    "5" : ImageTk.PhotoImage(Image.open(urlLayout + "5.jpg").resize(tamanoImg)),
    "6" : ImageTk.PhotoImage(Image.open(urlLayout + "6.png").resize(tamanoImg)),
    "7" : ImageTk.PhotoImage(Image.open(urlLayout + "7.jpg").resize(tamanoImg)),
    "8" : ImageTk.PhotoImage(Image.open(urlLayout + "8.png").resize(tamanoImg)),
    "9" : ImageTk.PhotoImage(Image.open(urlLayout + "9.jpg").resize(tamanoImg)),
        #IMAGENES DE LOS SIGNOS
    "*" : ImageTk.PhotoImage(Image.open(urlLayout + "x.jpg").resize(tamanoImg)),
    "+" : ImageTk.PhotoImage(Image.open(urlLayout + "+.jpg").resize(tamanoImg)), 
    "-" : ImageTk.PhotoImage(Image.open(urlLayout + "-.png").resize(tamanoImg)),
    "/" : ImageTk.PhotoImage(Image.open(urlLayout + "div.png").resize(tamanoImg)),
        #EASTER EGG
    "777" : ImageTk.PhotoImage(Image.open(urlLayout + "777.jpg").resize(tamanoImg)),
    "." : ImageTk.PhotoImage(Image.open(urlLayout + "punto.jpg").resize(tamanoImg))
}

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
out = Frame(ventana,width = 500,height = 50)
out.config(
    bg = Bg,
    relief  = "solid"
)
out.grid(
    column = 0,
    row = 1,
    columnspan = 1,
    sticky = W,
)

##FRAME TECLAS##
teclas = Frame(ventana ,width=500, height = 400)
teclas.config(bg = "Grey")
teclas.grid(column = 0, row = 2,sticky = W)

##AÑADIR LABEL##
def AddLabel(label):
    #Traemos la variable global operación y la usamos para agregarle el dato a este string global
    global operacion
    global numLabels
    global contadorCol
    operacion += label
    #Traemos la variable globall operación para añadirle el label
    localLabel = Label(out,image=images[label])
    localLabel.config(
        bd=1
        )
    numLabels.append(localLabel)
    #Tramos contadorCol para añadir el numero en una columna y continuar con la otra
    localLabel.grid(
    sticky = E,
    padx = 1,
    row = 1,
    column = contadorCol
    )
    contadorCol += 1

##MOSTRAR EL RESULTADO##
def ShowOutCome():
    #Quitamos todos los labeles
    _removeLabels()
   #Esta vez nos traemos operación para darle un resultado y mostrarlo
    global operacion
    print(operacion + " =", eval(operacion))
    resultado = str(eval(operacion))
    #Agregamos un label con cada imagen del resulado
    for index in resultado:
        AddLabel(index)
    operacion = resultado

##BORRAR TODOS LOS LABELES##
def _removeLabels():
    #Traemos la lista de labeles para remover cada uno de ellos
    global numLabels
    for label in numLabels:
        label.grid_remove()
    
def DeleteAll():
    #Obtenemos el texto de operaciones global y lo reiniciamos a "" y quitamos todos los labeles
    global operacion
    global numLabels
    global contadorCol
    operacion = ""
    #Vacíamos de la misma manera la lista de labeles y reiniciamos el contador actual de columnas a 0
    numLabels.clear()
    contadorCol = 0
    _removeLabels()

def DeleteOne():
    #Traemos el string de operación y la lista de numlabels y eliminamos el ultimo elemento y caracter
    global operacion
    global numLabels
    global contadorCol
    operacion = operacion[:-1]
    numLabels.pop().grid_remove()
    #Reducimos la columna actual en uno para moverlo atras
    contadorCol -= 1

    
##OPCIONES ESPECIALES##
##BOTONES##

#NUMEROS##
Button(teclas,text = "0",command = lambda:AddLabel("0"),padx = 50,pady = 33).grid(sticky = W,column = 0,row = 0)
Button(teclas,text = "1",command = lambda:AddLabel("1"),padx = 50,pady = 33).grid(sticky = W,column = 1,row = 0)
Button(teclas,text = "2",command = lambda:AddLabel("2"),padx = 50,pady = 33).grid(sticky = W,column = 2,row = 0)
Button(teclas,text = "3",command = lambda:AddLabel("3"),padx = 50,pady = 33).grid(sticky = W,column = 0,row = 1)
Button(teclas,text = "4",command = lambda:AddLabel("4"),padx = 50,pady = 33).grid(sticky = W,column = 1,row = 1)
Button(teclas,text = "5",command = lambda:AddLabel("5"),padx = 50,pady = 33).grid(sticky = W,column = 2,row = 1)
Button(teclas,text = "6",command = lambda:AddLabel("6"),padx = 50,pady = 33).grid(sticky = W,column = 0,row = 2)
Button(teclas,text = "7",command = lambda:AddLabel("7"),padx = 50,pady = 33).grid(sticky = W,column = 1,row = 2)
Button(teclas,text = "8",command = lambda:AddLabel("8"),padx = 50,pady = 33).grid(sticky = W,column = 2,row = 2)
Button(teclas,text = "9",command = lambda:AddLabel("9"),padx = 50,pady = 33).grid(sticky = W,column = 1,row = 3)
##SIMBOLOS##
Button(teclas,text = "+",command = lambda:AddLabel("+"),padx = 50,pady = 33).grid(sticky = W,column = 3,row = 0)
Button(teclas,text = "-",command = lambda:AddLabel("-"),padx = 50,pady = 33).grid(sticky = W,column = 3,row = 1)
Button(teclas,text = "x",command = lambda:AddLabel("*"),padx = 50,pady = 33).grid(sticky = W,column = 3,row = 2)
Button(teclas,text = "/",command = lambda:AddLabel("/"),padx = 50,pady = 33).grid(sticky = W,column = 3,row = 3)
Button(teclas,text = "=",command = ShowOutCome,padx = 221,pady = 10).grid(sticky = W,column = 0,columnspan = 4,row = 4)
##OPCIONES ESPECIALES##
Button(teclas,text = "DEL",command = DeleteOne,padx = 43,pady = 33).grid(sticky = W,column = 0,row = 3)
Button(teclas,text = "AC",command = DeleteAll,padx = 45,pady = 33).grid(sticky = W,column = 2,row = 3)
ventana.mainloop()
#EASTER EGG: CON TRES SIETES LA IMAGEN DE VEGETTA 