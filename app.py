from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'srt' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['srt']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    # Here you can add actual translation/processing logic
    # For now, just return success
    return jsonify({"message": "File uploaded", "filename": filename})

import os

port = int(os.environ.get('PORT', 10000))
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
