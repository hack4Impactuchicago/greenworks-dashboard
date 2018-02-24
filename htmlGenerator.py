import json
import os
import csvToDictionary as reader
from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)

#def dictToHtml(opts):
#    return render_template(.., data=json.dumps(opts))

UPLOAD_FOLDER = '~/layagollapudi/Desktop'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods = ['GET'])
def landing():
    return render_template("default.html");


#@app.route('/', methods = ['POST'])
# def result():
#   if request.method == 'POST':
#        #function for saving the information in server
#        #use jquery
#       result = request.form;
#       return render_template("default.html",result = result);

##for now just submitting data via postman, need to edit later to render edits
@app.route('/', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        print(request.files)
        # check if the post request has the file part
        if 'csv' not in request.files:
            print('No file part')
            return redirect(request.url)
        file = request.files['csv']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            print('No selected file')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print(filename)
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

#@app.route('/')
#def view():
    #fileName = '_low_carbon_commute.csv'
    #data = reader.csvToDict(fileName)
    #return dictToHtml(data)


# FLASK_APP=htmlGenerator.py flask run



if __name__ == "__main__":
    app.run()

# https://stackoverflow.com/questions/15321431/how-to-pass-a-list-from-python-by-jinja2-to-javascript
