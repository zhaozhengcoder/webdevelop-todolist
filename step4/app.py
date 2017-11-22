"""
step 1 : 实现一个登录的页面
关键点：  使用wtf from 实现登录的表单

step 2 ：使用sqlalchemy 实现了基本的查询todolist里面的内容
关键点：
1. 如果不熟悉orm，可能要先看一下sqlalchemy
2. 然后看一下flask-sqlalchemy 这个东西 ，熟悉一下基本的语法


step 3：
1. 修改的一部分的index页面，是index的页面更加完整一点
2. 修改了一部分的登录界面的登录逻辑
3. 实现了登录页面的消息闪现 flash ： http://docs.jinkan.org/docs/flask/patterns/flashing.html

step 4 :
1. flask_login 模块的使用,只有登录之后才能访问某些页面（如果不使用flask_login,可以使用session来解决这个问题）

"""
from flask import (Flask, render_template, redirect, url_for, request, flash)
import forms
import config
from ext import db,login_manager
from models import TodoList, User
#登录权限管理的扩展
from flask_login import login_required, login_user, logout_user, current_user

app = Flask(__name__)
app.secret_key=config.SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:root@127.0.0.1/test"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db.init_app(app)

#flask_login,注意login_manager在ext文件里面定义
login_manager.init_app(app)
login_manager.login_view = "login"

#flask_login
@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=int(user_id)).first()



@app.route('/', methods=['GET', 'POST'])
@login_required
def index():
    return "<h1> index </h1>"

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = forms.LoginFrom()
    if request.method == 'GET':
        return render_template("login.html",form=form)
    else:
        username=request.form['username']
        password=request.form['password']
        user = User.query.filter_by(username=request.form['username'], password=request.form['password']).first()
        if user:
            #flask_login
            login_user(user)
            flash('you have logged in!')
            return redirect(url_for('showtodolist' ))
        else:
            flash("error password !")
            return render_template("login.html",form=form)
        #return "<h1>home post method </h1> <h2> post data is {} and {}".format(username,password)


@app.route('/show', methods=['GET', 'POST'])
@login_required
def showtodolist():
    if request.method=="GET":
        todolists =TodoList.query.all()
        return render_template("index.html",todolists=todolists)
    else:
        return "<h1> method post </h1>"


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('you have logout!')
    return redirect(url_for('login'))


if __name__=="__main__":
    app.run(debug=True,port=5002)