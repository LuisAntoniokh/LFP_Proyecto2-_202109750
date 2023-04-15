from tkinter import *


class Pantalla_Principal():
    def __init__(self):
        self.vMain = Tk()
        self.vMain.title("Proyecto #2 - 202109750 - Luis Castro")
        self.vMain.geometry("580x400")
        self.vMain.config(bg = "#2d98da")
        self.vMain.resizable(False, False)
        self.p1()
        self.vMain.mainloop()
    
    def p1(self):
        self.Texto = ""

        Button(self.vMain, text="Archivo", font=("Arial", 12),  width=15, command=self.pArchivo).place(x=0, y=0)
        Button(self.vMain, text="Análisis", font=("Arial", 12),  width=15, command=self.pAnalisis).place(x=145, y=0)
        Button(self.vMain, text="Tokens", font=("Arial", 12),  width=15, command=self.pTokens).place(x=290, y=0)
        Button(self.vMain, text="Errores", font=("Arial", 12),  width=15, command=self.pErrores).place(x=435, y=0)

        Label(self.vMain, bg="#2d98da").place(x=25, y=50) #bg="#2d98da"
        
        txt_data = Text(self.vMain, width=66, height=19, name="txt_data")
        txt_data.place(x=25, y= 75)
    
    def pArchivo():
        pass

    def pAnalisis():
        pass

    def pTokens():
        pass

    def pErrores():
        pass

r = Pantalla_Principal()