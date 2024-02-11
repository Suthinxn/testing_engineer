from algorithms.pj_casesar_cipher.casesar_cipher import caesarCipher
import unittest

class Casesar_cipher_Test(unittest.TestCase):
    def test_01(self):
        s = "Hello_World!"
        k = 4
        result = caesarCipher(s, k)
        self.assertEqual(result,"Lipps_Asvph!")

    def test_02(self):
        s = "suthinanrongphon"
        k = 4
        result = caesarCipher(s, k)
        self.assertEqual(result,"wyxlmrervsrktlsr")

    def test_03(self):
        s = "welcometoyourlife"
        k = 10
        result = caesarCipher(s, k)
        self.assertEqual(result,"govmywodyiyebvspo")

    def test_04(self):
        s = ""
        k = 2
        result = caesarCipher(s, k)
        self.assertEqual(result,"")

    def test_05(self):
        s = "D3q4"
        k = 0
        result = caesarCipher(s, k)
        self.assertEqual(result,"D3q4")

    def test_06(self):
        s = "hackerrank"
        k = 10
        result = caesarCipher(s, k)
        self.assertEqual(result,"rkmuobbkxu")

    def test_07(self):
        s = "Always-Look-on-the-Bright-Side-of-Life"
        k = 5   
        result = caesarCipher(s, k)
        self.assertEqual(result,"Fqbfdx-Qttp-ts-ymj-Gwnlmy-Xnij-tk-Qnkj")

    def test_08(self):
        s = "!*(@@)$%^+_=)(#*@!)h"
        k = 2
        result = caesarCipher(s, k)
        self.assertEqual(result,"!*(@@)$%^+_=)(#*@!)j")

    def test_09(self):
        s = "APCKWLNCJO"
        k = 23
        result = caesarCipher(s, k)
        self.assertEqual(result,"XMZHTIKZGL")

    def test_10(self):
        s = "DEPLOY-WEB-HACKER-DEN"
        k = 19
        result = caesarCipher(s, k)
        self.assertEqual(result,"WXIEHR-PXU-ATVDXK-WXG")