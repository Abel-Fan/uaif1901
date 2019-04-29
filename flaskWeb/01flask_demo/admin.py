from flask import Blueprint,abort,render_template,request
from dbcon import db,cursor

admin2 = Blueprint("admin2",__name__,url_prefix="/admin",static_folder="./static/admin")

@admin2.route("/",methods=['GET'])
def index():
    return render_template("admin/index.html")

@admin2.route("/addpj.html",methods=['GET','POST'])
def addpj():
    if request.method == "GET":
        return render_template("admin/addpj.html")
    elif request.method == "POST":
        name = request.form['name']
        img = request.form['img']
        info = request.form['info']

        try:
            cursor.execute("insert into produces (name,img,info) values ('?','?','?')",(name,img,info))
            db.commit()
        except:
            return "error"
        return 'ok'
    else:
        abort(404)