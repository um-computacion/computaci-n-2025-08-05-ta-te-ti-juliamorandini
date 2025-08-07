from src.excepciones import PosOcupadaException
from src.tablero import Tablero



class Tateti:

    def __init__(self):

        self.turno = "X"

        self.tablero = Tablero()



    def ocupar_una_de_las_casillas(self, fil, col):

        # Intenta poner la ficha en la posición indicada

        try:

            self.tablero.poner_la_ficha(fil, col, self.turno)

        except PosOcupadaException as e:

            # Si la posición está ocupada, lanza la excepción para que la maneje el CLI

            raise e

        ganador = self.tablero.hay_ganador()

        if ganador:

            print(f"¡Ganó el jugador {ganador}!")

            exit()

        elif self.tablero.esta_lleno():

            print("¡Empate!")

            exit()

        # Cambia el turno solo si no terminó el juego

        self.turno = "0" if self.turno == "X" else "X"

