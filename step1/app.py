"""
step 1 : 实现一个登录的页面
关键点：  使用wtf from 实现登录的表单
"""
from flask import (Flask, render_template, redirect, url_for, request, flash)
import forms
import config


app = Flask(__name__)
app.secret_key=config.SECRET_KEY

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        form = forms.LoginFrom()
        return render_template("index.html",form=form)
    else:
        username=request.form['username']
        password=request.form['password']
        return "<h1>home post method </h1> <h2> post data is {} and {}".format(username,password)


if __name__=="__main__":
    app.run(debug=True,port=5001)