
class NumerosRomanos:
    def __init__(self):
        self.resultado = 0
        self.letras = ["I", "V", "X", "L", "C"]

    def numero(self, num_romano):
        if len(num_romano) == 1:
            if num_romano == "I":
                self.resultado = 1
            elif num_romano == "V":
                self.resultado = 5
            elif num_romano == "X":
                self.resultado = 10
            elif num_romano == "L":
                self.resultado = 50
            elif num_romano == "C":
                self.resultado = 100
        else:
            for i, x in num_romano:
                if x == "I":
                    self.resultado += 1
                elif x == "V":
                    self.resultado += 5
                elif x == "X":
                    self.resultado += 10
                elif x == "L":
                    self.resultado += 50
                elif x == "C":
                    self.resultado += 100



        return self.resultado
