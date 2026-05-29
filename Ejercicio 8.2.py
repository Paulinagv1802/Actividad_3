import tkinter as tk
from tkinter import messagebox
from math import pow, sqrt


class Notas:
    def __init__(self):
        self.lista_notas = [0.0] * 5

    def calcular_promedio(self):
        suma = 0.0
        for i in range(0, len(self.lista_notas)):  
            suma += self.lista_notas[i]
        return suma / len(self.lista_notas)

    def calcular_desviacion(self):
        prom = self.calcular_promedio()
        suma = 0.0
        for i in range(0, len(self.lista_notas)):
            suma += pow(self.lista_notas[i] - prom, 2)
        return sqrt(suma / len(self.lista_notas))

    def calcular_menor(self):
        menor = self.lista_notas[0]
        for i in range(0, len(self.lista_notas)):
            if self.lista_notas[i] < menor:
                menor = self.lista_notas[i]
        return menor

    def calcular_mayor(self):
        mayor = self.lista_notas[0]
        for i in range(0, len(self.lista_notas)):
            if self.lista_notas[i] > mayor:
                mayor = self.lista_notas[i]
        return mayor


# Ventana Principal
class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Notas")
        self.geometry("280x380")
        self.resizable(False, False)
        
        
        self.inicio()

    def inicio(self):
        # Etiquetas de Nota 1 a Nota 5
        tk.Label(self, text="Nota 1:").place(x=20, y=20, width=135, height=23)
        tk.Label(self, text="Nota 2:").place(x=20, y=50, width=135, height=23)
        tk.Label(self, text="Nota 3:").place(x=20, y=80, width=135, height=23)
        tk.Label(self, text="Nota 4:").place(x=20, y=110, width=135, height=23)
        tk.Label(self, text="Nota 5:").place(x=20, y=140, width=135, height=23)

        # Campos de texto (En Tkinter se llaman Entry)
        self.campoNota1 = tk.Entry(self)
        self.campoNota1.place(x=105, y=20, width=135, height=23)
        
        self.campoNota2 = tk.Entry(self)
        self.campoNota2.place(x=105, y=50, width=135, height=23)
        
        self.campoNota3 = tk.Entry(self)
        self.campoNota3.place(x=105, y=80, width=135, height=23)
        
        self.campoNota4 = tk.Entry(self)
        self.campoNota4.place(x=105, y=110, width=135, height=23)
        
        self.campoNota5 = tk.Entry(self)
        self.campoNota5.place(x=105, y=140, width=135, height=23)


        # Botones 
        self.calcular = tk.Button(self, text="Calcular", command=self.action_calcular)
        self.calcular.place(x=20, y=170, width=100, height=23)

        self.limpiar = tk.Button(self, text="Limpiar", command=self.action_limpiar)
        self.limpiar.place(x=125, y=170, width=80, height=23)


        # Etiquetas 
        self.promedio = tk.StringVar(value="Promedio = ")
        tk.Label(self, textvariable=self.promedio, anchor="w").place(x=20, y=210, width=135, height=23)

        self.desviacion = tk.StringVar(value="Desviación = ")
        tk.Label(self, textvariable=self.desviacion, anchor="w").place(x=20, y=240, width=200, height=23)

        self.mayor = tk.StringVar(value="Nota mayor = ")
        tk.Label(self, textvariable=self.mayor, anchor="w").place(x=20, y=270, width=120, height=23)

        self.menor = tk.StringVar(value="Nota menor = ")
        tk.Label(self, textvariable=self.menor, anchor="w").place(x=20, y=300, width=120, height=23)


    

    def action_calcular(self):
        try:
            notas = Notas()
            # Obtenemos el texto de los campos y lo convertimos a float
            notas.lista_notas[0] = float(self.campoNota1.get())
            notas.lista_notas[1] = float(self.campoNota2.get())
            notas.lista_notas[2] = float(self.campoNota3.get())
            notas.lista_notas[3] = float(self.campoNota4.get())
            notas.lista_notas[4] = float(self.campoNota5.get())

            # Actualizamos las etiquetas dinámicas
            self.promedio.set(f"Promedio = {notas.calcular_promedio():.2f}")
            self.desviacion.set(f"Desviación estándar = {notas.calcular_desviacion():.2f}")
            self.mayor.set(f"Valor mayor = {notas.calcular_mayor()}")
            self.menor.set(f"Valor menor = {notas.calcular_menor()}")
            
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos en todas las notas.")


    def action_limpiar(self):
        self.campoNota1.delete(0, tk.END)
        self.campoNota2.delete(0, tk.END)
        self.campoNota3.delete(0, tk.END)
        self.campoNota4.delete(0, tk.END)
        self.campoNota5.delete(0, tk.END)
        self.promedio.set("Promedio = ")
        self.desviacion.set("Desviación = ")
        self.mayor.set("Nota mayor = ")
        self.menor.set("Nota menor = ")


# --- CLASE PRINCIPAL (PUNTO DE ENTRADA) ---
class Principal:
    @staticmethod
    def main():
        miVentanaPrincipal = VentanaPrincipal()
        miVentanaPrincipal.mainloop()  # Mantiene la ventana abierta 

if __name__ == "__main__":
    Principal.main()

