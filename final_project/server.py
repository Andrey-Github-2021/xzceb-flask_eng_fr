from machinetranslation import translator
from flask import Flask, render_template, request
import json
import machinetranslation

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    French_text = machinetranslation.englishToFrench(textToTranslate)
    return French_text     "Translated text to French"

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    Eng_text = machinetranslation.frenchToEnglish(textToTranslate)
    return Eng_text         "Translated text to English"

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    index.html
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
