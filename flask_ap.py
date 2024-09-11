import os
from flask import Flask, flash, make_response, request
from werkzeug.utils import secure_filename


def allowed_file(filename):
    return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in {'json'}


app = Flask(__name__)

@app.route("/", methods=['GET'])
def ar_app():
    return make_response("my app v0.01", 200)

@app.route('/update_data', methods=['POST'])
def upload_file():
    # check if the post request has the file part
    if 'file' not in request.files:
        flash('No file part')
        return make_response('bad_request', 400)
    file = request.files['file']
    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == '':
        flash('No selected file')
        return make_response('bad_request', 400)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join('/home/za00ko/mysite/data', filename))
        return make_response('', 200)
