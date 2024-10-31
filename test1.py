import tkinter as tk
from tkinter import scrolledtext, messagebox
import speech_recognition as sr

recognizer = sr.Recognizer()
# Create the main window
root = tk.Tk()
root.title("Audio Recorder")

# Input label
input_label = tk.Label(root, text="Press the button to record audio:")
input_label.pack(pady=10)


# Output text area
output_label = tk.Label(root, text="Recognized Text: ")
output_label.pack(pady=10)

def record_and_transcribe():
    try:
        # Capture audio from the microphone
        with sr.Microphone() as source:
            print("Please speak now...")
            audio = recognizer.listen(source)

            # Transcribe audio using Google API
            text = recognizer.recognize_google(audio)
            print("Transcribed Text:", text)
            input_label['text'] = f"Recognized Text: {text}"
            return text

    except sr.UnknownValueError:
        print("Sorry, could not understand the audio.")
    except sr.RequestError:
        print("Could not connect to the service.")


# Record button
record_button = tk.Button(root, text="Record", command=record_and_transcribe)
record_button.pack(pady=5)


output_text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=10)
output_text_area.pack(padx=10, pady=10)

# Start the Tkinter main loop
root.mainloop()
# Run the function
print(record_and_transcribe())
