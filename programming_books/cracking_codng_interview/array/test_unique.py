import unittest
import unique_char


class uniqueChar(unittest.TestCase):
    def testNormalCase(self):
        self.assertEqual(unique_char.hasUniqueChar("string"), True)
        self.assertEqual(unique_char.hasUniqueChar("sstring"),  False)

    def testSpeicalCase(self):
        self.assertEqual(unique_char.hasUniqueChar(""), True)

    def testExtremeCase(self):
        self.assertEqual(unique_char.hasUniqueChar("aaaaaa"), False)


if __name__ == "__main__":
    unittest.main()
