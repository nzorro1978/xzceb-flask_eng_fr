import unittest  
from translator import Translator

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        outText = "englishToFrench"
        t = Translator()
        self.assertIsNone(t.englishToFrench()) # assert None yields None
        self.assertEqual(t.englishToFrench(outText), outText) # asserts for good function definition
        translation = "bonjour"
        self.assertEqual(t.englishToFrench("Hello").lower(), translation) # asserts basic translation

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        outText = "frenchToEnglish"
        t = Translator()
        self.assertIsNone(t.frenchToEnglish()) # assert None yields None
        self.assertEqual(t.frenchToEnglish(outText), outText) # asserts for good function definition
        textToTranslate = "Bonjour"
        self.assertEqual(t.frenchToEnglish(textToTranslate).lower(), "hello") # asserts basic translation


unittest.main()