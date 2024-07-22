'''import pyttsx3
import speech_recognition as sr
import datetime
import os
import random
import wikipedia
import webbrowser
import pyautogui
import time
import subprocess

# Initialize the speech engine
engine = pyttsx3.init()

# Set the voice property
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    """Function to convert text to speech"""
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takeCommand():
    """Function to take voice commands from the user"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except sr.RequestError:
            # API was unreachable or unresponsive
            speak("Sorry, I couldn't reach the Google API.")
            return "None"
        except sr.UnknownValueError:
            # Speech was unintelligible
            speak("Sorry, I could not understand what you said.")
            return "None"
        except sr.WaitTimeoutError:
            # Listening timed out while waiting for phrase to start
            speak("Sorry, I timed out while listening.")
            return "None"
        except Exception as e:
            speak("An error occurred: " + str(e))
            return None
        return query

def username():
    """Function to ask for the user's name and greet them"""
    speak("What should I call you, Sir?")
    uname = takeCommand()
    if uname != "None":
        speak("Welcome Mr. " + uname)
        speak("How can I help you, Sir?")
        
def wishMe():
    """Function to greet the user based on the time of day"""
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Night Sir")
    speak("This is your personal assistant, James")

if __name__ == '__main__':
    wishMe()
    username()  # Correctly calling the username
    while True:
        order = takeCommand().lower()
        if order == "none":
            continue
        
        
        if 'how are you' in order:
            speak("I am fine, Thank You!")
            speak("How are you, Sir?")
            
        elif 'fine' in order or 'good' in order:
            speak("It's good to know that you are fine")
            
        elif 'who I am' in order:
            speak('If you can talk, then surely, you are human')
            
        elif 'open notepad' in order:
            npath = 'C:\\windows\\notepad.exe'
            os.startfile(npath)
            
        #elif 'play music' in order or 'play songs' in order:
            #music_dir = ""
            #songs = os.listdir(music_dir)
            #rd = random.choice(songs)
            #os.startfile(os.path.join(music_dir,rd))
        
        elif 'wikipedia' in order:
            speak('Searching...')
            order = order.replace("wikipedia","")
            results = wikipedia.summary(order,sentences=2)
            speak("According to wikipedia")
            speak(results)
            
        elif 'open google' in order:
            speak("here you go to google, sir \n")
            webbrowser.open("google.com")
        
        elif 'open youtube' in order:
            speak("here you go to YouTube, sir \n")
            webbrowser.open("youtube.com") 
            
        elif 'open amazon' in order:
            speak("here you go to amazon, sir....Happy Shopping! \n")
            webbrowser.open("amazon.com")
            
        elif "where is" in order:
            order = order.replace("where is","")
            location=order
            speak("Locating...")
            speak(location)
            webbrowser.open("https://www.google.co.in/maps/place/"+location+"")
            
        elif "write a note" in order:
            speak("what should I write, sir?")
            note=takeCommand()
            file=open('texts.txt','w')
            speak("Sir, should I include date and time as well?")
            sn=takeCommand()
            if 'yes' in sn or 'sure' in sn:
                strTime=datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(note)
                speak("Done!, sir")
            else:
                file.write(note)
                speak("Done!, sir")
                
        elif 'show notes' in order:
            speak("showing notes...")
            file=open("texts.txt","r")
            print(file.read())
            speak(file.read(0))
            
        elif 'shut down' in order or 'turn off' in order:
            speak("Hold on a second: Your system is about to shut down")
            speak("Make sure, all of your applications are closed")
            time.sleep(5)
            subprocess.call(['shut down','/s'])
            
        elif 'restart' in order:
            speak("restarting the device...")
            subprocess.call(['restart','/r'])
            
        elif 'hibernate' in order:
            speak("hibernating...")
            subprocess.call(['hibernate','/h'])
            
        elif 'log out' in order or 'sign out' in order:
            speak("Make sure, all of your applications are closed")
            time.sleep(5)
            subprocess.call(['shut down','/i'])
            
        elif 'switch window' in order:
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            time.sleep(5)
            pyautogui.keyUp('alt')
        
        elif 'take a screenshot' in order or 'screenshot this' in order:
            speak("Sir, please tell me the name for this file. ")
            name = takeCommand().lower()
            speak("please hold the screen")
            time.sleep(3)
            img=pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("Screenshot captured sir!")
     '''
     
import pyttsx3
import speech_recognition as sr
import datetime
import os
import random
import wikipedia
import webbrowser
import pyautogui
import time
import subprocess
import psutil  # For system resource monitoring
import speedtest  # For internet speed test
import requests  # For fetching game news
from bs4 import BeautifulSoup  # For parsing HTML
from win10toast import ToastNotifier  # For system notifications

# Initialize the speech engine
engine = pyttsx3.init()

# Set the voice property
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    """Function to convert text to speech"""
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takeCommand():
    """Function to take voice commands from the user"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except sr.RequestError:
            speak("Sorry, I couldn't reach the Google API.")
            return "None"
        except sr.UnknownValueError:
            speak("Sorry, I could not understand what you said.")
            
            exit()
        except sr.WaitTimeoutError:
            speak("Sorry, I timed out while listening.")
            return "None"
            exit()
        except Exception as e:
            speak("An error occurred: " + str(e))
            return None
            exit()
        return query

def username():
    """Function to ask for the user's name and greet them"""
    speak("What should I call you, Sir?")
    uname = takeCommand()
    if uname != "None":
        speak("Welcome Mr. " + uname)
        speak("How can I assist you today?")

def wishMe():
    """Function to greet the user based on the time of day"""
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Night Sir")
    speak("This is your gaming assistant, James")

def open_game(game_name):
    """Function to open a game"""
    game_paths = {
        'minecraft': 'C:\\path_to_minecraft_launcher.exe',
        'fortnite': 'C:\\path_to_fortnite_launcher.exe',
        'csgo': 'C:\\path_to_csgo_launcher.exe'
    }
    path = game_paths.get(game_name.lower())
    if path:
        speak(f"Launching {game_name}")
        os.startfile(path)
    else:
        speak(f"Sorry, I don't have the path for {game_name}")

def adjust_volume(level):
    """Function to adjust system volume"""
    speak(f"Setting volume to {level}")
    if os.name == 'nt':
        subprocess.run(['nircmd.exe', 'setsysvolume', str(level * 65535 // 100)])
    else:
        speak("Volume control is not supported on this operating system.")

def check_game_stats():
    """Function to check and display game stats"""
    speak("Checking game statistics... Please wait.")
    # Example: fetch from an API or read from a file
    # stats = get_game_stats()
    # speak(f"Your current stats are: {stats}")

def manage_peripherals(command):
    """Function to manage gaming peripherals"""
    if 'lights' in command:
        speak("Managing RGB lights...")
        # Example: send command to RGB controller
    elif 'mouse' in command:
        speak("Adjusting mouse settings...")
        # Example: configure mouse DPI or macros
    else:
        speak("I cannot manage that peripheral at the moment.")

def system_monitoring():
    """Function to display system resource usage"""
    try:
        cpu_usage = psutil.cpu_percent(interval=1)
        ram_usage = psutil.virtual_memory().percent
        disk_usage = psutil.disk_usage('/').percent

        # Temperature monitoring might not be supported
        # gpu_temp = psutil.sensors_temperatures().get('coretemp', [{}])[0].get('current', 'N/A')

        speak(f"CPU Usage: {cpu_usage}%")
        speak(f"RAM Usage: {ram_usage}%")
        speak(f"Disk Usage: {disk_usage}%")
        # speak(f"GPU Temperature: {gpu_temp}°C")

    except Exception as e:
        speak(f"Sorry, I couldn't monitor the system resources. Error: {str(e)}")


def system_notifications():
    """Function to display system notifications"""
    speak("You have new notifications.")
    toaster = ToastNotifier()
    toaster.show_toast("System Notification", "You have new notifications", duration=10)

def exit_assistant():
    """Function to end the assistant"""
    speak("Goodbye! Have a great day.")
    exit()

if __name__ == '__main__':
    wishMe()
    username()  # Correctly calling the username
    while True:
        order = takeCommand().lower()
        if order == "none":
            continue
        
        if 'exit' in order or 'stop' in order:
            exit_assistant()
        
        if 'how are you' in order:
            speak("I am fine, Thank You!")
            speak("How are you, Sir?")
            
        elif 'fine' in order or 'good' in order:
            speak("It's good to know that you are fine")
            
        elif 'who I am' in order:
            speak('If you can talk, then surely, you are human')
        
        elif 'open notepad' in order:
            npath = 'C:\\windows\\notepad.exe'
            os.startfile(npath)
        
        elif 'wikipedia' in order:
            speak('Searching...')
            order = order.replace("wikipedia", "")
            results = wikipedia.summary(order, sentences=2)
            speak("According to Wikipedia")
            speak(results)
            
        elif 'open google' in order:
            speak("Here you go to Google, Sir")
            webbrowser.open("google.com")
        
        elif 'open youtube' in order:
            speak("Here you go to YouTube, Sir")
            webbrowser.open("youtube.com") 
            
        elif 'open amazon' in order:
            speak("Here you go to Amazon, Sir. Happy Shopping!")
            webbrowser.open("amazon.com")
            
        elif "where is" in order:
            order = order.replace("where is", "")
            location = order
            speak("Locating...")
            speak(location)
            webbrowser.open(f"https://www.google.co.in/maps/place/{location}")
            
        elif "write a note" in order:
            speak("What should I write, Sir?")
            note = takeCommand()
            with open('texts.txt', 'w') as file:
                speak("Sir, should I include date and time as well?")
                sn = takeCommand()
                if 'yes' in sn or 'sure' in sn:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    file.write(f"{strTime}\n{note}")
                else:
                    file.write(note)
            speak("Done, Sir")
                
        elif 'show notes' in order:
            speak("Showing notes...")
            with open("texts.txt", "r") as file:
                content = file.read()
            print(content)
            speak(content)
        
        elif 'shut down' in order or 'turn off' in order:
            speak("Hold on a second: Your system is about to shut down")
            speak("Make sure all of your applications are closed")
            time.sleep(5)
            subprocess.call(['shutdown', '/s'])
        
        elif 'restart' in order:
            speak("Restarting the device...")
            subprocess.call(['shutdown', '/r'])
            
        elif 'hibernate' in order:
            speak("Hibernating...")
            subprocess.call(['shutdown', '/h'])
            
        elif 'log out' in order or 'sign out' in order:
            speak("Make sure all of your applications are closed")
            time.sleep(5)
            subprocess.call(['shutdown', '/l'])
            
        elif 'switch window' in order:
            pyautogui.hotkey('alt', 'tab')
            time.sleep(2)
        
        elif 'take a screenshot' in order or 'screenshot this' in order:
            speak("Sir, please tell me the name for this file.")
            name = takeCommand().lower()
            speak("Please hold the screen")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("Screenshot captured, Sir!")
        
        # New functionalities for gaming assistant
        elif 'launch' in order:
            game_name = order.split('launch ')[-1]
            open_game(game_name)
        
        elif 'volume' in order:
            level = int(order.split('volume ')[-1].replace('%', ''))
            adjust_volume(level)
        
        elif 'check system' in order:
            system_monitoring()
        
        
        elif 'notifications' in order:
            system_notifications()
        
        elif 'manage peripherals' in order:
            manage_peripherals(order)
        
        else:
            speak("Sorry, I didn't understand that command.")
            exit()

   
