
from tkinter import messagebox, ttk
from conector import Conector
import tkinter as tk

def selection_changed():
    selection = combo.get()
    if(selection!=""):
        
        try:
            f=open("conf.txt","w") 
            f.write(selection)
            f.close()
            messagebox.showinfo(
                title="Elemento seleccionado",
                message=selection+" configurado correctamente"
            )
        except:
            messagebox.showinfo(
                title="Error",
                message="Error al tratar de guardar los datos"
            )
    else:
        messagebox.showwarning(
            title="Elemento seleccionado",
            message="Ningún elemento seleccionado"
        )

main_window = tk.Tk()
main_window.config(width=300, height=200)
main_window.title("Configuracion de impresora")

impresoras = Conector.obtenerImpresoras()

combo = ttk.Combobox(values=impresoras)
combo.place(x=50, y=50)

btnSave = ttk.Button(text="Guardar configuracion", command=selection_changed)
btnSave.place(x=50,y=80)

btnExit = ttk.Button(text="Salir", command=main_window.destroy)
btnExit.place(x=50,y=120)

main_window.mainloop()