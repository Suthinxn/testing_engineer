from algorithms.pj_two_characters.two_characters import alternate
import unittest

class Two_characters_Test(unittest.TestCase):
    def test_01(self):
        s = "beabeefeab"
        result = alternate(s)
        self.assertEqual(result,5)

    def test_02(self):
        s = "ab"
        result = alternate(s)
        self.assertEqual(result,2)

    def test_03(self):
        s = "aaaaa"
        result = alternate(s)
        self.assertEqual(result,0)

    def test_04(self):
        s = "den"
        result = alternate(s)
        self.assertEqual(result,2)

    def test_05(self):
        s = "!@#$+"
        result = alternate(s)
        self.assertEqual(result,2)

    def test_06(self):
        s = "ggzczxoxwqeihjsswxwxkuxqwcyeuxrppajcyrzahehomrlqzfesagmietjqtwsrioocnjqgggpzzkmxxqlujnqormwffsmhoatqbezymyhxwjtayyilozozzwbhhkewgimejokyvsyobcfprzjdgnhwitwsdssjohhvkvgwpxcnanqufqbskubxxiajpclpraimeozhvpwagabvhjndinvuhfzqlcvbfnkosqdsdzznsibukhlltcgaezcvlsrkbexelggocseryhqyntrolpskbgojetdaidcbcbiwzsemactmumjemlqkbqyqxbgjaqynnworreqbyqyawpqyuorkoqdlvovyqkvyqxffhbfcjabcqribrikvraivghmdssjqywbtkuzhoeltouoztkdjgupiwyowglrtttgcjxnnmvkihxckbayxwcjiyyrymomqclchpiorftyuuuccymzbzobltxojsdzdrtvqwcvclsfbkvxsdcncgzpjwjwvgyxzptjjscmujoslgx"
        result = alternate(s)
        self.assertEqual(result,0)

    def test_07(self):
        s = "clmgakmobtdtdvqttrpgzkjmhcwnflzuazzobixbnyzxbgoszbneqfshlzqspjxtbxhyybxklcqiheeqmkjfpgcjzgzlsanhikvprhedxbvyyksppxkcywwobeakjuvmzzdjptjkzvvovbmakdhabbwrvnztzxoptsytwjgglfdgyhpffwrtqbjgcarmnmuvniwvozocwukpdmaktuqqsufxdqazjppqkolcxsjonluxkhqnwsyudlyvmtgblbzqmjifqpgibndldpdkdsqeesikxwmnrzepefbveihjeacodnljfxjdniribcumqrcnwexjbahwuct"
        result = alternate(s)
        self.assertEqual(result,0)

    def test_08(self):
        s = "cobmjdczpffbxputsaqrwnfcweuothoygvlzugazulgjdbdbarnlffzpogdprjxvtvbmxjujeubiofecvmjmxvofejdvovtjulhhfyadr"
        result = alternate(s)
        self.assertEqual(result,8)

    def test_09(self):
        s = "addonadvance"
        result = alternate(s)
        self.assertEqual(result,3)

    def test_10(self):
        s = "suthinanrongphon"
        result = alternate(s)
        self.assertEqual(result,4)