import cv2
import face_recognition
import pickle
import os

DATA_FILE = "faces.pkl"

if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "rb") as f:
        known_faces = pickle.load(f)
else:
    print("No face data found. Run capture_face.py first.")
    exit()

known_encodings = known_faces["encodings"]
known_names = known_faces["names"]

video_capture = cv2.VideoCapture(1)

while True:
    ret, frame = video_capture.read()
    if not ret:
        break

    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)
    face_landmarks_list = face_recognition.face_landmarks(frame)

    for face_encoding, (top, right, bottom, left), face_landmarks in zip(face_encodings, face_locations, face_landmarks_list):
        matches = face_recognition.compare_faces(known_encodings, face_encoding)
        name = "Unknown"
        color = (0, 0, 255) 

        if True in matches:
            best_match_index = matches.index(True)
            name = known_names[best_match_index]
            color = (0, 255, 0)  

        for feature, points in face_landmarks.items():
            for i in range(len(points) - 1):
                cv2.line(frame, points[i], points[i + 1], (255, 0, 0), 1)

        cv2.rectangle(frame, (left, top), (right, bottom), color, 2)

        cv2.rectangle(frame, (left, bottom + 20), (right, bottom), color, cv2.FILLED)
        cv2.putText(frame, name, (left + 5, bottom + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    cv2.imshow("Face Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
