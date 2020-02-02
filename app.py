from flask import Flask, render_template, flash, redirect, request, send_from_directory
from form import SendForm, LoginForm, UploadForm
from config import Config
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename
import json
import os
from flask_bootstrap import Bootstrap
from  xls2xml_bayes.bayes import parse


app=Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html', title='Home')


@app.route('/send',methods=['GET','POST'])
def send():
    form = SendForm()
    if form.validate_on_submit():

        flash('Thank you for send data, {}'.format(form.username.data))
    
        #<shop>
        name=form.username.data
        company=form.company.data
        url=form.url.data

        data = {
                "name":name,
                "company":company,
                "url":url
                }

        with open('user_info.json', 'w') as f:
             f.write(json.dumps(data))
        

        #offer
        f = form.upload.data
        filename = 'excel.xlsx'
        f.save(os.path.join('uploads/', filename))
        parse()
        return redirect('/yml')
    
    return render_template('forms.html',title='Send', form=form)

@app.route('/login', methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        name=form.username.data
        password=form.password.data
        data = {
                "name":name,
                "password":password
        }
        with open('user_info.json', 'w') as f:
             f.write(json.dumps(data))
        return redirect('/upload')
    return render_template('login.html', title='Sign in', form=form)

@app.route('/upload',methods=['GET','POST'])
def upload():
    form=UploadForm()
    if form.validate_on_submit():
        f = form.upload.data
        filename = secure_filename(f.filename)
        f.save(os.path.join('uploads/', filename))
        
        return redirect('/yml')
    return render_template('upload.html', tiile='Upload File', form = form)

@app.route('/yml', methods=['GET'])
def yml():
   return send_from_directory(directory='/home/grimpoteuthis/app/xls2xml_bayes', filename='res.yml')

if __name__ == "__main__" :
    app.run(host='0.0.0.0')
