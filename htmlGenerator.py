import json
import os
import requests
import tempfile
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

# engine = create_engine('sqlite:///users.db', echo=True)
# Base = declarative_base()
#
# ########################################################################
# class User(Base):
#     """"""
#     __tablename__ = "users"
#
#     id = Column(Integer, primary_key=True)
#     username = Column(String)
#     password = Column(String)
#
#     #----------------------------------------------------------------------
#     def __init__(self, username, password):
#         """"""
#         self.username = username
#         self.set_password(password)
#
#     def set_password(self, password):
#         self.pw_hash = generate_password_hash(password)
#
#     def check_password(self, password):
#         return check_password_hash(self.pw_hash, password)
# # create tables
# Base.metadata.create_all(engine)
#
# ##########################################################################
#
# # create a Session
# Session = sessionmaker(bind=engine)
# session = Session()
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
count = 1
printable_list = []
ALLOWED_EXTENSIONS = set(['csv'])

##HELPERS
def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

#@app.route('/login', methods=['GET'])
#def do_admin_login():
 #   redirect(url_for('landing') + '#myModal2')
  #  POST_USERNAME = str(request.form['username'])
   # POST_PASSWORD = str(request.form['password'])
   # Session = sessionmaker(bind=engine)
   # s = Session()
   # query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]) )
   # result = query.first()
   # if result:
   #     session['logged_in'] = True
   # return landing()
#
# @app.route("/logout")
# def logout():
#     session['logged_in'] = False
#     return home()

##MAIN ROUTING
@app.route('/', methods = ['GET'])
def landing():
    
    #This is how to check authentification.
    #if 'access_token' in session:
     #   return 'Never trust strangers', 404    
    return render_template("default.html", results = printable_list)

@app.route('/', methods = ['POST'])
#@login_required
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
        return render_template("default.html", results=printable_list)

@app.route('/callback')
def callback():
    if 'code' in request.args:
        url = 'https://github.com/login/oauth/access_token'
        payload = {
            'client_id': '535c9a645fbc1e48c632',#Make environment upon real implementation
            'client_secret': 'd47c57f8562ef2f1a11b3d57ccfe7dc7bd4f58e3',
            'code': request.args['code']
        }
        headers = {'Accept': 'application/json'}
        r = requests.post(url, params=payload, headers=headers)
        response = r.json()
        # get access_token from response and store in session
        if 'access_token' in response:
            session['access_token'] = response['access_token']
        else:
            app.logger.error('github didn\'t return an access token, oh dear')
        # send authenticated user where they're supposed to go
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
