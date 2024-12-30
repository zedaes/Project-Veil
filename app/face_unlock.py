import cv2
from utils.face_recognition_utils import load_authorized_faces, compare_faces
from utils.file_utils import log_attempt
from app.config import CONFIG

def capture_image(temp_image_path):
    """Capture an image from the webcam."""
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(temp_image_path, frame)
    cap.release()

def face_unlock():
    """Unlock the laptop if face is recognized."""
    print("Starting face recognition...")
    authorized_encodings = load_authorized_faces(CONFIG["AUTHORIZED_FACES_DIR"])
    capture_image(CONFIG["TEMP_IMAGE"])
    success = compare_faces(authorized_encodings, CONFIG["TEMP_IMAGE"])
    log_attempt(CONFIG["LOG_DIR"], success)
    if success:
        print("Access Granted! Welcome!")
        # Add further actions, like opening a file
    else:
        print("Access Denied! Face not recognized.")
