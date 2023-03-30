
class NumerosRomanos:
    def __init__(self):
        self.resultado = 0

    def numero(self, num_romano):
        for x in num_romano:
            if len(num_romano) == 1:
                if num_romano == "I":
                    return 1
