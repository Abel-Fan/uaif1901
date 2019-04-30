from flask import Blueprint,render_template,session,request,redirect,jsonify
import json
import datetime
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
        sql = "select id,username,auth from users"
        cursor.execute(sql)
        users = cursor.fetchall()
        print(users)
        """
        (
            (1,horns,auth),
        )
        """
        return render_template(
            "admin/adduser.html",
            admin_static=ADMIN_STATIC,
            users=users)

    elif request.method == "POST":
       password = request.form.get('password',None)
       password1 = request.form.get('password1',None)
       username = request.form.get('username',None)
       auth = request.form.get('auth',None)
       print(username,password,password1,auth)
       if password==None or password1==None or username== None or auth ==None or password!=password1:
           return "no"
       else:
           sql = "insert into users (username,password,auth,ctime) values (%s,%s,%s,%s)"
           try:
               cursor.execute(sql,(username,password,auth, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
               database.commit()
           except:
               return "no"
           return "ok"

@adminblue.route("/authusername",methods=['POST'])
@authlogin
def authusername():
    username = request.form.get("username",None)
    if username:
        sql = "select username from users where username=%s"
        cursor.execute(sql,(username))
        res = cursor.fetchall()
        if len(res)>0:
            return jsonify({'code':'error','info':"用户名已存在"})
        else:
            return jsonify({'code':'ok'})
    return jsonify({'code':'error','info':"参数不对应"})

@adminblue.route("/addpj.html",methods=['GET','POST'])
@authlogin
def addpj():
    return render_template("/admin/addpj.html")

@adminblue.route("/loginout",methods=['GET'])
@authlogin
def loginout():
    session.pop('username',None)
    # 重定向
    return redirect("login")