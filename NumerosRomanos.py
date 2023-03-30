
class NumerosRomanos:
    def __init__(self):
        self.resultado = 0

    def numero(self, num_romano):
        for x in num_romano:
            if len(num_romano) == 1:
                if num_romano == "I":
                    self.resultado = 1
                elif num_romano == "V":
                    self.resultado = 5
                elif num_romano == "X":
                    self.resultado = 10
                elif num_romano == "L":
                    self.resultado = 50

        return self.resultado
