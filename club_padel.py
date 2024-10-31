import tkinter as tk   
from tkinter import ttk
import mysql.connector

# Conexión a la base de datos
cnx = mysql.connector.connect(host="localhost",
                            user="root",
                            password="1234",
                            database="clubpadel",
                            port="3307")
cursor = cnx.cursor()

# Función para agregar un socio
def agregar_socio():
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    telefono = entry_telefono.get()
    email = entry_email.get()
    cursor.execute("INSERT INTO socios (nombre, apellido, telefono, email) VALUES (%s, %s, %s, %s)", (nombre, apellido, telefono, email))
    cnx.commit()
    limpiar_campos()

# Función para agregar un horario
def agregar_horario():
    id_socio = combo_socios.get()
    fecha = entry_fecha.get()
    hora_inicio = entry_hora_inicio.get()
    hora_fin = entry_hora_fin.get()
    cancha = entry_cancha.get()
    cursor.execute("INSERT INTO horarios (id_socio, fecha, hora_inicio, hora_fin, id_canchas) VALUES (%s, %s, %s, %s, %s)", (id_socio, fecha, hora_inicio, hora_fin, cancha))
    cnx.commit()
    limpiar_campos()

# Función para editar un socio
def editar_socio():
    id_socio = entry_id_socio_editar.get()
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    telefono = entry_telefono.get()
    email = entry_email.get()
    cursor.execute("UPDATE socios SET nombre = %s, apellido = %s, telefono = %s, email = %s WHERE id_socio = %s", 
                (nombre, apellido, telefono, email, id_socio))
    cnx.commit()
    limpiar_campos()

# Función para editar un horario
def editar_horario():
    id_horario = entry_id_horario_editar.get()
    id_socio = combo_socios.get()
    fecha = entry_fecha.get()
    hora_inicio = entry_hora_inicio.get()
    hora_fin = entry_hora_fin.get()
    id_canchas = entry_cancha.get()
    cursor.execute("UPDATE horarios SET id_socio = %s, fecha = %s, hora_inicio = %s, hora_fin = %s, id_canchas = %s WHERE id_horario = %s", 
                (id_socio, fecha, hora_inicio, hora_fin, id_canchas, id_horario))
    cnx.commit()
    limpiar_campos()

# Función para mostrar socios
def mostrar_socios():
    cursor.execute("SELECT * FROM socios")
    resultados = cursor.fetchall()
    texto_resultados.delete(1.0, tk.END)
    for resultado in resultados:
        texto_resultados.insert(tk.END, f"ID: {resultado[0]} - Nombre: {resultado[1]} {resultado[2]} - Teléfono: {resultado[3]} - Email: {resultado[4]}\n")

# Función para mostrar horarios
def mostrar_horarios():
    cursor.execute("""
        SELECT horarios.id_horario, socios.nombre, socios.apellido, horarios.fecha, 
        horarios.hora_inicio, horarios.hora_fin, horarios.id_canchas 
        FROM horarios 
        JOIN socios ON horarios.id_socio = socios.id_socio
    """)
    resultados = cursor.fetchall()
    texto_resultados.delete(1.0, tk.END)
    for resultado in resultados:
        texto_resultados.insert(tk.END, f"ID:{resultado[0]}-Socio:{resultado[1]} {resultado[2]} - Fecha: {resultado[3]} - Hora inicio: {resultado[4]} - Hora fin: {resultado[5]} - Cancha: {resultado[6]}\n")

# Función para mostrar canchas
def mostrar_canchas():
    cursor.execute("SELECT * FROM canchas")
    resultados = cursor.fetchall()
    texto_resultados.delete(1.0, tk.END)
    for resultado in resultados:
        texto_resultados.insert(tk.END, f"ID Cancha: {resultado[0]} - : {resultado[1]} - Estado: {resultado[2]}\n")

# Función para eliminar un socio
def eliminar_socio():
    id_socio = entry_id_socio_eliminar.get()
    cursor.execute("DELETE FROM socios WHERE id_socio = %s", (id_socio,))
    cnx.commit()
    limpiar_campos()

# Función para eliminar un horario
def eliminar_horario():
    id_horario = entry_id_horario_eliminar.get()
    cursor.execute("DELETE FROM horarios WHERE id_horario = %s", (id_horario,))
    cnx.commit()
    limpiar_campos()

# Función para limpiar campos
def limpiar_campos():
    entry_nombre.delete(0, tk.END)
    entry_apellido.delete(0, tk.END)
    entry_telefono.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_fecha.delete(0, tk.END)
    entry_hora_inicio.delete(0, tk.END)
    entry_hora_fin.delete(0, tk.END)
    entry_cancha.delete(0, tk.END)
    entry_id_socio_editar.delete(0, tk.END)
    entry_id_horario_editar.delete(0, tk.END)
    entry_id_socio_eliminar.delete(0, tk.END)
    entry_id_horario_eliminar.delete(0, tk.END)

# Ventana principal
ventana = tk.Tk()
ventana.title("Club de Pádel")
ventana.geometry("900x700")  # Ajustar tamaño de la ventana

# Título
label_titulo = tk.Label(ventana, text="Club de Pádel", font=("Arial", 24))
label_titulo.grid(column=0, row=0, columnspan=2)

espacio = tk.Label(ventana, text=" ", font=("Arial", 12))
espacio.grid(column=0, row=3)

# Frame para agregar o editar socios
frame_socios = tk.Frame(ventana)
frame_socios.grid(column=0, row=1)

label_nombre = tk.Label(frame_socios, text="Nombre:", font=("Arial", 12))
label_nombre.grid(column=0, row=0)
entry_nombre = tk.Entry(frame_socios, width=30, font=("Arial", 12))
entry_nombre.grid(column=1, row=0)

label_apellido = tk.Label(frame_socios, text="Apellido:", font=("Arial", 12))
label_apellido.grid(column=0, row=1)
entry_apellido = tk.Entry(frame_socios, width=30, font=("Arial", 12))
entry_apellido.grid(column=1, row=1)

label_telefono = tk.Label(frame_socios, text="Teléfono:", font=("Arial", 12))
label_telefono.grid(column=0, row=2)
entry_telefono = tk.Entry(frame_socios, width=30, font=("Arial", 12))
entry_telefono.grid(column=1, row=2)

label_email = tk.Label(frame_socios, text="Email:", font=("Arial", 12))
label_email.grid(column=0, row=3)
entry_email = tk.Entry(frame_socios, width=30, font=("Arial", 12))
entry_email.grid(column=1, row=3)

boton_agregar_socio = tk.Button(frame_socios, text="Agregar Socio", command=agregar_socio, bg='blue', fg='white', font=("Arial", 12, "bold"))
boton_agregar_socio.grid(column=1, row=4)

label_id_socio_editar = tk.Label(frame_socios, text="ID Socio a editar:", font=("Arial", 12))
label_id_socio_editar.grid(column=0, row=5)
entry_id_socio_editar = tk.Entry(frame_socios, width=30, font=("Arial", 12))
entry_id_socio_editar.grid(column=1, row=5)

boton_editar_socio = tk.Button(frame_socios, text="Editar Socio", command=editar_socio, bg='blue', fg='white', font=("Arial", 12, "bold"))
boton_editar_socio.grid(column=1, row=6)

# Frame para agregar o editar horarios
frame_horarios = tk.Frame(ventana)
frame_horarios.grid(column=1, row=1)

label_id_socio = tk.Label(frame_horarios, text="ID Socio:", font=("Arial", 12))
label_id_socio.grid(column=0, row=0)
combo_socios = tk.Entry(frame_horarios, width=30, font=("Arial",12))
combo_socios.grid(column=1, row=0)

label_fecha = tk.Label(frame_horarios, text="Fecha (AÑO-MES-DIA):", font=("Arial", 12))
label_fecha.grid(column=0, row=1)
entry_fecha = tk.Entry(frame_horarios, width=30, font=("Arial", 12))
entry_fecha.grid(column=1, row=1)

label_hora_inicio = tk.Label(frame_horarios, text="Hora Inicio:", font=("Arial", 12))
label_hora_inicio.grid(column=0, row=2)
entry_hora_inicio = tk.Entry(frame_horarios, width=30, font=("Arial", 12))
entry_hora_inicio.grid(column=1, row=2)

label_hora_fin = tk.Label(frame_horarios, text="Hora Fin:", font=("Arial", 12))
label_hora_fin.grid(column=0, row=3)
entry_hora_fin = tk.Entry(frame_horarios, width=30, font=("Arial", 12))
entry_hora_fin.grid(column=1, row=3)

label_cancha = tk.Label(frame_horarios, text="ID Cancha:", font=("Arial", 12))
label_cancha.grid(column=0, row=4)
entry_cancha = tk.Entry(frame_horarios, width=30, font=("Arial", 12))
entry_cancha.grid(column=1, row=4)

boton_agregar_horario = tk.Button(frame_horarios, text="Agregar Horario", command=agregar_horario, bg='blue', fg='white', font=("Arial", 12, "bold"))
boton_agregar_horario.grid(column=1, row=5)

label_id_horario_editar = tk.Label(frame_horarios, text="ID Horario a editar:", font=("Arial", 12))
label_id_horario_editar.grid(column=0, row=6)
entry_id_horario_editar = tk.Entry(frame_horarios, width=30, font=("Arial", 12))
entry_id_horario_editar.grid(column=1, row=6)

boton_editar_horario = tk.Button(frame_horarios, text="Editar Horario", command=editar_horario, bg='blue', fg='white', font=("Arial", 12, "bold"))
boton_editar_horario.grid(column=1, row=7)

espacio1 = tk.Label(frame_horarios, text=" ", font=("Arial", 12))
espacio1.grid(column=0, row=8)

# Frame para eliminar socios y horarios
frame_eliminar = tk.Frame(ventana)
frame_eliminar.grid(column=0, row=2, columnspan=2)

label_id_socio_eliminar = tk.Label(frame_eliminar, text="ID Socio a eliminar:", font=("Arial", 12))
label_id_socio_eliminar.grid(column=0, row=0)
entry_id_socio_eliminar = tk.Entry(frame_eliminar, width=30, font=("Arial", 12))
entry_id_socio_eliminar.grid(column=1, row=0)

boton_eliminar_socio = tk.Button(frame_eliminar, text="Eliminar Socio", command=eliminar_socio, bg='red', fg='white', font=("Arial", 12, "bold"))
boton_eliminar_socio.grid(column=1, row=1)

label_id_horario_eliminar = tk.Label(frame_eliminar, text="ID Horario a eliminar:", font=("Arial", 12))
label_id_horario_eliminar.grid(column=0, row=2)
entry_id_horario_eliminar = tk.Entry(frame_eliminar, width=30, font=("Arial", 12))
entry_id_horario_eliminar.grid(column=1, row=2)

boton_eliminar_horario = tk.Button(frame_eliminar, text="Eliminar Horario", command=eliminar_horario, bg='red', fg='white', font=("Arial", 12, "bold"))
boton_eliminar_horario.grid(column=1, row=3)
espacio2 = tk.Label(frame_eliminar, text=" ", font=("Arial", 12))
espacio2.grid(column=0, row=4)

# Frame para mostrar resultados
frame_resultados = tk.Frame(ventana)
frame_resultados.grid(column=0, row=3, columnspan=2)

texto_resultados = tk.Text(frame_resultados, height=10, width=80, font=("Arial", 12))
texto_resultados.grid(column=0, row=0, columnspan=3)

boton_mostrar_socios = tk.Button(frame_resultados, text="Mostrar Socios", command=mostrar_socios, bg='green', fg='white', font=("Arial", 12, "bold"))
boton_mostrar_socios.grid(column=0, row=1)

boton_mostrar_horarios = tk.Button(frame_resultados, text="Mostrar Horarios", command=mostrar_horarios, bg='green', fg='white', font=("Arial", 12, "bold"))
boton_mostrar_horarios.grid(column=1, row=1)

boton_mostrar_canchas = tk.Button(frame_resultados, text="Mostrar Canchas", command=mostrar_canchas, bg='green', fg='white', font=("Arial", 12, "bold"))
boton_mostrar_canchas.grid(column=2, row=1)

ventana.mainloop()

# Cerrar cursor y conexión
cursor.close()
cnx.close()