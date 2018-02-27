class Nodo:

    def __init__(self):
        self.radio = 0.1
        self.color = "#00000000"
        self.posicion = (0, 0)
        self.tipo = ""
        self.id = 0

    def Color(self, r, g, b, a):
        self.color = "#" + str(hex(a)[2:] + str(hex(r)[2:]) + str(hex(g)[2:]) + str(hex(b)[2:])) # https://stackoverflow.com/questions/5796238/python-convert-decimal-to-hex
