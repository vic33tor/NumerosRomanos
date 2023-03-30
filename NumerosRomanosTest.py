import unittest

from NumerosRomanos import NumerosRomanos


class NumerosRomanosTest(unittest.TestCase):
    def setUp(self) -> None:
        self.n = NumerosRomanos()

    def test_I(self):
        self.assertEqual(self.n.numero("I"), 1)


if __name__ == '__main__':
    unittest.main()