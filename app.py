from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func
from werkzeug.utils import secure_filename

# instantiate the object of the class flask
app = Flask(__name__)
# configure the connection to the database
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost/height_collector'

# heroku database creditentials
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://gbidvfwfujdfxa:2b37f7a710abad85e0b15903c3cc14648268931d2db9ddbdc78ed0f1f8869fe3@ec2-54-81-37-115.compute-1.amazonaws.com:5432/da06m423gtjbtf'
# creating an SQL alchemy object for Flask app
db = SQLAlchemy(app)


class Data(db.Model):  # model from the sqlalchemy
    """ Class that hundle the database"""
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key=True)
    email_ = db.Column(db.String(120), unique=True)
    height_ = db.Column(db.Integer)

    def __init__(self, email_, height_):
        # constructor
        self.email_ = email_
        self.height_ = height_


# creating our first route as home page
@app.route('/')
def index():
    # rendering the index page
    return render_template('index.html')


@app.route('/success', methods=['POST'])  # To post the data to the server
def success():
    # processing data if request is post
    if request.method == 'POST':
        file = request.files['file']
        # saving the file into our directory by adding a certain level of security
        file.save(secure_filename("uploaded"+file.filename))
        with open("uploaded"+file.filename, "a") as f:
            f.write("Just got pissed")

        # rendering the success page
        return render_template('index.html', btn="download.html")


# the script is being executed
if __name__ == "__main__":
    app.run(debug=True)
