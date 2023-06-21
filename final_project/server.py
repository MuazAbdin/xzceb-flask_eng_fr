from flask import Flask, render_template, request
import json
import machinetranslation as mt


app = Flask(__name__)

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    return mt.translator.english_to_french(textToTranslate)

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    return mt.translator.french_to_english(textToTranslate)

@app.route("/")
def renderIndexPage():
    return render_template('index.html')

@app.route("/about")
def view_about_page():
    return render_template("about.html", title="About project")


if __name__ == "__main__":
    app.run(debug=True)