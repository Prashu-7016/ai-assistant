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
    file = request.data
    with open(os.path.join(UPLOAD_FOLDER, 'latest.pdf'), 'wb') as f:
        f.write(file)
    return 'Upload successful', 200

if __name__ == '__main__':
    app.run(debug=True)