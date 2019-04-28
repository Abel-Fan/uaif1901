from flask import Flask,render_template,request

app = Flask(__name__)


@app.route("/<pagename>.html",methods=['GET'])
def index(pagename):
    data={}
    if pagename=="index":
        data = {
            "tuijian":[
                {'title': "汉服花莲", 'imgurl': "static/img/hanfu01.jpg", 'link':""},
                {'title': "汉服花莲", 'imgurl': "static/img/hanfu01.jpg", 'link': ""},
                {'title': "汉服花莲", 'imgurl': "static/img/hanfu01.jpg", 'link': ""},

            ],
            "pinpai":[
                {'img':"static/img/guo01.jpg",'name':"Smile晴天",'info':"衣服面料超舒服 买之前还考虑要不要退 买回来感觉太好 这么好的衣服都舍不得退 ",'link':""},
                {'img': "static/img/guo01.jpg", 'name': "Smile晴天", 'info': "衣服面料超舒服 买之前还考虑要不要退 买回来感觉太好 这么好的衣服都舍不得退 ",
                 'link': ""},
                {'img': "static/img/guo01.jpg", 'name': "Smile晴天", 'info': "衣服面料超舒服 买之前还考虑要不要退 买回来感觉太好 这么好的衣服都舍不得退 ",
                 'link': ""},
                {'img': "static/img/guo01.jpg", 'name': "Smile晴天", 'info': "衣服面料超舒服 买之前还考虑要不要退 买回来感觉太好 这么好的衣服都舍不得退 ",
                 'link': ""},
                {'img': "static/img/guo01.jpg", 'name': "Smile晴天", 'info': "衣服面料超舒服 买之前还考虑要不要退 买回来感觉太好 这么好的衣服都舍不得退 ",
                 'link': ""},
                {'img': "static/img/guo01.jpg", 'name': "Smile晴天", 'info': "衣服面料超舒服 买之前还考虑要不要退 买回来感觉太好 这么好的衣服都舍不得退 ",
                 'link': ""},
            ],
            "remen":[
                {
                    'img':[],
                    'title':"",
                    'info':"",
                    'link':''
                 },
            ]
        }
    elif pagename == '':
        pass
    return render_template("index/%s.html"%pagename,data=data)



if __name__ =="__main__":
    app.run(debug=True,host="192.168.32.102",port='8000')