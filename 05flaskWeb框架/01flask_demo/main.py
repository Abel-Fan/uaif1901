from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/",methods=['GET'])
def index():
    print(dir(request))
    print("method",request.method)

    con = render_template("index/index.html")
    return con


if __name__ =="__main__":
    app.run(debug=True,host="192.168.32.102",port='8000')