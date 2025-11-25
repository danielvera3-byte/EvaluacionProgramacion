import tkinter as tk


global operacion, num1
operacion = "" 
num1 = 0 

def click(numero):
    
    actual = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(0, actual + str(numero))

def operar(op):

    global operacion, num1
    try:
        num1 = float(entrada.get()) 
        operacion = op
        entrada.delete(0, tk.END)
    except ValueError:
        
        entrada.delete(0, tk.END)

def calcular():
    
    try:
        num2 = float(entrada.get())
        entrada.delete(0, tk.END)
        
        
        if operacion == "+":
            entrada.insert(0, num1 + num2)
        elif operacion == "-":
            entrada.insert(0, num1 - num2)
        elif operacion == "*":
            entrada.insert(0, num1 * num2)
        elif operacion == "/":
            
            if num2 == 0:
                entrada.insert(0, "Error")
            else:
                entrada.insert(0, num1 / num2)
    except:
        entrada.delete(0, tk.END)

def limpiar():
    
    entrada.delete(0, tk.END)

def validar_input(texto):
    
    
    return texto.isdigit() or texto == "" or texto == "."


ventana = tk.Tk()
ventana.title("Calculadora By Daniel")

ventana.attributes('-fullscreen', True) 


ventana.rowconfigure(tuple(range(6)), weight=1)
ventana.columnconfigure(tuple(range(4)), weight=1)


vcmd = (ventana.register(validar_input), "%P")


entrada = tk.Entry(ventana, font=("Arial", 30), validate="key", validatecommand=vcmd, justify="right")
entrada.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)


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
        
    
    tk.Button(ventana, text=texto, font=("Arial", 30), command=cmd).grid(row=fila, column=columna, sticky="nsew", padx=5, pady=5)


ventana.bind("<Escape>", lambda e: ventana.destroy())

ventana.mainloop()