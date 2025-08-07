import unittest
from src.tateti import Tateti

class TestTateti(unittest.TestCase):
    def test_turno_cambia(self):
        juego = Tateti()
        self.assertEqual(juego.turno, "X")
        juego.ocupar_una_de_las_casillas(0, 0)
        self.assertEqual(juego.turno, "0")
        juego.ocupar_una_de_las_casillas(0, 1)
        self.assertEqual(juego.turno, "X")

if __name__ == "__main__":
    unittest.main()