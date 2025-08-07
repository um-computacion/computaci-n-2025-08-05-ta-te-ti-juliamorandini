from src.excepciones import PosOcupadaException

class Tablero:


    def __init__(self):

        self.contenedor = [

            ["", "", ""],

            ["", "", ""],

            ["", "", ""],

        ]



    def poner_la_ficha(self, fil, col, ficha):

        # ver si esta ocupado...

        if self.contenedor[fil][col] == "":

            self.contenedor[fil][col] = ficha

        else:

            raise PosOcupadaException("pos ocupada!")
        
    def esta_vacia(self, fil, col):
        # Devuelve True si la casilla está vacía, False si está ocupada
        return self.contenedor[fil][col] == ""

    def hay_ganador(self):
        # Chequea filas y columnas
        for i in range(3):
            if self.contenedor[i][0] != "" and all(self.contenedor[i][j] == self.contenedor[i][0] for j in range(3)):
                return self.contenedor[i][0]
            if self.contenedor[0][i] != "" and all(self.contenedor[j][i] == self.contenedor[0][i] for j in range(3)):
                return self.contenedor[0][i]
        # Chequea diagonales
        if self.contenedor[0][0] != "" and all(self.contenedor[d][d] == self.contenedor[0][0] for d in range(3)):
            return self.contenedor[0][0]
        if self.contenedor[0][2] != "" and all(self.contenedor[d][2-d] == self.contenedor[0][2] for d in range(3)):
            return self.contenedor[0][2]
        return None

    def esta_lleno(self):
        return all(self.contenedor[f][c] != "" for f in range(3) for c in range(3))

    def __str__(self):
        return str(self.contenedor)
