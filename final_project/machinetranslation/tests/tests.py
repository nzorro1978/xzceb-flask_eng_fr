#!/bin/python3.8
import unittest
from machinetranslation import translator

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        outText = "englishToFrench"
        t = translator.Translator()
        self.assertIsNone(t.english_to_french()) # assert None yields None
        self.assertEqual(t.english_to_french(outText), outText) # asserts for good function definition
        translation = "bonjour"
        self.assertEqual(t.english_to_french("Hello").lower(), translation) # asserts basic translation

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        outText = "frenchToEnglish"
        t = translator.Translator()
        self.assertIsNone(t.french_to_english()) # assert None yields None
        self.assertEqual(t.french_to_english(outText), outText) # asserts for good function definition
        textToTranslate = "Bonjour"
        self.assertEqual(t.french_to_english(textToTranslate).lower(), "hello") # asserts basic translation

if __name__ == "__main__":    
    unittest.main()