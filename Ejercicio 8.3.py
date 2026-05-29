import math
import tkinter as tk
from tkinter import messagebox

# ... (Las clases lógicas FiguraGeometrica, Cilindro, Esfera y Piramide se quedan idénticas a la Versión 1) ...

class FiguraGeometrica:
    def __init__(self):
        self._volumen = 0.0
        self._superficie = 0.0

    def set_volumen(self, volumen):
        self._volumen = volumen

    def set_superficie(self, superficie):
        self._superficie = superficie

    def get_volumen(self):
        return self._volumen

    def get_superficie(self):
        return self._superficie


class Cilindro(FiguraGeometrica):
    def __init__(self, radio, altura):
        super().__init__()
        self.radio = radio
        self.altura = altura
        self.set_volumen(self.calcular_volumen())
        self.set_superficie(self.calcular_superficie())

    def calcular_volumen(self):
        return math.pi * self.altura * math.pow(self.radio, 2.0)

    def calcular_superficie(self):
        area_lado_a = 2.0 * math.pi * self.radio * self.altura
        area_lado_b = 2.0 * math.pi * math.pow(self.radio, 2.0)
        return area_lado_a + area_lado_b


class Esfera(FiguraGeometrica):
    def __init__(self, radio):
        super().__init__()
        self.radio = radio
        self.set_volumen(self.calcular_volumen())
        self.set_superficie(self.calcular_superficie())

    def calcular_volumen(self):
        return 1.333 * math.pi * math.pow(self.radio, 3.0)

    def calcular_superficie(self):
        return 4.0 * math.pi * math.pow(self.radio, 2.0)


class Piramide(FiguraGeometrica):
    def __init__(self, base, altura, apotema):
        super().__init__()
        self.base = base
        self.altura = altura
        self.apotema = apotema
        self.set_volumen(self.calcular_volumen())
        self.set_superficie(self.calcular_superficie())

    def calcular_volumen(self):
        return (math.pow(self.base, 2.0) * self.altura) / 3.0

    def calcular_superficie(self):
        area_base = math.pow(self.base, 2.0)
        area_lado = 2.0 * self.base * self.apotema
        return area_base + area_lado


class VentanaCilindro(tk.Toplevel):
    def __init__(self, padre):
        super().__init__(padre)
        self.title("Cilindro")
        self.geometry("280x210")
        self.resizable(False, False)
        self.inicio()

    def inicio(self):
        tk.Label(self, text="Radio (cms):", anchor="w").place(x=20, y=20, width=135, height=23)
        self.campoRadio = tk.Entry(self)
        self.campoRadio.place(x=100, y=20, width=135, height=23)

        tk.Label(self, text="Altura (cms):", anchor="w").place(x=20, y=50, width=135, height=23)
        self.campoAltura = tk.Entry(self)
        self.campoAltura.place(x=100, y=50, width=135, height=23)

        btn_calcular = tk.Button(self, text="Calcular", command=self.action_calcular)
        btn_calcular.place(x=100, y=80, width=135, height=23)

        self.lbl_volumen = tk.StringVar(value="Volumen (cm3):")
        tk.Label(self, textvariable=self.lbl_volumen, anchor="w").place(x=20, y=110, width=200, height=23)

        self.lbl_superficie = tk.StringVar(value="Superficie (cm2):")
        tk.Label(self, textvariable=self.lbl_superficie, anchor="w").place(x=20, y=140, width=200, height=23)

    def action_calcular(self):
        try:
            r = float(self.campoRadio.get())
            h = float(self.campoAltura.get())
            cilindro = Cilindro(r, h)
            self.lbl_volumen.set(f"Volumen (cm3): {cilindro.get_volumen():.2f}")
            self.lbl_superficie.set(f"Superficie (cm2): {cilindro.get_superficie():.2f}")
        except ValueError:
            messagebox.showerror("Error", "Campo nulo o error en formato de número")


class VentanaEsfera(tk.Toplevel):
    def __init__(self, padre):
        super().__init__(padre)
        self.title("Esfera")
        self.geometry("280x200")
        self.resizable(False, False)
        self.inicio()

    def inicio(self):
        tk.Label(self, text="Radio (cms):", anchor="w").place(x=20, y=20, width=135, height=23)
        self.campoRadio = tk.Entry(self)
        self.campoRadio.place(x=100, y=20, width=135, height=23)

        btn_calcular = tk.Button(self, text="Calcular", command=self.action_calcular)
        btn_calcular.place(x=100, y=50, width=135, height=23)

        self.lbl_volumen = tk.StringVar(value="Volumen (cm3):")
        tk.Label(self, textvariable=self.lbl_volumen, anchor="w").place(x=20, y=90, width=200, height=23)

        self.lbl_superficie = tk.StringVar(value="Superficie (cm2):")
        tk.Label(self, textvariable=self.lbl_superficie, anchor="w").place(x=20, y=120, width=200, height=23)

    def action_calcular(self):
        try:
            r = float(self.campoRadio.get())
            esfera = Esfera(r)
            self.lbl_volumen.set(f"Volumen (cm3): {esfera.get_volumen():.2f}")
            self.lbl_superficie.set(f"Superficie (cm2): {esfera.get_superficie():.2f}")
        except ValueError:
            messagebox.showerror("Error", "Campo nulo o error en formato de número")


class VentanaPiramide(tk.Toplevel):
    def __init__(self, padre):
        super().__init__(padre)
        self.title("Pirámide")
        self.geometry("280x240")
        self.resizable(False, False)
        self.inicio()

    def inicio(self):
        tk.Label(self, text="Base (cms):", anchor="w").place(x=20, y=20, width=135, height=23)
        self.campoBase = tk.Entry(self)
        self.campoBase.place(x=120, y=20, width=135, height=23)

        tk.Label(self, text="Altura (cms):", anchor="w").place(x=20, y=50, width=135, height=23)
        self.campoAltura = tk.Entry(self)
        self.campoAltura.place(x=120, y=50, width=135, height=23)

        tk.Label(self, text="Apotema (cms):", anchor="w").place(x=20, y=80, width=135, height=23)
        self.campoApotema = tk.Entry(self)
        self.campoApotema.place(x=120, y=80, width=135, height=23)

        btn_calcular = tk.Button(self, text="Calcular", command=self.action_calcular)
        btn_calcular.place(x=120, y=110, width=135, height=23)

        self.lbl_volumen = tk.StringVar(value="Volumen (cm3):")
        tk.Label(self, textvariable=self.lbl_volumen, anchor="w").place(x=20, y=140, width=200, height=23)

        self.lbl_superficie = tk.StringVar(value="Superficie (cm2):")
        tk.Label(self, textvariable=self.lbl_superficie, anchor="w").place(x=20, y=170, width=200, height=23)

    def action_calcular(self):
        try:
            b = float(self.campoBase.get())
            h = float(self.campoAltura.get())
            a = float(self.campoApotema.get())
            piramide = Piramide(b, h, a)
            self.lbl_volumen.set(f"Volumen (cm3): {piramide.get_volumen():.2f}")
            self.lbl_superficie.set(f"Superficie (cm2): {piramide.get_superficie():.2f}")
        except ValueError:
            messagebox.showerror("Error", "Campo nulo o error en formato de número")


class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Riguras")
        self.geometry("350x160")
        self.resizable(False, False)
        self.inicio()

    def inicio(self):
        btn_cilindro = tk.Button(self, text="Cilindro", command=self.abrir_cilindro)
        btn_cilindro.place(x=20, y=50, width=80, height=23)

        btn_esfera = tk.Button(self, text="Esfera", command=self.abrir_esfera)
        btn_esfera.place(x=125, y=50, width=80, height=23)

        btn_piramide = tk.Button(self, text="Pirámide", command=self.abrir_piramide)
        btn_piramide.place(x=225, y=50, width=100, height=23)

    def abrir_cilindro(self):
        VentanaCilindro(self)

    def abrir_esfera(self):
        VentanaEsfera(self)

    def abrir_piramide(self):
        VentanaPiramide(self)


class Principal:
    @staticmethod
    def main():
        app = VentanaPrincipal()
        app.mainloop()

if __name__ == "__main__":
    Principal.main()

    
