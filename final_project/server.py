from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")
t = translator.Translator()

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here

    return t.english_to_french(str(textToTranslate))

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    return t.french_to_english(str(textToTranslate))

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template("index.html")
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
