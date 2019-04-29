from flask import Flask,render_template,request,abort
from index import index1
from admin import admin2
app = Flask(__name__)

app.register_blueprint(index1)
app.register_blueprint(admin2)


if __name__ =="__main__":
    app.run(debug=True)