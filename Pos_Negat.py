import tkinter as tk
from tkinter import messagebox

def verificar_numero():
    try:
        num = int(entrada.get())
        if num > 0:
            mensaje = "El número es positivo"
        elif num < 0:
            mensaje = "El número es negativo"
        else:
            mensaje = "El número es cero"
        messagebox.showinfo("Resultado", mensaje)
        
        # Preguntar si quiere intentar con otro número
        repetir = messagebox.askyesno("Repetir", "¿Quieres intentar con otro número?")
        if repetir:
            entrada.delete(0, tk.END)  # Borra el campo de entrada
        else:
            root.destroy()  # Cierra la ventana
    except ValueError:
        messagebox.showerror("Error", "Por favor, introduce un número válido")

# Crear la ventana principal
root = tk.Tk()
root.title("Verificador de números")

# Etiqueta
etiqueta = tk.Label(root, text="Introduce un número:")
etiqueta.pack(pady=10)

# Entrada
entrada = tk.Entry(root)
entrada.pack(pady=5)

# Botón para verificar
boton = tk.Button(root, text="Verificar", command=verificar_numero)
boton.pack(pady=10)

# Ejecutar la aplicación
root.mainloop()
