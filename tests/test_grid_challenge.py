from algorithms.pj_grid_challenge.grid_challenge import gridChallenge
import unittest

class Grid_Challenge_Test(unittest.TestCase):
    def test_01(self):
        grid = ["eabcd", "fghij", "olkmn", "trpqs", "xywuv"]
        result = gridChallenge(grid)
        self.assertEqual(result, "YES")

    def test_02(self):
        grid = ["kc", "iu"]
        result = gridChallenge(grid)
        self.assertEqual(result, "YES")

    def test_03(self):
        grid = ["uxf", "vof", "hmp"]
        result = gridChallenge(grid)
        self.assertEqual(result, "NO")

    def test_04(self):
        grid = ["lyivr", "jgfew", "uweor", "qxwyr", "uikjd"]
        result = gridChallenge(grid)
        self.assertEqual(result, "NO")

    def test_05(self):
        grid = ["12345", "67890", "12345", "67890", "12345"]
        result = gridChallenge(grid)
        self.assertEqual(result, "NO")

    def test_06(self):
        grid = ["ab", "cd"]
        result = gridChallenge(grid)
        self.assertEqual(result, "YES")

    def test_07(self):
        grid = ["den", "kan", "pik"]
        result = gridChallenge(grid)
        self.assertEqual(result, "NO")

    def test_08(self):
        grid = ["eibjbwsp", "ptfxehaq", "jxipvfga", "rkefiyub", "kalwfhfj", "lktajiaq", "srdgoros", "nflvjznh"]
        result = gridChallenge(grid)
        self.assertEqual(result, "NO")

    def test_09(self):
        grid = ["!@#", "$%^&", "!@#"]
        result = gridChallenge(grid)
        self.assertEqual(result, "NO")

    def test_10(self):
        grid = ["as1", "as2", "as3"]
        result = gridChallenge(grid)
        self.assertEqual(result, "YES")