import unittest

from NumerosRomanos import NumerosRomanos


class NumerosRomanosTest(unittest.TestCase):
    def setUp(self) -> None:
        self.n = NumerosRomanos()

    def test_I(self):
        self.assertEqual(self.n.numero("I"), 1)

    def test_V(self):
        self.assertEqual(self.n.numero("V"), 5)

    def test_X(self):
        self.assertEqual(self.n.numero("X"), 10)

    def test_L(self):
        self.assertEqual(self.n.numero("L"), 50)

    def test_C(self):
        self.assertEqual(self.n.numero("C"), 100)

    def test_dos_num_iguales(self):
        self.assertEqual(self.n.numero("XX"), 20)


if __name__ == '__main__':
    unittest.main()