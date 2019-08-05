import unittest
import palindromePermu


class paliPermu(unittest.TestCase):
    def testNormalCase(self):
        self.assertEqual(palindromePermu.isPalindromePermu("aaccb"), True)
    #     self.assertEqual(palindromePermu.isPalindromePermu("sstring"),  False)

    # def testSpeicalCase(self):
    #     self.assertEqual(palindromePermu.isPalindromePermu(""), True)

    # def testExtremeCase(self):
    #     self.assertEqual(palindromePermu.isPalindromePermu("aaaaaa"), False)


if __name__ == "__main__":
    unittest.main()
