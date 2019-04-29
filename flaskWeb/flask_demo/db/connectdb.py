import pymysql
from flaskWeb.flask_demo.settings import HOST,PORT,USER,PASSWORD,DB

database = pymysql.connect(
    host=HOST,
    port = PORT,
    user = USER,
    password = PASSWORD,
    db = DB
)

cursor = database.cursor()