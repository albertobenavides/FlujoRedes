class Nodo:

    def __init__(self):
        self.id = "1"
        self.tipo = ""
        self.posicion = (0.5, 0.5)
        self.radio = 0.1
        self.color = "#0080808080"

    def Color(self, r, g, b, a):
        self.color = "#"
        self.color += format(a, '02x')
        self.color += format(r, '02x')
        self.color += format(g, '02x')
        self.color += format(b, '02x')
        # https://www.w3resource.com/python-exercises/python-basic-exercise-141.php
