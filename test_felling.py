import cv2
import time
import threading
import customtkinter
from deepface import DeepFace
from PIL import Image
import pyttsx3

# ==============================
#        Setup voice
# ==============================
def speak(text):
    def run():
        try:
            engine = pyttsx3.init()
            engine.setProperty('rate', 155)
            voices = engine.getProperty('voices')
            if voices:
                engine.setProperty('voice', voices[0].id)
            engine.say(text)
            engine.runAndWait()
            engine.stop()
        except Exception as e:
            print("❌ sound error : ", e)
    threading.Thread(target=run, daemon=True).start()

# ==============================
#       Setup UI
# ==============================
app = customtkinter.CTk()
app.title("Emotion & Age Vision")
app.geometry("1100x750")
app.configure(fg_color="#0b0b0b")

# Main title
title_label = customtkinter.CTkLabel(app, text="Emotion & Age Vision",
                                     font=("Arial Black", 36),
                                     text_color="#FFD700")
title_label.place(x=200, y=60)

# Video display area
video_label = customtkinter.CTkLabel(app, text="")
video_label.place(x=120, y=180)

# ==============================
#       Setup camera
# ==============================
cap = cv2.VideoCapture(0)
emotion = "..."
age = "..."
last_analysis_time = 0
running = True

# ==============================
#        Smart analysis
# ==============================
def analyze_stream():
    global emotion, age, last_analysis_time, running
    while running:
        ret, frame = cap.read()
        if not ret:
            continue

        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Analyze only once per second
        if time.time() - last_analysis_time > 1:
            try:
                results = DeepFace.analyze(rgb, actions=['age', 'emotion'], enforce_detection=False)
                if isinstance(results, list):
                    results = results[0]

                emotion = results.get('dominant_emotion', 'Unknown')
                age = str(results.get('age', '?'))

                # Messages in English
                messages = {
                    "happy": "you look happy today",
                    "sad": "you look sad , don't worry every thing will be okay",
                    "angry": "are you angry ? have a deep breath",
                    "surprise": "you look surprised",
                    "fear": " is there something make you fear ",
                    "neutral": "you look calm "
                }

                # Voice prompt
                if emotion in messages:
                    text = f"{messages[emotion]}   it looks like u are  {age} year old."
                    speak(text)

            except Exception as e:
                print("⚠️ error during the analyse:", e)
                emotion = "No face"
                age = "..."

            last_analysis_time = time.time()

        # Draw results on the video
        cv2.putText(frame, f"Emotion: {emotion}", (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 100), 2)
        cv2.putText(frame, f"Age: {age}", (30, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 200, 255), 2)

        # Convert the image for the UI
        img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        imgtk = customtkinter.CTkImage(light_image=img, dark_image=img, size=(850, 480))
        video_label.configure(image=imgtk)
        video_label.image = imgtk
# ==============================
#      stop and exit button
# ==============================
def stop_app():
    global running
    running = False
    cap.release()
    app.destroy()

stop_button = customtkinter.CTkButton(app, text="🔴  stop the program",
                                      fg_color="#C9302C", hover_color="#A02020",
                                      font=("Arial", 20, "bold"), command=stop_app)
stop_button.place(x=450, y=700)

# ==============================
#         start analysing 
# ==============================
threading.Thread(target=analyze_stream, daemon=True).start()
app.mainloop()