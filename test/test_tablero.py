import unittest
from src.tablero import Tablero
from src.excepciones import PosOcupadaException

class TestTablero(unittest.TestCase):
    def test_tablero_inicial_vacio(self):
        t = Tablero()
        self.assertEqual(t.contenedor, [["", "", ""], ["", "", ""], ["", "", ""]])

    def test_poner_ficha(self):
        t = Tablero()
        t.poner_la_ficha(0, 0, "X")
        self.assertEqual(t.contenedor[0][0], "X")

    def test_pos_ocupada_exception(self):
        t = Tablero()
        t.poner_la_ficha(0, 0, "X")
        with self.assertRaises(PosOcupadaException):
            t.poner_la_ficha(0, 0, "0")

    def test_hay_ganador_fila(self):
        t = Tablero()
        for col in range(3):
            t.poner_la_ficha(1, col, "X")
        self.assertEqual(t.hay_ganador(), "X")

    def test_hay_ganador_columna(self):
        t = Tablero()
        for fila in range(3):
            t.poner_la_ficha(fila, 2, "0")
        self.assertEqual(t.hay_ganador(), "0")

    def test_hay_ganador_diagonal(self):
        t = Tablero()
        for i in range(3):
            t.poner_la_ficha(i, i, "X")
        self.assertEqual(t.hay_ganador(), "X")

    def test_empate(self):
        t = Tablero()
        jugadas = [
            (0, 0, "X"), (0, 1, "0"), (0, 2, "X"),
            (1, 0, "X"), (1, 1, "0"), (1, 2, "0"),
            (2, 0, "0"), (2, 1, "X"), (2, 2, "X"),
        ]
        for f, c, s in jugadas:
            t.poner_la_ficha(f, c, s)
        self.assertTrue(t.esta_lleno())
        self.assertIsNone(t.hay_ganador())

if __name__ == "__main__":
    unittest.main()