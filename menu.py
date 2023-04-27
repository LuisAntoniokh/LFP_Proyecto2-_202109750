import os
from tkinter import *
from tkinter import filedialog, messagebox

class Pantalla_Principal():
    def __init__(self):
        self.filename = None
        self.vMain = Tk()
        self.vMain.title("Proyecto #2 - 202109750 - Luis Castro")
        self.vMain.geometry("580x400")
        self.vMain.config(bg = "#2d98da")
        self.vMain.resizable(False, False)
        self.p1()
        self.vMain.mainloop()
    
    def p1(self):
        self.Texto = ""

        Button(self.vMain, text="Archivo", font=("Arial", 12),  width=15, command=self.panArch).place(x=0, y=0)
        Button(self.vMain, text="Análisis", font=("Arial", 12),  width=15, command=self.pAnalisis).place(x=145, y=0)
        Button(self.vMain, text="Tokens", font=("Arial", 12),  width=15, command=self.pTokens).place(x=290, y=0)
        Button(self.vMain, text="Errores", font=("Arial", 12),  width=15, command=self.pErrores).place(x=435, y=0)

        lbNomArch = Label(self.vMain, bg="#2d98da", name="lbNombre", fg="White") #bg="#2d98da"
        lbNomArch.place(x=25, y=50)

        txt_data = Text(self.vMain, width=66, height=19, name="txt_data")
        txt_data.place(x=25, y= 75)
    
    def panArch(self):
        self.vArch = Toplevel(self.vMain)
        self.vArch.geometry("250x250")
        self.vArch.resizable(False, False)
        self.vArch.config(bg = "#686de0")
        Button(self.vArch, text="Nuevo", font=("Arial", 12),  width=15, borderwidth=5, command=self.btnNuevo).pack(pady=5)
        Button(self.vArch, text="Abrir", font=("Arial", 12),  width=15, borderwidth=5, command=self.abrirArchivo).pack(pady=5)
        Button(self.vArch, text="Guardar", font=("Arial", 12),  width=15, borderwidth=5, command=self.guardar).pack(pady=5)
        Button(self.vArch, text="Guardar como", font=("Arial", 12),  width=15, borderwidth=5, command=self.guardarComo).pack(pady=5)
        Button(self.vArch, text="Salir", font=("Arial", 12),  width=15, borderwidth=5, command=self.vMain.destroy).pack(pady=5)
        self.vArch.mainloop()

    def abrirArchivo(self):
        x = ""
        Tk().withdraw()
        try:
            filename = filedialog.askopenfilename(title="Selecciona un documento")
            with open(filename) as infile:
                x = infile.read()
                self.filename = filename
                lbNomArch = self.vMain.nametowidget("lbNombre")
                lbNomArch.config(text=os.path.basename(filename))
        except Exception as e:
            print(e)
            return
        
        self.Texto = x.strip()
        #print(self.Texto)

        self.txt_data = self.vMain.nametowidget("txt_data")
        self.txt_data.delete(1.0, END)
        self.txt_data.insert(END, self.Texto)
        
    def guardarComo(self):
        n_arch = filedialog.asksaveasfile(title="Guardar archivo como", filetypes=[("Text files", "*.txt")])
        if n_arch:
            txt_data = self.vMain.nametowidget("txt_data")
            n_arch.write(txt_data.get('1.0', 'end-1c')) 
            n_arch.close()
            
    def guardar(self):
        if self.filename:
            cont = self.vMain.nametowidget("txt_data").get('1.0', END)
            with open(self.filename, 'w') as outfile:
                outfile.write(cont)
        else:
            print("error")

    def btnNuevo(self):
        if self.filename:
            respuesta = messagebox.askyesnocancel(title="Guardar cambios", message="¿Desea guardar los cambios antes de limpiar el editor?")
            if respuesta == True:
                self.guardarComo()
                self.filename = None
                lbNomArch = self.vMain.nametowidget("lbNombre")
                lbNomArch.config(text="")
            elif respuesta == False:
                self.filename = None
            else: 
                return
            
        else:
            messagebox.showinfo(title="Información", message="No hay ningún archivo seleccionado, seleccione uno")

        txt_data = self.vMain.nametowidget("txt_data")
        txt_data.delete(1.0, END)
        
    def pAnalisis():
        pass

    def pTokens():
        pass

    def pErrores():
        pass

r = Pantalla_Principal()
