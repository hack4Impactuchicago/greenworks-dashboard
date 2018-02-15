import json
import csvToDictionary as reader
from flask import Flask, request, render_template, Markup
app = Flask(__name__)

@app.route('/')
def landing():
    return render_template("default.html");

#@app.route('/')
#def view():
    #fileName = '_low_carbon_commute.csv'
    #data = reader.csvToDict(fileName)
    #return dictToHtml(data)


# FLASK_APP=htmlGenerator.py flask run

#def dictToHtml(opts):
    #return render_template('_low_carbon_commute.html', data=json.dumps(opts))

if __name__ == "__main__":
    app.run()

# https://stackoverflow.com/questions/15321431/how-to-pass-a-list-from-python-by-jinja2-to-javascript
