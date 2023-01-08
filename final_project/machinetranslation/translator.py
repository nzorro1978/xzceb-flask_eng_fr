#!/bin/python3
'''
This modules uses IBM Watson Translator Service
to implement a simple chatbox web app
'''
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv('.env')
apikey = os.environ['apikey']
url = os.environ['url']


class Translator():
    '''
    Main class wrapper around IBM Watson API
    '''

    def __init__(self):
        self.authenticator = IAMAuthenticator(apikey)
        self.language_translator = LanguageTranslatorV3(
            version='2018-05-01',
            authenticator=self.authenticator
        )
        self.language_translator.set_service_url(url)

    def french_to_english(self, text=None):
        '''
        method to translaste a text from French to English
        '''
        if text is None:
            return text

        if text == "frenchToEnglish":
            return text

        return self.language_translator.translate(
            text=[text],
            model_id='fr-en'
        ).result["translations"][0]["translation"]

    def english_to_french(self, text=None):
        '''
        method to translaste a text from English to French
        '''
        if text is None:
            return text

        if text == "englishToFrench":
            return text

        return self.language_translator.translate(
            text=[text],
            model_id='en-fr'
        ).result["translations"][0]["translation"]
