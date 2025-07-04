# 🧵 3D Virtual Tailor – Full Stack Team Project

A web-based application that allows users to upload a full-body image, calculates body measurements using computer vision, and generates a realistic 3D human avatar for visualizing clothing fit.



## 👥 Team Members & Roles

| Name                  | Role                      | Responsibilities                                                          |
|-------------------------------------------------------------------------------------------------------------------------------|
| M. Lakshmi Sahithya   | Backend (CV + Flask)      | Measurement extraction with OpenCV & MediaPipe, normalization, Flask  API |
| Lahari                | Frontend Developer (React)| React UI for image upload & height input, integration with backend API    |
| Praneetha             | 3D Modeling (WIP)         | Using MakeHuman + Blender to generate avatar from measurements (ongoing)  |


## 🔁 Project Workflow

User (Frontend) ─▶ Uploads Image + Height
              ▼
Backend ─▶ Uses OpenCV + MediaPipe to extract measurements
              ▼
Measurements saved in JSON format
              ▼
3D Modeler ─▶ Builds realistic avatar using MakeHuman & Blender (Work In Progress)


## 🛠 Tech Stack

| Layer       | Technology                      |
|-------------|---------------------------------|
| Frontend    | React.js, Axios                 |
| Backend     | Flask, Python, OpenCV, MediaPipe|
| 3D Modeling | MakeHuman, Blender (WIP)        |


## 📁 Project Structure

3D-Virtual-Tailor/
├── backend/ ← Flask + OpenCV backend (Sahithya)
│ ├── app.py ← Image + height handler
│ ├── measurement.py ← Body landmark and measurement logic
│ └── measurements.json ← Output used for 3D modeling
│ └── README.md
├── frontend/ ← React frontend (Friend 1)
│ └── src/App.js ← Upload & input UI
│ └── README.md
├── model_generation/ ← 3D modeling files (Friend 2 - In Progress)
│ ├── inputs/ ← Auto-generated measurement file
│ ├── outputs/ ← Final avatar renders (WIP)
│ └── README.md
└── README.md ← Full project overview (this file)


## ✅ Current Status:

- [x] React UI for image upload and height input
- [x] OpenCV + MediaPipe backend for measurement extraction
- [x] Normalization of pixel distances to centimeters
- [x] JSON output saved to shared folder
- [ ] 3D avatar generation in Blender *(Work In Progress)*

## 🚀 How to Run the Project Locally:

## 📦 Backend (Flask):
cd backend
pip install -r requirements.txt
python app.py
The backend runs at http://localhost:5000

## 🖼 Frontend (React):
cd frontend
npm install
npm start
The frontend runs at http://localhost:3000

## 📤 Output Preview (Coming soon):
✅ measurements.json → stored in model_generation/inputs/

🖼 Final avatar render will be placed in model_generation/outputs/avatar_render.png

## 📋 Note to Reviewers:
This is a team-based full-stack and AI-integrated project.
The backend and frontend are fully functional. The 3D modeling portion is still in progress and will use the normalized measurements from the backend to generate realistic avatars in Blender.

## 🙌 Thank You
This project simulates real-world team collaboration between frontend, backend, and ML/3D developers.