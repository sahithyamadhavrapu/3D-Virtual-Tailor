# 🧠 Backend - Body Measurement (OpenCV + MediaPipe + Flask)

This backend module is responsible for:

- Accepting full-body image uploads and user-provided height
- Extracting body measurements (shoulders, hips, height) using MediaPipe
- Normalizing pixel distances to real-world cm
- Returning measurements as JSON
- Saving output to `model_generation/inputs/measurements.json`

---

## 🔧 Technologies Used

- Python
- Flask
- OpenCV
- MediaPipe

---

## 📥 API Endpoint

**POST /upload**

| Field | Type | Description |
|-------|------|-------------|
| `image` | File | Full-body image (JPEG/PNG) |
| `height` | Number | User's height in centimeters |

Returns:
```json
{
  "shoulder_width_cm": 44.67,
  "hip_width_cm": 38.55,
  "user_height_cm": 160.0
}

How to Run the Backend:

cd backend
pip install -r requirements.txt
python app.py

The Flask API will start on http://localhost:5000/.

Folder Structure:
backend/
├── app.py                  ← Flask API server
├── measurement.py          ← OpenCV + MediaPipe logic for measurement
├── measurements.json       ← Output (auto-generated from user input)
└── README.md               ← This file (module-level documentation)

Output Usage:
The measurements extracted by this backend are saved in measurements.json and used by the 3D modeling teammate to create an avatar in MakeHuman and Blender.