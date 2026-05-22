# Emotion & Age Vision AI

A real-time AI desktop application that detects facial emotions and estimates age using a webcam feed. The system also provides live voice feedback based on detected emotions.

---

## Features

-  Real-time emotion detection (happy, sad, angry, neutral, etc.)
-  Age estimation using deep learning
-  Live webcam video processing with OpenCV
-  AI-powered analysis using DeepFace
-  Modern GUI built with CustomTkinter
-  Text-to-speech feedback using pyttsx3
-  Multi-threaded processing for smooth performance

---

## Technologies Used

- Python 3.10+
- OpenCV
- DeepFace
- TensorFlow
- Pillow (PIL)
- CustomTkinter
- pyttsx3
- threading

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/emotion-age-vision.git
cd emotion-age-vision

2. Create virtual environment
python -m venv .venv
.venv\Scripts\activate   # Windows

3. Install dependencies
pip install -r requirements.txt
📌 Run the project
python test_felling.py

📁 Project Structure
emotion-age-vision/
│
├── test_felling.py
├── requirements.txt
└── README.md

⚠️ Notes
Requires webcam access
First run may download large AI models (DeepFace/TensorFlow)
Performance depends on CPU/GPU
If pyttsx3 fails, install:
pip install pyttsx3

 Future Improvements
Add gender detection
Add emotion timeline graph
Improve UI animations
Replace DeepFace with lightweight model for faster inference
Add GPU acceleration support

 Author

Developed by imlouli abderrahmane

📜 License

This project is open-source for educational purposes.