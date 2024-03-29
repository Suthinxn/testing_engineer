from algorithms.pj_alternating_characters.alternating_characters import alternatingCharacters
import unittest

class Alternating_Characters_Test(unittest.TestCase):
    def test_01(self):
        s = "ABABBABAAB"
        result = alternatingCharacters(s)
        self.assertEqual(result,2)

    def test_02(self):
        s = "AAAABAABBB"
        result = alternatingCharacters(s)
        self.assertEqual(result,6)

    def test_03(self):
        s = "AABBBBAAAA"
        result = alternatingCharacters(s)
        self.assertEqual(result,7)

    def test_04(self):
        s = "BABAAABBBB"
        result = alternatingCharacters(s)
        self.assertEqual(result,5)

    def test_05(self):
        s = "ADADADADADADDSKFJDPGNWRGWPOGWGPSDFKSDFKDSAKF"
        result = alternatingCharacters(s)
        self.assertEqual(result,1)

    def test_06(self):
        s = "DENNNANDAFDAFLLAPPDKASFJDAPPPPP"
        result = alternatingCharacters(s)
        self.assertEqual(result,8)

    def test_07(self):
        s = "SUTHINANRONGPHON"
        result = alternatingCharacters(s)
        self.assertEqual(result,0)

    def test_08(self):
        s = "WEWILLWEWILLLROCKYOUROCKYOUU"
        result = alternatingCharacters(s)
        self.assertEqual(result,4)

    def test_09 (self):
        s = "BABABBBBBABBABBBAAABBBBBBBBABBBBBABBBAABBBBABBBBBBBAABABBBBBBABBABBBBBBBBBABBBBBABBABBBBABABBBBBBBBBBBBBBBBBBBABBBBBAABABBBBBBBBBBBABABBBABBBABBBBBBBBBBABBBBBABBBABBBABBABBBBBBAABBBABABBBAABABAABBBBAABBBBBBBBBAAABBABABBABBBABBBBABBBBBABABBBBABABBBAABBABBAABBBBBBABBABBBBBBBBBBBBBBBBBABBBBBBABBBBBBBBABBABBBBBBBBBAAABBBBBBBBBABBABABBBAAABBBBBBABBABBBBBBBABBBBBABBBABBAABAABAAABABBBBBBBABBBBABBBBBABBBBBBABBABBBBBBBBBBBBBBBBBABBABBBAABBBBBAABABBBBBBAABBBBBBBBBABBBBBABBABBBBBBBBBABBBBBBABBBABBBBBABBBBBBBBBBBBBBBBBBABBBBBBBBBBABBBBABABBBBBBBBABBBBBBBBBABBBBBAAABBBBABABABBBBABBBBBBBBBBAABBBBBBBBABBAABBBBBBBBBABAABBBBBBBBBBBBABBBBABABBBBBBBBABBBBBBBBBBBBABBBBABBBBBABBBBBBBBBBABBAABBBABBBBBBBBBABBBBAABBBBBBBBABABABBBBBABBBBBBBBBBBBBBBBBBABBBBABBBBBABBABABAABBBABBBBBBBBBAABABABBBBBBBBAABBBBABBABBBABBBBAABBABABBBBABAABBBBBBBBBBABBABBBBBABAABBBBBBBBBBBBABABBBBBBBBBBABAABABBBBABBBBBBBBBBBBBABBBBBABBABBAABBBBABBBBBBBBBBBAABBBBBBBBBBBBBBAABABBBBBABBBBBBBBBABBBBABBBBABABBABBBBABABBBABABAAABBBBAAAAAABBBA"
        result = alternatingCharacters(s)
        self.assertEqual(result,660)

    def test_10(self):
        s = "AABBABABBBBBABBABABBBBABBABABABBABBABBBBAAABBBBBBBBBBBABBBBBBBABBBBBBBBBBBBABBABBBBAABBBBBAAAABBBBBB"
        result = alternatingCharacters(s)
        self.assertEqual(result,62)