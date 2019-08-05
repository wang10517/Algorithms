import unittest
import urlify


class replaceSpace(unittest.TestCase):
    def testNormalCase(self):
        self.assertEqual(urlify.replaceSpace(
            "Mr John Smith     ", 13), "Mr%20John%20Smith")
    #     self.assertEqual(urlify.replaceSpace("sstring"),  False)

    # def testSpeicalCase(self):
    #     self.assertEqual(urlify.replaceSpace(""), True)

    def testExtremeCase(self):
        self.assertEqual(urlify.replaceSpace(
            "abc              ", 7), "abc%20%20%20%20")


if __name__ == "__main__":
    unittest.main()
