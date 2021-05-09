from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '22ab2d75d7ed9d73f7f38b7a'
db = SQLAlchemy(app)

from market import routes


# if __name__ == "__main__":
#     app.run(debug = True)