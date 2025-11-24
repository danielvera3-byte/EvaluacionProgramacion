import tkinter as tk
from datetime import datetime, date, timedelta
import calendar
from tkinter import messagebox 

current_date = datetime.now()

day_buttons = [] 

start_date = None 

meses_es = ["", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
            "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

weekdays = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]


def actualizar_calendario():
    
    global start_date 
    
    year = current_date.year
    month = current_date.month
    
    label_month_year.config(text=f"{meses_es[month]} {year}")
    
    first_day_weekday, num_days_in_month = calendar.monthrange(year, month)
    
    current_day_num = 1
    for i in range(42): 
        btn = day_buttons[i] 
        
        btn.config(text="", state="disabled", bg="#F0F0F0", fg="black")
        
        if i >= first_day_weekday and current_day_num <= num_days_in_month:
            btn.config(text=str(current_day_num), state="normal", bg="white")
            
            if start_date is not None:
                current_day_obj = date(year, month, current_day_num)
                
                days_diff = (current_day_obj - start_date).days
                
                if (days_diff % 14) < 7:
                    btn.config(bg="green", fg="white") 
                else:
                    btn.config(bg="salmon", fg="black") 
            
            current_day_num += 1
            

def boton_generar_click():
    global start_date 
    
    date_str = entry_inicio.get() 
    try:
        start_date = datetime.strptime(date_str, "%d/%m/%Y").date()
    except ValueError:
        start_date = None 
        messagebox.showerror("Error", "Formato de fecha incorrecto.\nUsa DD/MM/AAAA")
    
    actualizar_calendario() 

def boton_prev_click():
    global current_date
    current_date = (current_date.replace(day=1) - timedelta(days=1))
    actualizar_calendario() 

def boton_next_click():
    global current_date
    days_in_month = calendar.monthrange(current_date.year, current_date.month)[1]
    current_date = (current_date.replace(day=1) + timedelta(days=days_in_month))
    actualizar_calendario() 


root = tk.Tk()
root.title("Planificador 7x7 By Daniel")

input_frame = tk.Frame(root) 
input_frame.pack(pady=10) 

label_inicio = tk.Label(input_frame, text="Inicio (DD/MM/AAAA):")
label_inicio.pack(side=tk.LEFT, padx=5)

entry_inicio = tk.Entry(input_frame, width=15)
entry_inicio.pack(side=tk.LEFT)

entry_inicio.insert(0, datetime.now().strftime("%d/%m/%Y"))

btn_generar = tk.Button(input_frame, text="Generar", command=boton_generar_click)
btn_generar.pack(side=tk.LEFT, padx=10)

nav_frame = tk.Frame(root)
nav_frame.pack()

btn_prev = tk.Button(nav_frame, text="<", command=boton_prev_click)
btn_prev.pack(side=tk.LEFT, padx=10)

label_month_year = tk.Label(nav_frame, text="", font=("Arial", 14, "bold"))
label_month_year.pack(side=tk.LEFT)

btn_next = tk.Button(nav_frame, text=">", command=boton_next_click)
btn_next.pack(side=tk.LEFT, padx=10)

calendar_frame = tk.Frame(root)
calendar_frame.pack(pady=10, padx=10)

for i in range(7): 
    label_dia = tk.Label(calendar_frame, text=weekdays[i], font=("Arial", 9, "bold"))
    label_dia.grid(row=0, column=i, padx=2, pady=2) 

for row in range(6):
    for col in range(7):
        btn = tk.Button(calendar_frame, text="", width=4, height=2, 
                        state="disabled", bg="#F0F0F0")
        btn.grid(row=row + 1, column=col, padx=2, pady=2)
        day_buttons.append(btn) 

actualizar_calendario() 
root.mainloop()