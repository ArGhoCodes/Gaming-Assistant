import speech_recognition as sr 
import pyttsx3

recognizer = sr.Recognizer()
while True:

    try:

        with sr.Microphone() as mic:

            recognizer.adjust_for_ambient_noise(mic, duration=1)
            audio = recognizer.listen(mic)

            text = recognizer.recognize_google(audio, language='en')
            text = text.lower()

            print(f'Recognized speech to text:  {text}')

    except sr.UnknownValueError():
        recognizer = sr.Recognizer()
        continue