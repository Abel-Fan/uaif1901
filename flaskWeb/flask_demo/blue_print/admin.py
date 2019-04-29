from flask import Blueprint,render_template,session,request,redirect
import json
from flaskWeb.flask_demo.settings import ADMIN_STATIC
from flaskWeb.flask_demo.db.connectdb import cursor,database
from flaskWeb.flask_demo.uli.myuli import authlogin
adminblue = Blueprint("adminblue",__name__,url_prefix="/admin")



@adminblue.route("/login",methods=['GET',"POST"])
def login():
    if request.method == "GET":
        return render_template("admin/login.html",admin_static=ADMIN_STATIC)
    elif request.method == "POST":
        username = request.form.get("username",None)
        password = request.form.get('password',None)
        if username and password:
            cursor.execute("select * from users where username=%s",username)
            res = cursor.fetchone()
            if res:
                if res[2]== password:
                    session['username'] = username
                    return json.dumps({'code':'ok','info':'登录成功'})
                else:
                    return json.dumps({'code': 'error', 'info': '密码不正确'})
            else:
                return json.dumps({'code':'error','info':'没有此用户'})
        else:
            return json.dumps({'code':'error','info':'username,password 为空'})


    # 登录流程
    # ajax post
    # 判断是否username password 是否为空
    # 判断是否username 存在
    # 判断是否password正确



@adminblue.route("/",methods=['GET'])
@authlogin
def admin():
    return render_template("admin/index.html")


@adminblue.route("/adduser.html",methods=['GET','POST'])
@authlogin
def adduser():
    if request.method == "GET":
        return render_template("admin/adduser.html")
    elif request.method == "POST":
        return render_template("admin/adduser.html")