import tkinter as tk
from tkinter import ttk, messagebox

class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('600x700+650+200')
        self.resizable(0,0) # Para que no se pueda modificar el tamaño original
        self.title('Calculadora')
        self.configurar_ventana()
        self.definir_entrada()
        self.crear_botones()

    def configurar_ventana(self):
        for i in range(6):
            self.rowconfigure(i, weight=1)
        for i in range(4):
            self.columnconfigure(i, weight=1)
    def definir_entrada(self):
        self.entrada_var = tk.StringVar()
        self.entrada = tk.Entry(self, font=('arial', 20, 'bold'), width=30, justify=tk.RIGHT,
                                textvariable=self.entrada_var, bg='grey', bd=2, cursor='arrow')
        self.entrada.grid(column=0, row=0, sticky='NSWE', columnspan=4, padx=10, pady=10, ipadx=10)
    def funcion_igual(self):
        try:
            operacion = self.entrada.get()
            if self.validar_entrada(operacion):
                # resultado = float(sp.sympify(operacion).evalf())
                resultado = eval(operacion)
                self.entrada_var.set(resultado)
            else:
                self.entrada_var.set('')
        except ZeroDivisionError as e:
            messagebox.showerror('Error', f'Se trato de dividir entre cero')
            self.entrada_var.set('')
        except Exception as e:
            messagebox.showerror('Error', f'Expresion invalida')
            self.entrada_var.set('')
    def validar_entrada(self, operacion):
        caracteresValidos='0123456789+-*/.()'
        for caracter in operacion:
            if caracter not in caracteresValidos:
                return False
            else:
                return True
    def crear_botones(self):
        botones = [
            ('C', lambda: self.entrada.delete(0, tk.END), 0, 1, 3, '#ccc'),
            ('/', lambda: self.entrada.insert(tk.END, '/'), 3, 1, '#ccc'),
            ('7', lambda: self.entrada.insert(tk.END, '7'), 0, 2, '#eee'),
            ('8', lambda: self.entrada.insert(tk.END, '8'), 1, 2, '#eee'),
            ('9', lambda: self.entrada.insert(tk.END, '9'), 2, 2, '#eee'),
            ('*', lambda: self.entrada.insert(tk.END, '*'), 3, 2, '#ccc'),
            ('4', lambda: self.entrada.insert(tk.END, '4'), 0, 3, '#eee'),
            ('5', lambda: self.entrada.insert(tk.END, '5'), 1, 3, '#eee'),
            ('6', lambda: self.entrada.insert(tk.END, '6'), 2, 3, '#eee'),
            ('-', lambda: self.entrada.insert(tk.END, '-'), 3, 3, '#ccc'),
            ('1', lambda: self.entrada.insert(tk.END, '1'), 0, 4, '#eee'),
            ('2', lambda: self.entrada.insert(tk.END, '2'), 1, 4, '#eee'),
            ('3', lambda: self.entrada.insert(tk.END, '3'), 2, 4, '#eee'),
            ('+', lambda: self.entrada.insert(tk.END, '+'), 3, 4, '#ccc'),
            ('0', lambda: self.entrada.insert(tk.END, '0'), 0, 5, 2, '#eee'),
            ('.', lambda: self.entrada.insert(tk.END, '.'), 2, 5, '#eee'),
            ('=', self.funcion_igual, 3, 5, '#ccc')
        ]
        for boton in botones:
            texto = boton[0]
            comando = boton[1]
            columna = boton[2]
            fila = boton[3]
            span = boton[4] if len(boton) > 5 else 1
            color = boton[-1]
            boton = tk.Button(self, text=texto, command=comando, bd=2,
                              bg=color, cursor='hand2', font=('arial', 18, 'bold'))
            boton.grid(column=columna, row=fila, columnspan=span, sticky='NSWE')

if __name__ == '__main__':
    ventana=Calculadora()
    ventana.mainloop()