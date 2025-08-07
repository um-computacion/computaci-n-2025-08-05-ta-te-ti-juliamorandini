import unittest

class TestCLI(unittest.TestCase):
    def test_cli_import(self):
        import src.cli  # Solo verifica que el archivo se puede importar sin errores

if __name__ == "__main__":
    unittest.main()