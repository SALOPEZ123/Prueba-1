import tkinter as tk
from view.view_ventana1 import *

ventana = tk.Tk()
ventana.title("Mi tienda")
ventana.geometry("1000x600")



cargar_login(ventana)

ventana.mainloop()