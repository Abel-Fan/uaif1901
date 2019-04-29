from flask import Blueprint,render_template
from flaskWeb.flask_demo.db.connectdb import database,cursor
from flaskWeb.flask_demo.settings import INDEX_STATIC

indexblue = Blueprint("index",__name__,url_prefix="/")

@indexblue.route("/",methods=["GET"])
def index():
    data = {}
    sql = "select * from produces limit 3"
    cursor.execute(sql)  # 执行sql语句
    tuijians = cursor.fetchall()    # 获取数据
    data['tuijian'] = tuijians

    return render_template("index/index.html",data=data,index_static=INDEX_STATIC)

@indexblue.route("/<pagename>.html",methods=["GET"])
def getpage(pagename):
    return render_template("index/%s.html"%pagename)