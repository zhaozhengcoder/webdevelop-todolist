"""
step 1 : 实现一个登录的页面
关键点：  使用wtf from 实现登录的表单

step 2 ：使用sqlalchemy 实现了基本的查询todolist里面的内容
关键点：
1. 如果不熟悉orm，可能要先看一下sqlalchemy
2. 然后看一下flask-sqlalchemy 这个东西 ，熟悉一下基本的语法

官网文档：http://www.pythondoc.com/flask-sqlalchemy/  
然后看完官方文档里面的快速入门
"""
from flask import (Flask, render_template, redirect, url_for, request, flash)
import forms
import config

from ext import db
from models import TodoList, User


app = Flask(__name__)
app.secret_key=config.SECRET_KEY


app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:root@127.0.0.1/test"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db.init_app(app)


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        form = forms.LoginFrom()
        return render_template("login.html",form=form)
    else:
        username=request.form['username']
        password=request.form['password']
        return "<h1>home post method </h1> <h2> post data is {} and {}".format(username,password)


@app.route('/show', methods=['GET', 'POST'])
def showtodolist():
    if request.method=="GET":
        todolists =TodoList.query.all()
        return render_template("index.html",todolists=todolists)
    else:
        return "<h1> method post </h1>"

if __name__=="__main__":
    app.run(debug=True,port=5002)