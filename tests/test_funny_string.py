from algorithms.pj_funny_string.funny_string import funnyString
import unittest


class Funny_String_Test(unittest.TestCase):
    def test_01(self):
        s = "acxz"
        result = funnyString(s)
        self.assertEqual(result,"Funny")

    def test_02(self):
        s = "bcxz"
        result = funnyString(s)
        self.assertEqual(result,"Not Funny")

    def test_03(self):
        s = "ovyvzvptyvpvpxyztlrztsrztztqvrxtxuxq"
        result = funnyString(s)
        self.assertEqual(result,"Funny")

    def test_04(self):
        s = "fmpszyvqwxrtvpuwqszvyvotmsxsxuvzyvpwzrpmuxqwtswvytytzsnuxuyrpvtysqoutzurqxury"
        result = funnyString(s)
        self.assertEqual(result,"Not Funny")

    def test_05(self):
        s = "{test}"
        result = funnyString(s)
        self.assertEqual(result,"Not Funny")

    def test_06(self):
        s = "{{suthinan_Rongphon}}"
        result = funnyString(s)
        self.assertEqual(result,"Not Funny")    

    def test_07(self):
        s = "ptvzstvotxqyvzrwyqryzrpkswzryupwutmigc"
        result = funnyString(s)
        self.assertEqual(result,"Funny")

    def test_08(self):
        s = "abcdefghijklmnopqrstuvwsyz"
        result = funnyString(s)
        self.assertEqual(result,"Not Funny")

    def test_09(self):
        s = "hxckerrankdotcom"
        result = funnyString(s)
        self.assertEqual(result,"Not Funny")

    def test_10(self):
        s = "asdfadpsgjajgeraihgsfajvpamwepofweqgqjwgpmmfd;hgewairjtjgqpwjrelkfjasdjf;ladfvnear;bvneqrgifq;aerjfedihgdsfg;jerijgefgjlkfdsjgs;odgij;erojgtwoerijgoidsfjgs;eroijgwaoerijgoas;eiofgjskdfjgiaieorjtgwae;fgad;lkgjsd;gomewirjgoejgflkdsgj;slejrg;werogjsdf;lgjof;dg"
        result = funnyString(s)
        self.assertEqual(result,"Not Funny")