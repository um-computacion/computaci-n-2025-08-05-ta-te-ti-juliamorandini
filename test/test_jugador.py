import unittest
from src.jugador import Jugador

class TestJugador(unittest.TestCase):
    def test_simbolo(self):
        j = Jugador("X")
        self.assertEqual(j.simbolo, "X")
        self.assertEqual(str(j), "X")

if __name__ == "__main__":
    unittest.main()