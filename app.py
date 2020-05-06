from flask import Flask, render_template, request

# instantiate the object of the class flask
app = Flask(__name__)

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

        # rendering the success page
        return render_template('success.html')


# the script is being executed
if __name__ == "__main__":
    app.run(debug=True)
