import sqlite3
from tkinter import *
from tkinter import messagebox

# ------------------ BBDD ------------------
def conexion_bbdd():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()
    try:
        miCursor.execute('''
            CREATE TABLE USUARIOS (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NOMBRE VARCHAR(50),
                PASSWORD VARCHAR(50),
                APELLIDO VARCHAR(50),
                DIRECCION VARCHAR(100),
                COMENTARIOS TEXT
            )
        ''')
        messagebox.showinfo("BBDD", "BBDD creada con éxito")
    except:
        messagebox.showwarning("¡Atención!", "La BBDD ya existe")

def salir_aplicacion():
    valor = messagebox.askquestion("Salir", "¿Deseas salir de la aplicación?")
    if valor == "yes":
        root.destroy()

def limpiar_campos():
    miId.set("")
    miNombre.set("")
    miPass.set("")
    miApellido.set("")
    miDireccion.set("")
    cuadroComentarios.delete(1.0, END)

# ------------------ CRUD ------------------
def crear():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()
    datos = (miNombre.get(), miPass.get(), miApellido.get(),
             miDireccion.get(), cuadroComentarios.get("1.0", END))
    miCursor.execute("INSERT INTO USUARIOS VALUES(NULL,?,?,?,?,?)", datos)
    miConexion.commit()
    messagebox.showinfo("BBDD", "Registro insertado con éxito")
    limpiar_campos() 

def leer():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()
    miCursor.execute("SELECT * FROM USUARIOS WHERE ID=" + miId.get())
    elUsuario = miCursor.fetchall()

    for usuario in elUsuario:
        miId.set(usuario[0])
        miNombre.set(usuario[1])
        miPass.set(usuario[2])
        miApellido.set(usuario[3])
        miDireccion.set(usuario[4])
        cuadroComentarios.delete(1.0, END)
        cuadroComentarios.insert(1.0, usuario[5])

    miConexion.commit()

def actualizar():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()
    datos = (miNombre.get(), miPass.get(), miApellido.get(),
             miDireccion.get(), cuadroComentarios.get("1.0", END), miId.get())
    miCursor.execute("UPDATE USUARIOS SET NOMBRE=?, PASSWORD=?, APELLIDO=?, DIRECCION=?, COMENTARIOS=? WHERE ID=?", datos)
    miConexion.commit()
    messagebox.showinfo("BBDD", "Registro actualizado con éxito")
    limpiar_campos() 

def eliminar():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()
    miCursor.execute("DELETE FROM USUARIOS WHERE ID=" + miId.get())
    miConexion.commit()
    messagebox.showinfo("BBDD", "Registro eliminado con éxito")
    limpiar_campos()

# ------------------ INTERFAZ ------------------
root = Tk()
root.title("Gestión de Usuarios")
root.config(bg="#1E1E1E")
root.iconbitmap("logo.ico")


# ------------------- Variables ----------------
miId = StringVar()
miNombre = StringVar()
miPass = StringVar()
miApellido = StringVar()
miDireccion = StringVar()

# Menú
barraMenu = Menu(root)
root.config(menu=barraMenu, width=300, height=300)

bbddMenu = Menu(barraMenu, tearoff=0, bg="#1E1E1E", fg="#00ADB5")
bbddMenu.add_command(label="Conectar", command=conexion_bbdd)
bbddMenu.add_command(label="Salir", command=salir_aplicacion)

borrarMenu = Menu(barraMenu, tearoff=0, bg="#1E1E1E", fg="#00ADB5")
borrarMenu.add_command(label="Limpiar Campos", command=limpiar_campos)

crudMenu = Menu(barraMenu, tearoff=0, bg="#1E1E1E", fg="#00ADB5")
crudMenu.add_command(label="Crear", command=crear)
crudMenu.add_command(label="Leer", command=leer)
crudMenu.add_command(label="Actualizar", command=actualizar)
crudMenu.add_command(label="Eliminar", command=eliminar)

ayudaMenu = Menu(barraMenu, tearoff=0, bg="#1E1E1E", fg="#00ADB5")
ayudaMenu.add_command(label="Acerca de...", command=lambda: messagebox.showinfo("Ayuda", "Aplicación CRUD con Tkinter y SQLite"))

barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

# ------------------- Campos ---------------------
frameCampos = Frame(root, bg="#1E1E1E")
frameCampos.pack()

Label(frameCampos, text="ID:", bg="#1E1E1E", fg="#00ADB5", 
      font=("Arial", 10, "bold")).grid(row=0, column=0, sticky="e")
Entry(frameCampos, textvariable=miId,  bg="#1E1E1E", fg="white", insertbackground="#32CD32").grid(row=0, column=1, padx=10, pady=5)

Label(frameCampos, text="Nombre:", bg="#1E1E1E", fg="#00ADB5", 
      font=("Arial", 10, "bold")).grid(row=1, column=0, sticky="e")
Entry(frameCampos, textvariable=miNombre, bg="#1E1E1E", fg="white", insertbackground="#32CD32").grid(row=1, column=1, padx=10, pady=5)

Label(frameCampos, text="Password:", bg="#1E1E1E", fg="#00ADB5", 
      font=("Arial", 10, "bold")).grid(row=2, column=0, sticky="e")
Entry(frameCampos, textvariable=miPass, show="*", bg="#1E1E1E", fg="white", insertbackground="#32CD32").grid(row=2, column=1, padx=10, pady=5)

Label(frameCampos, text="Apellido:", bg="#1E1E1E", fg="#00ADB5", 
      font=("Arial", 10, "bold")).grid(row=3, column=0, sticky="e")
Entry(frameCampos, textvariable=miApellido, bg="#1E1E1E", fg="white", insertbackground="#32CD32").grid(row=3, column=1, padx=10, pady=5)

Label(frameCampos, text="Dirección:", bg="#1E1E1E", fg="#00ADB5", 
      font=("Arial", 10, "bold")).grid(row=4, column=0, sticky="e")
Entry(frameCampos, textvariable=miDireccion, bg="#1E1E1E", fg="white", insertbackground="#32CD32").grid(row=4, column=1, padx=10, pady=5)

Label(frameCampos, text="Comentarios:", bg="#1E1E1E", fg="#00ADB5", 
      font=("Arial", 10, "bold")).grid(row=5, column=0, sticky="ne")
cuadroComentarios = Text(frameCampos, width=20, height=5,  bg="#1E1E1E", fg="white", insertbackground="#32CD32")
cuadroComentarios.grid(row=5, column=1, padx=10, pady=5)
scrollVert = Scrollbar(frameCampos, command=cuadroComentarios.yview)
scrollVert.grid(row=5, column=2, sticky="nsew")
cuadroComentarios.config(yscrollcommand=scrollVert.set)

# -------------------- Botones -----------------------
frameBotones = Frame(root, bg="#1E1E1E")
frameBotones.pack()

Button(frameBotones, text="Create", command=crear, bg="#1E1E1E", fg="#00ADB5").grid(row=0, column=0, padx=10, pady=10)
Button(frameBotones, text="Read", command=leer,  bg="#1E1E1E", fg="#00ADB5").grid(row=0, column=1, padx=10, pady=10)
Button(frameBotones, text="Update", command=actualizar,  bg="#1E1E1E", fg="#00ADB5").grid(row=0, column=2, padx=10, pady=10)
Button(frameBotones, text="Delete", command=eliminar,  bg="#1E1E1E", fg="#00ADB5").grid(row=0, column=3, padx=10, pady=10)

root.mainloop()
