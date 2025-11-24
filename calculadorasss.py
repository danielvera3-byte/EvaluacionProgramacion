import tkinter as tk

# Inicialización obligatoria de las variables globales.
# Estas variables son esenciales para guardar el primer número (num1) 
# y el operador (operacion) mientras el usuario ingresa el segundo número.
global operacion, num1
operacion = "" 
num1 = 0 

def click(numero):
    """
    Función que se llama al presionar un botón numérico (0-9) o el punto.
    
    Toma el texto actual en la pantalla, lo limpia, y añade el nuevo dígito. 
    Así se construye el número que el usuario quiere ingresar.
    """
    actual = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(0, actual + str(numero))

def operar(op):
    """
    Función que se activa cuando se presiona un operador (+, -, *, /).
    
    Guarda el número que el usuario escribió (num1) y el operador. 
    Luego, limpia la pantalla para que el usuario pueda ingresar el segundo número.
    """
    global operacion, num1
    try:
        num1 = float(entrada.get()) # Convertimos el texto de la pantalla a un número decimal
        operacion = op
        entrada.delete(0, tk.END)
    except ValueError:
        # Si el usuario no ingresó un número, limpiamos la pantalla.
        entrada.delete(0, tk.END)

def calcular():
    """
    Función principal, se llama al presionar el botón de igualdad (=).
    
    Toma el segundo número, revisa qué operador está guardado y 
    hace el cálculo con las estructuras 'if/elif' para evitar usar 'eval()'.
    """
    try:
        num2 = float(entrada.get())
        entrada.delete(0, tk.END)
        
        # Revisa el operador guardado y ejecuta la operación correspondiente
        if operacion == "+":
            entrada.insert(0, num1 + num2)
        elif operacion == "-":
            entrada.insert(0, num1 - num2)
        elif operacion == "*":
            entrada.insert(0, num1 * num2)
        elif operacion == "/":
            # Controlamos la división por cero, que causaría un error en Python.
            if num2 == 0:
                entrada.insert(0, "Error")
            else:
                entrada.insert(0, num1 / num2)
    except:
        # Manejo de error genérico para evitar que el programa se cierre
        entrada.delete(0, tk.END)

def limpiar():
    """
    Borra completamente la pantalla (botón C).
    """
    entrada.delete(0, tk.END)

def validar_input(texto):
    """
    Esta es una función de seguridad que limita lo que el usuario 
    puede escribir directamente. Solo permite números y el punto decimal.
    """
    # Devuelve True si es un dígito, está vacío o es el punto.
    return texto.isdigit() or texto == "" or texto == "."

# --- CONFIGURACIÓN DE LA INTERFAZ DE TKINTER ---
ventana = tk.Tk()
ventana.title("Calculadora By Daniel")
# Este es un detalle estético para que se vea más profesional en el PC.
ventana.attributes('-fullscreen', True) 

# Configuración de la geometría: asegura que las filas y columnas 
# se expandan al mismo tamaño para que los botones se vean bien.
ventana.rowconfigure(tuple(range(6)), weight=1)
ventana.columnconfigure(tuple(range(4)), weight=1)

# Registro el comando de validación para usarlo en la casilla de entrada
vcmd = (ventana.register(validar_input), "%P")

# Casilla de entrada (la "pantalla" de la calculadora)
entrada = tk.Entry(ventana, font=("Arial", 30), validate="key", validatecommand=vcmd, justify="right")
entrada.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)

# Lista de botones con su texto, fila y columna para usar el layout 'grid'
botones = [
    ("1", 1, 0), ("2", 1, 1), ("3", 1, 2), ("+", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("-", 2, 3),
    ("7", 3, 0), ("8", 3, 1), ("9", 3, 2), ("*", 3, 3),
    ("C", 4, 0), ("0", 4, 1), ("=", 4, 2), ("/", 4, 3)
]

# Creamos los botones usando un bucle 'for' para ahorrar código
for texto, fila, columna in botones:
    # Determinamos qué función llamar al presionar cada botón
    if texto.isdigit() or texto == ".":
        cmd = lambda t=texto: click(t)
    elif texto == "=":
        cmd = calcular
    elif texto == "C":
        cmd = limpiar
    else: # Operadores
        cmd = lambda t=texto: operar(t)
        
    # Colocamos el botón en la cuadrícula (grid)
    tk.Button(ventana, text=texto, font=("Arial", 30), command=cmd).grid(row=fila, column=columna, sticky="nsew", padx=5, pady=5)

# Enlazar la tecla ESC para salir si está en pantalla completa
ventana.bind("<Escape>", lambda e: ventana.destroy())

ventana.mainloop()