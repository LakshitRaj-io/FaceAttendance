# 👁️ Face Recognition Attendance System

This is a Python-based Face Recognition Attendance System that automatically records the attendance of known individuals using webcam video input. It utilizes **OpenCV** and **face_recognition** for facial detection and recognition.

> ✅ Developed with assistance from [ChatGPT by OpenAI](https://openai.com/chatgpt)

---

## 📸 Features

- Real-time face recognition using a webcam
- Auto-logging of attendance with timestamp into a CSV file
- Supports adding new faces by simply placing images in the `known_faces/` folder
- Lightweight and fast, ideal for classroom or lab environments

---

## 🛠️ Tech Stack

- **Language:** Python 3
- **Libraries:** 
  - [`face_recognition`](https://github.com/ageitgey/face_recognition)
  - `opencv-python`
- **Output Format:** `.csv` for attendance logs

---

## 📁 Project Structure

FaceRecognitionAttendance/
├── recognize_face.py # Main script
├── requirements.txt # Required libraries
├── attendance.csv # Auto-generated attendance log
└── known_faces/ # Folder with known face images (e.g., alice.jpg)

## ✅ How to Run

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
Add known faces

Put JPG/PNG images in known_faces/

File name should be the person’s name (e.g., john_doe.jpg)

Run the script

bash
Copy
Edit
python recognize_face.py
Quit

Press Q to stop the webcam

📌 Output
Attendance is logged to attendance.csv like this:

yaml
Copy
Edit
Name, Timestamp
Alice, 2025-05-18 10:03:45
Bob, 2025-05-18 10:05:12
