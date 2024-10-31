import tkinter as tk
from tkinter import scrolledtext, messagebox
import speech_recognition as sr
import threading

class AudioRecorderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Audio Recorder")
        
        # Create UI components
        self.create_widgets()

    def create_widgets(self):
        # Input label
        input_label = tk.Label(self.root, text="Press the button to record audio:")
        input_label.pack(pady=10)

        # Record button
        record_button = tk.Button(self.root, text="Record", command=self.start_recording)
        record_button.pack(pady=5)

        # Output text area
        output_label = tk.Label(self.root, text="Recognized Text:")
        output_label.pack(pady=10)

        self.output_text_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=50, height=10)
        self.output_text_area.pack(padx=10, pady=10)

    def start_recording(self):
        # Run the record_audio method in a separate thread
        threading.Thread(target=self.record_audio).start()

    def record_audio(self):
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            messagebox.showinfo("Recording", "Please speak...")
            audio = recognizer.listen(source)  # Listen for the first phrase

        try:
            # Recognize speech using Google Web Speech API
            text = recognizer.recognize_google(audio)
            self.output_text_area.delete("1.0", tk.END)  # Clear previous output
            self.output_text_area.insert(tk.END, text)  # Insert recognized text
        except sr.UnknownValueError:
            messagebox.showerror("Error", "Sorry, I could not understand the audio.")
        except sr.RequestError:
            messagebox.showerror("Error", "Could not request results from Google Speech Recognition service.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AudioRecorderApp(root)
    root.mainloop()
