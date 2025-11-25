import tkinter as tk

# --- Funciones de la Lógica ---

def click(numero):
    # Esta función toma lo que ya hay en la pantalla y le agrega el nuevo número que presione.
    actual = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(0, actual + str(numero))

def operar(op):
    # Aquí uso variables globales para "recordar" el primer número y el signo
    # mientras el usuario escribe el segundo número.
    global operacion, num1
    try:
        num1 = float(entrada.get())
        operacion = op
        entrada.delete(0, tk.END) # Limpio la pantalla para el siguiente número
    except ValueError:
        entrada.delete(0, tk.END)

def calcular():
    # Esta función se activa con el "=". Hace la matemática final.
    try:
        num2 = float(entrada.get()) # Tomo el segundo número de la pantalla
        entrada.delete(0, tk.END)
        
        # Uso if/elif en lugar de eval() porque es más seguro y controlado
        if operacion == "+":
            entrada.insert(0, num1 + num2)
        elif operacion == "-":
            entrada.insert(0, num1 - num2)
        elif operacion == "*":
            entrada.insert(0, num1 * num2)
        elif operacion == "/":
            if num2 == 0:
                entrada.insert(0, "Error") # Evito que el programa explote si dividen por 0
            else:
                entrada.insert(0, num1 / num2)
    except:
        entrada.delete(0, tk.END)

def limpiar():
    # Botón C: borra todo
    entrada.delete(0, tk.END)

def validar_input(texto):
    # Esto es para que el usuario no pueda escribir letras en la caja, solo números.
    return texto.isdigit() or texto == "" or texto == "."

# --- Configuración de la Ventana (GUI) ---

ventana = tk.Tk()
ventana.title("Calculadora By Daniel")
ventana.attributes('-fullscreen', True) # Se ve genial en pantalla completa
ventana.rowconfigure(tuple(range(6)), weight=1)
ventana.columnconfigure(tuple(range(4)), weight=1)

vcmd = (ventana.register(validar_input), "%P")

entrada = tk.Entry(ventana, font=("Arial", 30), validate="key", validatecommand=vcmd, justify="right")
entrada.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)

# Lista de botones para crearlos con un bucle (ahorra escribir mucho código)
botones = [
    ("1", 1, 0), ("2", 1, 1), ("3", 1, 2), ("+", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("-", 2, 3),
    ("7", 3, 0), ("8", 3, 1), ("9", 3, 2), ("*", 3, 3),
    ("C", 4, 0), ("0", 4, 1), ("=", 4, 2), ("/", 4, 3)
]

for texto, fila, columna in botones:
    if texto.isdigit() or texto == ".":
        cmd = lambda t=texto: click(t)
    elif texto == "=":
        cmd = calcular
    elif texto == "C":
        cmd = limpiar
    else:
        cmd = lambda t=texto: operar(t)
    # Creo el botón y lo acomodo en la rejilla
    tk.Button(ventana, text=texto, font=("Arial", 30), command=cmd).grid(row=fila, column=columna, sticky="nsew", padx=5, pady=5)

# Tecla de escape para salir rápido de la pantalla completa
ventana.bind("<Escape>", lambda e: ventana.destroy())

ventana.mainloop()