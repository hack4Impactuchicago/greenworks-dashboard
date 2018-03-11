import json
import os
import tempfile
import csvToDictionary as reader
from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from wtforms.validators import Required


app = Flask(__name__)

##Definitions
path_directory = os.path.join('static','_data')
UPLOAD_FOLDER = os.path.normpath(path_directory);
print(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

printable_list = []
ALLOWED_EXTENSIONS = set(['csv'])

##HELPERS
def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def dictToHtml(opts, description, purpose, source, vision):
    file = render_template('chartTemplate.html', src=source, vs=vision, data=json.dumps(opts), desc=description, purp=purpose)
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config[UPLOAD_FOLDER], filename))


##ROUTING
@app.route('/',  methods = ['GET'])
def landing():
        return render_template("default.html", results = printable_list)

@app.route('/',  methods = ['POST'])
def upload():
    if request.method == "POST":
        file = request.files['Upload']
        if 'Upload' not in request.files:
             flash('No file part')
        if file.filename == '':
             flash('No selected file')
        if file:
             path = os.path.normpath(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename)))
             file.save(path)
             data = reader.csvToDict(file,request.form,app.config['UPLOAD_FOLDER'])
             #now working with the actual template rendering
             values = [json.dumps(data), request.form['source'], request.form['vision'], request.form['subject'], request.form['purpose']]
             printable_list.append(values)
    return render_template("default.html", results=printable_list)


#@app.route('/html')
#def view():
    #fileName = 'static/_data/_low_carbon_commute.csv'
    #data = reader.csvToDict(fileName)
    #return dictToHtml(data)


# FLASK_APP=htmlGenerator.py flask run



if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)

# https://stackoverflow.com/questions/15321431/how-to-pass-a-list-from-python-by-jinja2-to-javascript
