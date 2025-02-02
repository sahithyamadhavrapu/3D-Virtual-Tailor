from flask import Flask, request, jsonify
import os
from measurements import get_body_measurements

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route('/upload', methods=['POST'])
def upload_image():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files["file"]
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(file_path)

    measurements = get_body_measurements(file_path)
    if not measurements:
        return jsonify({"error": "Body not detected"}), 400

    return jsonify(measurements)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
