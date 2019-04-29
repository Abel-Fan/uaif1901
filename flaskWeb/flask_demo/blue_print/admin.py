from flask import Blueprint,render_template

adminblue = Blueprint("adminblue",__name__,url_prefix="/admin")

@adminblue.route("/",methods=['GET'])
def admin():
    return render_template("admin/index.html")