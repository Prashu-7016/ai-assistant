from flask import Flask, request, render_template
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static/snapshots'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    try:
        filename = 'sheet_snapshot.pdf'
        filepath = os.path.join(UPLOAD_FOLDER, filename)

        with open(filepath, 'wb') as f:
            f.write(request.data)

        return 'Uploaded', 200
    except Exception as e:
        return f'Error: {str(e)}', 500
