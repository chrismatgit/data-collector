from flask import Flask, render_template, request, send_file
from geopy.geocoders import Nominatim
import pandas
from werkzeug.utils import secure_filename

# instantiate the object of the class flask
app = Flask(__name__)

# creating our first route as home page
@app.route('/')
def index():
    # rendering the index page
    return render_template('index.html', btn="")


# To post the data to the server and draw the table
@app.route('/success-tab', methods=['POST'])
def success_tab():
    # processing data if request is post
    global file
    if request.method == 'POST':
        file = request.files['file']
        try:
            df = pandas.read_csv(file)
            gc = Nominatim(scheme='http')
            df['coordinates'] = df['Address'].apply(gc.geocode)
            df['Latitude'] = df['coordinates'].apply(
                lambda x: x.latitude if x != None else None)
            df['Longitude'] = df['coordinates'].apply(
                lambda x: x.longitude if x != None else None)
            df = df.drop("coordinates", 1)
            # create the filename and formatted it by adding the datetime on it
            filename = datetime.datetime.now().strftime(
                "sample_files/%Y-%m-%d-%H-%M-%S-%f"+".csv")
            df.to_csv(filename, index=None)
            return render_template("index.html", text=df.to_html(), btn='download.html')
        except Exception as e:
            return render_template("index.html", text=str(e), btn="")

        # rendering the success page
        return render_template('index.html', btn="download.html")


@app.route('/download-file/')  # route to download the csv file
def download():
    # function to download the file
    return send_file(filename, attachment_filename="yourfile.csv", as_attachment=True)


# the script is being executed
if __name__ == "__main__":
    app.run(debug=True)
