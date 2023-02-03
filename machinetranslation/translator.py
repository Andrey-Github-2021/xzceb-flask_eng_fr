"""This python file is using IBM Watson to translate english to Franch and Franch to English"""
import os
from ibm_watson import LanguageTranslatorV3 # pylint: disable=import-error
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator # pylint: disable=import-error
from dotenv import load_dotenv # pylint: disable=import-error
load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(url)


def englishToFrench(english_text): 
    """function for translate english to Franch"""

    translation    =    language_translator.translate(
    text    =    english_text,
    model_id    =    'en-fr')
    french_text    =     translation.get_result()['translations'][0]['translation']
    return french_text


def frenchToEnglish(french_text):
    """function for translate Franch to English"""
    #write the code here

    translation    =    language_translator.translate(
    text    =    french_text,
    model_id    =    'fr-en')
    english_text    =    translation.get_result()['translations'][0]['translation']
    return english_text
