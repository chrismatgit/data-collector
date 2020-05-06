from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

# instantiate the object of the class flask
app = Flask(__name__)
# configure the connection to the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost/height_collector'
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
        email = request.form['email_name']
        height = request.form['height_name']
        print(email, height)
        # checking the duplication
        if db.session.query(Data).filter(Data.email_ == email).count() == 0:

            # add rows with sqlalchemy
            data = Data(email, height)
            db.session.add(data)
            db.session.commit()

            # rendering the success page
            return render_template('success.html')
        return render_template('index.html',
                               text="Seems like we've got something from that email address already")


# the script is being executed
if __name__ == "__main__":
    app.run(debug=True)
