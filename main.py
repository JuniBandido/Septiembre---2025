import tkinter as tk

ventana = tk.Tk()
ventana.title("calculadora")
ventana.geometry("300x400")

etiqueta = tk.Label(ventana, text="Escribe el primer numero:")
etiqueta.pack(pady=5)

entrada = tk.Entry(ventana)
entrada.pack(pady=5)

etiqueta2 = tk.Label(ventana, text="Escribe el segundo numero:")
etiqueta2.pack(pady=5)

entrada2 = tk.Entry(ventana)
entrada2.pack(pady=5)

def sumar():
    a = int(entrada.get())
    b = int(entrada2.get())
    etiqueta.config(text=f"Respuesta = {a + b}")

def restar():
    a = int(entrada.get())
    b = int(entrada2.get())
    etiqueta.config(text=f"Respuesta = {a - b}")

def multiplicar():
    a = int(entrada.get())
    b = int(entrada2.get())
    etiqueta.config(text=f"Respuesta = {a * b}")

def dividir():
    a = int(entrada.get())
    b = int(entrada2.get())
    etiqueta.config(text=f"Respuesta = {a / b}")

def limpiar():
    entrada.delete(0, tk.END)
    etiqueta.config(text="Escribe tu nombre:")

boton_sumar = tk.Button(ventana, text="Sumar", command=sumar, background="red", fg="black")
boton_sumar.pack(pady=5)

boton_restar = tk.Button(ventana, text="Restar", command=restar, background= "blue", fg="pink")
boton_restar.pack(pady=5)

boton_multiplicar = tk.Button(ventana, text="Multiplicar", command=multiplicar, background="pink")
boton_multiplicar.pack(pady=5)

boton_dividir = tk.Button(ventana, text="Dividir", command=dividir)
boton_dividir.pack(pady=5)

boton_salir = tk.Button(ventana, text="Salir", command=ventana.quit)
boton_salir.pack(pady=5)

ventana.mainloop()