#!/bin/python3
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']

class Translator():
    def __init__(self):
        self.authenticator = IAMAuthenticator(apikey)
        self.language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=self.authenticator
        )
        self.language_translator.set_service_url(url)


    def frenchToEnglish(self, text):
        if text == None:
            return

        if text == "frenchToEnglish":
            return text
        
        return self.language_translator.translate(
            text = [text],
            model_id='fr-en'
        ).result["translations"][0]["translation"]

    def englishToFrench(self, text):                
        if text == None:            
            return
            
        if text == "englishToFrench":
            return text

        return self.language_translator.translate(
            text = [text],
            model_id='en-fr'
        ).result["translations"][0]["translation"]