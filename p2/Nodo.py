class Nodo:

    def __init__(self):
        self.radio = 0.1
        self.color = "#00000000"
        self.posicion = (0, 0)
        self.tipo = ""
        self.id = 0

    def Color(self, r, g, b, a):
        self.color = "#"
        self.color += format(a, '02x')
        self.color += format(r, '02x')
        self.color += format(g, '02x')
        self.color += format(b, '02x')
        # https://www.w3resource.com/python-exercises/python-basic-exercise-141.php
