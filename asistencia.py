import tkinter as tk

def calcularestado():
    total = int(entradatotal.get())
    faltas = int(entradafaltas.get())
    justificadas = int(entradajustificadas.get())

    asistencia = ((total - faltas) / total) * 100
    mensaje = "Recursa"

    if asistencia >= 81:
        mensaje = "Tiene acceso al examen final"

    if asistencia >= 70:
        if asistencia <= 80:
            porcentajejustificadas = (justificadas / faltas) * 100
            if porcentajejustificadas >= 30:
                mensaje = "Tiene acceso al examen final"

    resultado.config(text=mensaje)
ventana = tk.Tk()
ventana.title("Estado del Estudiante")
ventana.geometry("300x300")
tk.Label(ventana, text="Total de clases:").pack()
entradatotal = tk.Entry(ventana)
entradatotal.pack()
tk.Label(ventana, text="Cantidad de faltas:").pack()
entradafaltas = tk.Entry(ventana)
entradafaltas.pack()
tk.Label(ventana, text="Faltas justificadas:").pack()
entradajustificadas = tk.Entry(ventana)
entradajustificadas.pack()
resultado = tk.Label(ventana, text="", fg="blue")
resultado.pack(pady=10)

tk.Button(ventana, text="Evaluar", command=calcularestado).pack()

ventana.mainloop()

