import cv2
import mediapipe as mp
import numpy as np

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

def get_body_measurements(image_path):
    image = cv2.imread(image_path)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = pose.process(image_rgb)

    if not results.pose_landmarks:
        return None

    landmarks = results.pose_landmarks.landmark
    shoulder_width = np.linalg.norm([
        landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x - 
        landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x
    ])
    height = np.linalg.norm([
        landmarks[mp_pose.PoseLandmark.NOSE.value].y - 
        landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y
    ])
    
    return {
        "shoulder_width": shoulder_width,
        "height": height
    }
