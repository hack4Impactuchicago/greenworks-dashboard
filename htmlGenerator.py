import json
import os
import requests
import tempfile
import shelve
import csvToDictionary as reader
from flask import Flask, request, render_template, redirect, url_for, g, session
from flask import render_template_string
from werkzeug.utils import secure_filename
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from wtforms.validators import Required

app = Flask(__name__)

from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from werkzeug.security import generate_password_hash, \
     check_password_hash
import datetime
from sqlalchemy.orm import sessionmaker


#
# user = User("admin","password")
# session.add(user)
#
# # commit the record the database
# session.commit()


##Definitions
path_directory = os.path.join('static','_data')
UPLOAD_FOLDER = os.path.normpath(path_directory);

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
printable_list = []
with shelve.open('shelve') as db:
    flag = 'list' in db
    if flag:
        printable_list = db['list']
    else:
        printable_list = []
        db['list'] = printable_list
    db.close()
count = len(printable_list) + 1
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
    with shelve.open('shelve') as db:
        printable_list = db['list']
        db.close()
    if not 'logged_in' in session:
        session['logged_in'] = False
        session['authenticated'] = False
    return render_template("default.html", results = printable_list)

@app.route('/', methods = ['POST'])
def upload():
    if request.method == "POST":
        file = request.files['Upload']
    if 'Upload' not in request.files:
        flash('No file part')
    if file.filename == '':
        flash('No selected file')
    if file:
        global count
        file.filename = secure_filename(file.filename)
        path = os.path.normpath(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename)))
        file.save(path)
        data = reader.csvToDict(file,request.form,app.config['UPLOAD_FOLDER'])
         #now working with the actual template rendering
        myString = "myChart" + str(count)
        print(myString)
        values = [json.dumps(data), request.form['source'], request.form['vision'], request.form['subject'], request.form['purpose'], myString]
        printable_list.append(values)
        count += 1
        with shelve.open('shelve') as db:
            del db['list']
            db['list'] = printable_list
            db.close()
        return redirect('/')

@app.route('/editing', methods = ['POST'])
def edit():
    global printable_list
    global count
    numlist = []
    dels = []
    count2 = 0
    for result in printable_list:
        if request.form[result[5]] == "delete":
            dels.append(result)
            print(result)
        else:
            numlist.append(int(request.form[result[5]]) - 1)
        count2 += 1
    for val in dels:
        printable_list.remove(val)
    printable_list = [ printable_list[i] for i in numlist ]
    with shelve.open('shelve') as db:
        del db['list']
        db['list'] = printable_list
        db.close()
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
            engine = create_engine('sqlite:///users.db', echo=True)
            Base = declarative_base()

            class User(Base):
                __tablename__ = "users"

                id = Column(Integer, primary_key=True)
                username = Column(String)

            # # create tables
            Base.metadata.create_all(engine)

            # # create a Session
            dbSession = sessionmaker(bind=engine)
            dbsession = dbSession()

            if dbsession.query(User).filter(User.username == username).first() is not None:
                session['authenticated'] = True
                print('yes')

            dbsession.close()
            engine.dispose()
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
