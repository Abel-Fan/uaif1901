from flask import Flask
from flaskWeb.flask_demo.blue_print.index import indexblue
from flaskWeb.flask_demo.blue_print.admin import adminblue

app = Flask(__name__)
app.register_blueprint(indexblue)
app.register_blueprint(adminblue)


if __name__ == "__main__":
    app.run(debug=True)
