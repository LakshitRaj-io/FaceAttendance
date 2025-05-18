import cv2
import face_recognition
import os
import csv
from datetime import datetime

KNOWN_DIR = 'known_faces'
CSV_FILE = 'attendance.csv'

def load_known_faces():
    known_encodings = []
    known_names = []
    for name in os.listdir(KNOWN_DIR):
        path = os.path.join(KNOWN_DIR, name)
        img = face_recognition.load_image_file(path)
        encoding = face_recognition.face_encodings(img)[0]
        known_encodings.append(encoding)
        known_names.append(os.path.splitext(name)[0])
    return known_encodings, known_names

def mark_attendance(name):
    with open(CSV_FILE, 'a+', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([name, datetime.now().strftime("%Y-%m-%d %H:%M:%S")])

def recognize_faces():
    known_encodings, known_names = load_known_faces()
    cap = cv2.VideoCapture(0)
    print("[INFO] Starting camera...")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        boxes = face_recognition.face_locations(rgb)
        encodings = face_recognition.face_encodings(rgb, boxes)

        for encoding, box in zip(encodings, boxes):
            matches = face_recognition.compare_faces(known_encodings, encoding)
            name = "Unknown"

            if True in matches:
                match_index = matches.index(True)
                name = known_names[match_index]
                mark_attendance(name)

            top, right, bottom, left = box
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)

        cv2.imshow("Attendance", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    recognize_faces()
