import json
import os
import requests
import tempfile
import shelve
import sqlite3
import random
import csvToDictionary as reader
from flask import Flask, request, render_template, redirect, url_for, g, session
from flask import render_template_string
from werkzeug.utils import secure_filename
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from wtforms.validators import Required

app = Flask(__name__)


#
# user = User("admin","password")
# session.add(user)
#
# # commit the record the database
# session.commit()


def createChartID():
    conn = sqlite3.connect('charts.db')
    c = conn.cursor()
    while True:
        id = random.randint(1, 1000000)
        c.execute('Select * FROM charts WHERE chartid =?', (id,))
        preexisting = c.fetchone()
        if preexisting is None:
            break
    conn.commit()
    conn.close()
    return id

def findNextAvailable():
    conn = sqlite3.connect('charts.db')
    c = conn.cursor()
    c.execute('SELECT Count(*) FROM charts')
    numrow = c.fetchone()
    num = 0
    if numrow:
        num = numrow[0] + 1
    conn.commit()
    c.close()
    return num

##Definitions
path_directory = os.path.join('static','_data')
UPLOAD_FOLDER = os.path.normpath(path_directory)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
printable_list = []
ALLOWED_EXTENSIONS = set(['csv'])

##HELPERS
def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route("/logout")
def logout():
    session['logged_in'] = False
    session['authenticated'] = False
    return redirect('/')

##MAIN ROUTING
@app.route('/', methods = ['GET'])
def landing():
    if not 'logged_in' in session:
        session['logged_in'] = False
        session['authenticated'] = False
    conn = sqlite3.connect('charts.db')
    c = conn.cursor()
    c.execute('SELECT * FROM charts ORDER BY position')
    return render_template("default.html", results = c.fetchall())

@app.route('/', methods = ['POST'])
def upload():
    if request.method == "POST":
        file = request.files['Upload']
    if 'Upload' not in request.files:
        flash('No file part')
    if file.filename == '':
        flash('No selected file')
    if file:
        conn = sqlite3.connect('charts.db')
        c = conn.cursor()
        file.filename = secure_filename(file.filename)
        path = os.path.normpath(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename)))
        file.save(path)
        data = reader.csvToDict(file,request.form,app.config['UPLOAD_FOLDER'])
         #now working with the actual template rendering
        values = (json.dumps(data), request.form['source'], request.form['vision'], request.form['subject'], request.form['purpose'], createChartID(), findNextAvailable())
        c.execute('INSERT INTO charts VALUES (?, ?, ?, ?, ?, ?, ?)', values)
        conn.commit()
        conn.close()
        return redirect('/')

@app.route('/editing', methods = ['POST'])
def edit():
    conn = sqlite3.connect('charts.db')
    c = conn.cursor()
    c.execute('SELECT * FROM charts')
    rows = c.fetchall()
    for counter, entry in enumerate(rows):
        form = request.form[str(counter + 1)]
        c.execute('UPDATE charts SET position = ? WHERE chartid = ?', (counter + 1, form))
    conn.commit()
    conn.close()
    return redirect('/')    

@app.route('/deleting', methods = ['POST'])
def delete():
    deletions = request.form.getlist('deletion')
    conn = sqlite3.connect('charts.db')
    c = conn.cursor()
    for result in deletions:
        c.execute('DELETE FROM charts WHERE chartid = ?', (result,))
    c.execute('SELECT * FROM charts ORDER BY position')
    rows = c.fetchall()
    for counter, entry in enumerate(rows):
        c.execute('UPDATE charts SET position = ? WHERE chartid = ?', (counter + 1, entry[5]))
    conn.commit()
    conn.close()
    return redirect('/')
    
@app.route('/adduser', methods = ['POST'])
def adduser():
    username = request.form["username"]
    print(username)
    conn = sqlite3.connect('charts.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE username = ?', (username,))
    output = c.fetchone()
    if output is not None:
        return redirect('/')
    c.execute('INSERT INTO users VALUES (?)', (username,))
    conn.commit()
    conn.close()
    return redirect('/')


@app.route('/callback')
def callback():
    if 'code' in request.args:
        url = 'https://github.com/login/oauth/access_token'
        payload = {
            'client_id': '74db254106d90e8610cb',#Make environment upon real implementation
            'client_secret': 'e99fc11a7901fbaa706b01ca1688569dbbc74412',
            'code': request.args['code']
        }
        headers = {'Accept': 'application/json'}
        r = requests.post(url, params=payload, headers=headers)
        response = r.json()
        if 'access_token' in response:
            session['access_token'] = response['access_token']

            # This gets the github user's information
            access_token_url = 'https://api.github.com/user?access_token={}'
            r2 = requests.get(access_token_url.format(session['access_token']))
            response2 = r2.json()
            username = response2['login']
            # This gets the github user's information

            session['logged_in'] = True

            # Now we check if this user is an approved user
            conn = sqlite3.connect('charts.db')
            c = conn.cursor()
            c.execute('SELECT * FROM users WHERE username = ?', (username,))
            user = c.fetchone()
            if user is not None:
                session['authenticated'] = True
            conn.commit()
            conn.close()
        return redirect('/')
    return '', 404



#@app.route('/html')
#def view():
    #fileName = 'static/_data/_low_carbon_commute.csv'
    #data = reader.csvToDict(fileName)
    #return dictToHtml(data)


# FLASK_APP=htmlGenerator.py flask run



if __name__ == "__main__":
    #init_db()
    app.secret_key = 'd47c57f8562ef2f1a11b3d57ccfe7dc7bd4f58e3'
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)

# https://stackoverflow.com/questions/15321431/how-to-pass-a-list-from-python-by-jinja2-to-javascript
