import tkinter as tk
from tkinter import ttk
import mysql.connector

# Configuración de la conexión a la base de datos
# Conexión a la base de datos
cnx=mysql.connector.connect(host="localhost",
                            user="root",
                            password="1234",
                            database="clubpadel",
                            port="3307")

# Cursor para ejecutar consultas
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
    cursor.execute("INSERT INTO horarios (id_socio, fecha, hora_inicio, hora_fin, cancha) VALUES (%s, %s, %s, %s, %s)", (id_socio, fecha, hora_inicio, hora_fin, cancha))
    cnx.commit()
    limpiar_campos()

# Función para mostrar socios
def mostrar_socios():
    cursor.execute("SELECT * FROM socios")
    resultados = cursor.fetchall()
    texto_resultados.delete(1.0, tk.END)
    for resultado in resultados:
        texto_resultados.insert(tk.END, f"ID: {resultado[0]} - Nombre: {resultado[1]} {resultado[2]}\n")

# Función para mostrar horarios
def mostrar_horarios():
    cursor.execute("SELECT * FROM horarios")
    resultados = cursor.fetchall()
    texto_resultados.delete(1.0, tk.END)
    for resultado in resultados:
        texto_resultados.insert(tk.END, f"ID: {resultado[0]} - Socio: {resultado[1]} - Fecha: {resultado[2]} - Hora inicio: {resultado[3]} - Hora fin: {resultado[4]} - Cancha: {resultado[5]}\n")

# Función para eliminar un socio
def eliminar_socio():
    id_socio = entry_id_socio.get()
    cursor.execute("DELETE FROM socios WHERE id_socio = %s", (id_socio,))
    cnx.commit()
    limpiar_campos()

# Función para eliminar un horario
def eliminar_horario():
    id_horario = entry_id_horario.get()
    cursor.execute("DELETE FROM horarios WHERE id_horario = %s", (id_horario,))
    cnx.commit()
    limpiar_campos()

# Ventana principal
root = tk.Tk()
root.title("Club de Pádel")

# Título
label_titulo = tk.Label(root, text="Club de Pádel", font=("Arial", 24))
label_titulo.grid(column=0, row=0, columnspan=2)

# Frame para agregar socios
frame_socios = tk.Frame(root)
frame_socios.grid(column=0, row=1)

label_nombre = tk.Label(frame_socios, text="Nombre:")
label_nombre.grid(column=0, row=0)
entry_nombre = tk.Entry(frame_socios)
entry_nombre.grid(column=1, row=0)

label_apellido = tk.Label(frame_socios, text="Apellido:")
label_apellido.grid(column=0, row=1)
entry_apellido = tk.Entry(frame_socios)
entry_apellido.grid(column=1, row=1)

label_telefono = tk.Label(frame_socios, text="Teléfono:")
label_telefono.grid(column=0, row=2)
entry_telefono = tk.Entry(frame_socios)
entry_telefono.grid(column=1, row=2)

label_email = tk.Label(frame_socios, text="Email:")
label_email.grid(column=0, row=3)
entry_email = tk.Entry(frame_socios)
entry_email.grid(column=1, row=3)

boton_agregar_socio = tk.Button(frame_socios, text="Agregar Socio", command=agregar_socio)
boton_agregar_socio.grid(column=1, row=4)

# Frame para agregar horarios
frame_horarios = tk.Frame(root)
frame_horarios.grid(column=1, row=1)

label_id_socio = tk.Label(frame_horarios, text="ID Socio:")
label_id_socio.grid(column=0, row=0)
combo_socios = ttk.Combobox(frame_horarios)
combo_socios.grid(column=1, row=0)

label_fecha = tk.Label(frame_horarios, text="Fecha:")
label_fecha.grid(column=0, row=1)
entry_fecha = tk.Entry(frame_horarios)
entry_fecha.grid(column=1, row=1)

label_hora_inicio = tk.Label(frame_horarios, text="Hora Inicio:")
label_hora_inicio.grid(column=0, row=2)
entry_hora_inicio = tk.Entry(frame_horarios)
entry_hora_inicio.grid(column=1, row=2)

label_hora_fin = tk.Label(frame_horarios, text="Hora Fin:")
label_hora_fin.grid(column=0, row=3)
entry_hora_fin = tk.Entry(frame_horarios)
entry_hora_fin.grid(column=1, row=3)

label_cancha = tk.Label(frame_horarios, text="Cancha:")
label_cancha.grid(column=0, row=4)
entry_cancha = tk.Entry(frame_horarios)
entry_cancha.grid(column=1, row=4)

boton_agregar_horario = tk.Button(frame_horarios, text="Agregar Horario", command=agregar_horario)
boton_agregar_horario.grid(column=1, row=5)

# Frame para mostrar resultados
frame_resultados = tk.Frame(root)
frame_resultados.grid(column=0, row=2, columnspan=2)

boton_mostrar_socios = tk.Button(frame_resultados, text="Mostrar Socios", command=mostrar_socios)
boton_mostrar_socios.grid(column=0, row=0)

boton_mostrar_horarios = tk.Button(frame_resultados, text="Mostrar Horarios", command=mostrar_horarios)
boton_mostrar_horarios.grid(column=1, row=0)

texto_resultados = tk.Text(frame_resultados)
texto_resultados.grid(column=0, row=1, columnspan=2)

# Frame para eliminar registros
frame_eliminar = tk.Frame(root)
frame_eliminar.grid(column=0, row=3, columnspan=2)

label_id_socio_eliminar = tk.Label(frame_eliminar, text="ID Socio a eliminar:")
label_id_socio_eliminar.grid(column=0, row=0)
entry_id_socio = tk.Entry(frame_eliminar)
entry_id_socio.grid(column=1, row=0)

boton_eliminar_socio = tk.Button(frame_eliminar, text="Eliminar Socio", command=eliminar_socio)
boton_eliminar_socio.grid(column=1, row=1)

label_id_horario_eliminar = tk.Label(frame_eliminar, text="ID Horario a eliminar:")
label_id_horario_eliminar.grid(column=0, row=2)
entry_id_horario = tk.Entry(frame_eliminar)
entry_id_horario.grid(column=1, row=2)

boton_eliminar_horario = tk.Button(frame_eliminar, text="Eliminar Horario", command=eliminar_horario)
boton_eliminar_horario.grid(column=1, row=3)

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
    entry_id_socio.delete(0, tk.END)
    entry_id_horario.delete(0, tk.END)

# Inicializar combobox de socios
cursor.execute("SELECT id_socio FROM socios")
socios = cursor.fetchall()
combo_socios['values'] = [socio[0] for socio in socios]

# Iniciar bucle principal
root.mainloop()

# Cerrar conexión a la base de datos
cnx.close()