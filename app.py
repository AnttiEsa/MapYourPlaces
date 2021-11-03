from flask import Flask, render_template, request, redirect
from database.operations import insert_data
from api import get_json
from database.operations import truncateTable, getRows, columnError
import os

app = Flask(__name__)

# Google API key

APP_KEY = os.environ['GOOGLE_MAPS_API_KEY']

"""TO DO APP CONFIG FILE"""

UPLOAD_FOLDER = "c:\\bootcamp\YWBD"
ALLOWED_EXTENSIONS = {'csv'}

app.config['CSV_UPLOADS'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/table/')
def index():
    return render_template('table.html')

@app.route('/maps/', methods=["GET", "POST"])
def maps():
    fileErrors = {"columnNameError": 0, "fileTypeError": 0}
    if request.method == "POST":
        
        if request.files:
            csv = request.files["formFile"]
            
            if csv and allowed_file(csv.filename):               
                csv.save(os.path.join(app.config['CSV_UPLOADS'], "data.csv"))
                if(columnError() == False):
                    truncateTable()
                    getRows()
                else:
                    fileErrors["columnNameError"] = 1
                    return render_template('maps.html', columnNameError = fileErrors["columnNameError"], YOUR_API_KEY = APP_KEY)

            return redirect(request.url)
        return render_template('maps.html', columnNameError = fileErrors["columnNameError"], YOUR_API_KEY = APP_KEY)
    else:
        return render_template('maps.html', columnNameError = fileErrors["columnNameError"], YOUR_API_KEY = APP_KEY)

    


@app.route('/api/all')
def api():
    return get_json()

if __name__ == "__main__":
    app.debug = True
    app.run(port=5001)