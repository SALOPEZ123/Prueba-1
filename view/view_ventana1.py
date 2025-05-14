import tkinter as tk

from service.mi_sql import conectar

def cargar_login(ventana):
    login_panel = tk.Frame(ventana,
    bg="white",
    padx=0,
    pady=0,
    width=1000,
    height=600,
    )

    titulo = tk.Label(login_panel, text="Filtrar datos")
    titulo.pack()

    entrada_correo = tk.Entry(login_panel)
    entrada_correo.pack()

    def btm_continuar():    
        Et_Corro = entrada_correo.get()
        print(conectar(f"""SELECT * FROM usuario WHERE nombre = '{Et_Corro}'"""))


    boton = tk.Button(login_panel, text="Consultar",command=btm_continuar)
    boton.pack()


    login_panel.pack()
    print("panel login cargado")
