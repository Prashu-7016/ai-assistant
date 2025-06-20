from flask import Flask, request, render_template
import os

app = Flask(__name__)

UPLOAD_FOLDER = "static/snapshots"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file part', 400

    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400

    save_path = os.path.join(UPLOAD_FOLDER, 'sheet_snapshot.pdf')
    file.save(save_path)
    print(f"Saved file to {save_path}")
    return 'Uploaded', 200
