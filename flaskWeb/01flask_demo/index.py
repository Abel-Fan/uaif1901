from flask import Blueprint,abort,render_template

index1 = Blueprint("index",__name__,url_prefix="/")

@index1.route("/<pagename>.html",methods=["GET"])
def index(pagename):
    data={}
    if pagename=="index" or pagename=='':
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
    elif pagename == 'protect':
        pass
    elif pagename == 'find':
        pass
    elif pagename == "about":
        pass
    elif pagename == "contect":
        pass
    else:
       abort(404)

    return render_template("index/%s.html"%pagename,data=data)