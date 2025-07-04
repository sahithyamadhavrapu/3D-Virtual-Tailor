from flask import Flask, request, jsonify
from measurement import process_image
import json
import os

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_image():
    image = request.files['image']
    image.save('user_image.jpg')

    known_height = float(request.form.get('height'))
    measurements = process_image('user_image.jpg', known_height)

    # ✅ Save JSON to file (your final step)
    with open("backend/measurements.json", "w") as f:
        json.dump(measurements, f, indent=4)

    os.makedirs("model_generation/inputs", exist_ok=True)
    with open("model_generation/inputs/measurements.json", "w") as f:
        json.dump(measurements, f, indent=4)

    return jsonify(measurements)

if __name__ == '__main__':
    app.run(debug=True)
