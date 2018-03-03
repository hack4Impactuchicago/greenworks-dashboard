import json
import os
import parse as parser
import csvToDictionary as reader
from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
from wtforms import Form, BooleanField, StringField, PasswordField, validators

app = Flask(__name__)

#def dictToHtml(opts):
#    return render_template(.., data=json.dumps(opts))

@app.route('/',  methods = ['GET','POST'])
def landing():
    if request.method == "POST":
        return redirect(url_for('uploaded_file'))
    else:
        return render_template("default.html")

##for now just submitting data via postman, need to edit later to render edits]
@app.route('/uploaded_file',  methods = ['POST'])
def upload():
    if request.Form.validateInputs == False:
        return render_template("default.html")
    if 'csv' not in request.files:
        print('No file part')
        return redirect(request.url)
    file = request.files['csv']
    if file.filename == '':
        print('No selected file')
        return redirect(request.url)
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['~/layagollapudi/Desktop'], filename))
        print(filename)




#@app.route('/')
#def view():
    #fileName = '_low_carbon_commute.csv'
    #data = reader.csvToDict(fileName)
    #return dictToHtml(data)


# FLASK_APP=htmlGenerator.py flask run



if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)

# https://stackoverflow.com/questions/15321431/how-to-pass-a-list-from-python-by-jinja2-to-javascript
