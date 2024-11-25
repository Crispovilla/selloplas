class Ventana:
    """Clase base para representar ventanas genéricas."""

    def __init__(self, ancho, alto):
        if ancho <= 0 or alto <= 0:
            raise ValueError("El ancho y alto deben ser valores positivos.")
        self.ancho = ancho
        self.alto = alto


class VentanaAmericana(Ventana):
    """Representa una ventana americana con medidas específicas."""

    def __init__(self, ancho, alto):
        super().__init__(ancho, alto)
        self.horizontal_movil = self.calcular_horizontal_movil()
        self.vertical = self.calcular_vertical()
        self.travesano = self.calcular_travesano()
        self.riel = self.calcular_riel()
        self.refuerzo_travesano = self.calcular_refuerzo_travesano()
        self.refuerzo_traslapo_movil = self.calcular_refuerzo_traslapo_movil()

    def calcular_horizontal_movil(self):
        return (self.ancho / 2) + 13

    def calcular_vertical(self):
        return self.alto - 43

    def calcular_travesano(self):
        return self.calcular_vertical() - 39

    def calcular_riel(self):
        return self.ancho - 25

    def calcular_refuerzo_travesano(self):
        return self.alto - 84

    def calcular_refuerzo_traslapo_movil(self):
        return self.ancho - 119


class VentanaEuropeaCorredera(Ventana):
    """Representa una ventana europea corredera con medidas específicas."""

    def __init__(self, ancho, alto):
        super().__init__(ancho, alto)
        self.puerta = self.calcular_puerta()
        self.ventana = self.calcular_ventana()
        self.vertical = self.calcular_vertical()

    def calcular_puerta(self):
        return (self.ancho / 2) + 15

    def calcular_ventana(self):
        return (self.ancho / 2) + 5

    def calcular_vertical(self):
        return self.alto - 73


class VentanaEuropeaProyectante(Ventana):
    """Representa una ventana europea proyectante con medidas específicas."""

    def __init__(self, ancho, alto):
        super().__init__(ancho, alto)
        self.ancho_proyectante = self.calcular_ancho_proyectante()
        self.alto_proyectante = self.calcular_alto_proyectante()
        self.travesano = self.calcular_travesano()

    def calcular_ancho_proyectante(self):
        return self.ancho - 106

    def calcular_alto_proyectante(self):
        return self.alto - 106

    def calcular_travesano(self):
        return self.alto - 84
