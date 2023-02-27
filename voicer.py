import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import sys
listener = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('voice', 'english')

def talk(text):
engine.say(text)
engine.runAndWait()

def take_command():
try:
with sr.Microphone() as source:
listener.adjust_for_ambient_noise(source, duration = 2)
print('listening...')
voice = listener.listen(source)
command = listener.recognize_google(voice)
command = command.lower()
if 'geek speak' in command:
command = command.replace('geek speak', '')
except:
command = "garbled"
return command

def run_geekspeak():
command = take_command()
print(command)
if 'play' in command:
song = command.replace('play', '')
talk('playing ' + song)
pywhatkit.playonyt(song)
elif 'time' in command:
time = datetime.datetime.now().strftime('%I:%M %p')
print(time)
talk('Current time is' + time)
elif 'who is' in command:
person = command.replace('who is', '')
info = wikipedia.summary(person, 1)
print(info)
talk(info)

elif 'date' in command:
talk('sorry, I am single’)
elif 'are you single' in command:
talk('Why? How many of me do you see?’)
elif 'what is' in command:
person = command.replace('what is', '')
info = wikipedia.summary(person, 1)
print(info)
talk(info)
elif 'joke' in command:
talk(pyjokes.get_joke())
elif 'quit' in command:
sys.exit()
else:
talk('Place say again')

while True:
run_geekspeak()
