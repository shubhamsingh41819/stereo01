import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import cv2
import pywhatkit as kit
import sys
import pyautogui
import psutil
import pyjokes
import pytz
import wolframalpha
import time
wol = 'TYR862-QV8VPPU5H2'

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("good morning!, sir.")

    elif 12 <= hour < 18:
        speak("good Afternoon!, sir.")

    else:
        speak("good Evening!, sir, i hope your day was good.")

    speak("I am stereo sir. Please tell me how may i help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)

        try:
            print("recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"user said: {query}\n")

        except Exception as e:
            print(e)
            print("say that again please...")
            return "none"
        return query


def cpu():
    cpu = str(psutil.cpu_percent())
    print(cpu)
    speak(f"you have used{cpu} of battery.")
    battery = psutil.sensors_battery().percent
    speak(f"you have used{battery} of battery")


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('aa094681101@gmail.com@gmail.com', 'shub779592')
    server.sendmail('ss09468110@gmail.com', to, content)
    server.close()


def screenshot():
    img = pyautogui.screenshot()
    img.save("C:\\Users\\SHUBHAM SINGH\\OneDrive\\Pictures\\BlueStacks.png")
    speak("screenshot is successfully taken")


def date():
    t_date = datetime.datetime.now(tz=pytz.timezone("Asia/Kolkata"))
    print(t_date.strftime("%I:%M%p"))
    speak(t_date.strftime("%I:%M%p"))


date()


def joke():
    print(pyjokes.get_joke())
    speak(pyjokes.get_joke())


if __name__ == "__main__":
    wishMe()
while True:

    query = takeCommand().lower()
    if 'wikipedia' in query:
        speak('wait for a second')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("answer for your question.")
        print(results)
        speak(results)

    elif "note down" in query:
        speak("what should i write down sir")
        note = takeCommand()
        remember = open("data.txt", "w")
        remember.write(note)
        remember.close()
        speak("i have noted it down" + note)

    elif 'what do you have in notes' in query:
        speak('showing note')
        remember = open('data.txt', 'r')
        print(remember.read())
        speak(remember.read())

    elif 'open google' in query:
        speak("sir what should i search?")
        cm = takeCommand().lower()
        speak('here you go')
        webbrowser.open('https://www.google.com/search?q=' + cm)

    elif 'open hotstar' in query:
        webbrowser.open("hotstar.com")
        speak("opening hotstar")

    elif 'open voot' in query:
        webbrowser.open("voot.com")
        speak("here you go")

    elif 'open sony Liv' in query:
        webbrowser.open("www.sonyliv.com")
        speak("opening sonyliv")

    elif 'open whatsapp' in query:
        webbrowser.open("whatsapp.com")
        speak("opening whatsapp")

    elif 'open jio cinema' in query:
        webbrowser.open("https://www.jiocinema.com/")
        speak("opening jio cinema")

    elif 'open edu mantra' in query:
        webbrowser.open("https://www.edumantra.com")
        speak("opening edumantra")

    elif 'what is the time' in query:
        strTime = datetime.datetime.now().strftime("%I:%M:%p")
        print(f"sir, the time is {strTime}")
        speak(f"sir, the time is {strTime}")

    elif 'open code' in query:
        f = "C:\\Users\\SHUBHAM SINGH\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(f)
        speak("here you go")

    elif "open command prompt" in query:
        os.system("start cmd")
        speak("starting command prompt")

    elif 'open instagram' in query:
        webbrowser.open("https://www.instagram.com/shubham_91418/", new=2)
        speak("Have a look sir")

    elif "open google chrome" in query:
        speak("what should i search")
        gc = r"C:\Users\SHUBHAM SINGH\AppData\Local\Google\Chrome\Application\chrome.exe"
        speak("opening google chrome")
        search = takeCommand().lower()
        webbrowser.get(gc).open_new_tab(search + ".com")
    elif "send message" in query:
        kit.sendwhatmsg("+917795922805", "i sent this message using stereo", 7, 3)

    elif "videos on youtube" in query:
        kit.playonyt("carryminati")

    elif "open camera" in query:
        cap = cv2.VideoCapture(0)
        while True:
            ret, img = cap.read()
            cv2.imshow("webcam", img)
            k = cv2.waitKey(50)
            if k == 27:
                break
        cap.release()
        cv2.destroyAllWindows()

    elif 'email to shubham' in query:
        try:
            speak("what should i say?")
            content = takeCommand().lower()
            to = "aa094681101@gmail.com"
            sendEmail(to, content)
            speak("Email has been sent!.")

        except Exception as e:
            print(e)
            speak("sorry sir, email cannot be sent")

    elif "close" in query:
        speak("Thanks for Using me sir, have a good day.")
        sys.exit()
    elif query == "none":
        continue

    elif 'open youtube' in query:
        speak("what should i play,sir")
        sp = takeCommand().lower()
        speak('opening youtube')
        webbrowser.open_new_tab('https://www.youtube.com/search?q=' + sp)
        
    elif "close notepad" in query:
        speak("okay sir, closing notepad")
        os.system("taskkill /f /im notepad.exe")

    elif "screenshot" in query or 'take a screenshot' in query:
        screenshot()
    elif "battery" in query:
        cpu()

    elif "tell me a joke" in query:
        joke = pyjokes.get_joke()
        print(joke)
        speak(joke)

    elif "open word" in query:
        speak('opening MS word')
        md = r'"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE"'
        os.startfile(md)

    elif 'remember that' in query:
        speak("what should i remember?")
        memory = takeCommand()
        speak('you asked me to remember that' + memory)
        remember = open('memory.txt', 'w')
        remember.write(memory)
        remember.close()

    elif 'what did i ask you to remember' in query:
        remember = open('memory.txt', 'r')
        speak('you asked me to remember that' + remember.read())

    elif 'where is' in query:
        query = query.replace('where is', '')
        location = query
        speak('you asked to locate' + location)
        webbrowser.open("https://www.google.com/maps/place" + location)

    elif 'stop listening' in query:
        try:

            speak('for how many seconds you want me to stop listening to your commands?')
            ans = str(takeCommand())
            time.sleep(ans)
            print(ans)
        except Exception as e:
            print(e)
            speak("sorry, repeat it")

    elif 'calculate' in query:
        client = wolframalpha.Client(wol)
        ind = query.lower().split().index('calculate')
        query = query.split()[ind + 1:]
        res = client.query(''.join(query))
        ans = next(res.results).text
        print('the answer is :' + ans)
        speak('the answer is:' + ans)
    elif 'what is ' or 'who is' in query:
        client = wolframalpha.Client(wol)
        res = client.query(query)
        try:
            print(next(res.results).text)
            speak(next(res.results).text)
        except StopIteration:
            print("sorry, could not find")
