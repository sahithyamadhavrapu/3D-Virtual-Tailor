import cv2
import mediapipe as mp
import math

mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=True)

def calc_distance(p1, p2, width, height):
    x1, y1 = int(p1.x * width), int(p1.y * height)
    x2, y2 = int(p2.x * width), int(p2.y * height)
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def process_image(image_path, known_height_cm):
    image = cv2.imread(image_path)
    height, width, _ = image.shape

    results = pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    if not results.pose_landmarks:
        return {"error": "Pose landmarks not detected"}

    landmarks = results.pose_landmarks.landmark

    # Calculate measurements
    shoulder_px = calc_distance(
        landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER],
        landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER],
        width, height
    )

    hip_px = calc_distance(
        landmarks[mp_pose.PoseLandmark.LEFT_HIP],
        landmarks[mp_pose.PoseLandmark.RIGHT_HIP],
        width, height
    )

    height_px = calc_distance(
        landmarks[mp_pose.PoseLandmark.NOSE],
        landmarks[mp_pose.PoseLandmark.LEFT_ANKLE],
        width, height
    )

    # Normalize to cm
    pixel_per_cm = height_px / known_height_cm
    shoulder_cm = shoulder_px / pixel_per_cm
    hip_cm = hip_px / pixel_per_cm

    return {
        "shoulder_width_cm": round(shoulder_cm, 2),
        "hip_width_cm": round(hip_cm, 2),
        "user_height_cm": known_height_cm
    }
