from flask import Blueprint,render_template
from flaskWeb.flask_demo.db.connectdb import database,cursor

indexblue = Blueprint("index",__name__,url_prefix="/")

@indexblue.route("/",methods=["GET"])
def index():
    data = {}
    sql = "select * from produces limit 3"
    cursor.execute(sql)  # 执行sql语句
    tuijians = cursor.fetchall()    # 获取数据
    data['tuijian'] = tuijians

    return render_template("index/index.html",data=data)