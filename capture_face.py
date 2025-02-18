import cv2
import face_recognition
import pickle
import os

DATA_FILE = "faces.pkl"

if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "rb") as f:
        known_faces = pickle.load(f)
else:
    known_faces = {"encodings": [], "names": []}
    with open(DATA_FILE, "wb") as f:
        pickle.dump(known_faces, f)

name = input("Enter the name of the person: ")

video_capture = cv2.VideoCapture(0)

print("Press 's' to save the detected face or 'q' to quit.")

while True:
    ret, frame = video_capture.read()
    if not ret:
        break

    face_locations = face_recognition.face_locations(frame)
    face_landmarks_list = face_recognition.face_landmarks(frame)

    if face_locations:
        for (top, right, bottom, left), face_landmarks in zip(face_locations, face_landmarks_list):
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            for feature, points in face_landmarks.items():
                for i in range(len(points) - 1):
                    cv2.line(frame, points[i], points[i + 1], (255, 0, 0), 1)

    cv2.imshow("Capture Face", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('s') and face_locations:
        face_encodings = face_recognition.face_encodings(frame, face_locations)
        if face_encodings:
            known_faces["encodings"].append(face_encodings[0])
            known_faces["names"].append(name)

            with open(DATA_FILE, "wb") as f:
                pickle.dump(known_faces, f)

            print(f"Face of '{name}' saved successfully!")
            break
    elif key == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
