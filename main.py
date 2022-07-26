import speech_recognition as sr
import pyjokes
import pyttsx3
import wikipedia
r = sr.Recognizer()
with sr.Microphone() as source:
    print("\n")
    print("\n")
    print("\n")
    print("\n")

    print("                                                     listening...          ")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    audio = r.listen(source)


    # down below are my replies
    #bots_reply = pass
if r.recognize_google(audio) == "what is your name":
    bots_reply = "I am a bot"
elif r.recognize_google(audio) == "what is your favorite color":
    bots_reply = "I like blue"
elif r.recognize_google(audio) == "what is your favorite food":
    bots_reply = "I like pizza"
elif r.recognize_google(audio) == "what is your favorite movie":
    bots_reply = "I like Star Wars"
elif r.recognize_google(audio) == "what is your favorite song":
    bots_reply = "I like all the songs on the following playlist " \
                     "https://open.spotify.com/playlist/6V5Vr5ik0u16lpoH6w2xYo?si=c809ac07413144b6"
elif r.recognize_google(audio) == "what is your favorite sport":
    bots_reply = "I like football"
elif r.recognize_google(audio) == "what is your favorite animal":
    bots_reply = "I like dogs"
elif r.recognize_google(audio) == "tell me a joke" or r.recognize_google(audio) == "joke":
    bots_reply =pyjokes.get_joke()
else:

    bots_reply = wikipedia.summary("Wikipedia")

#down below is code to speak



engine = pyttsx3.init()
engine.say(bots_reply)
engine.runAndWait()

# down below is the code to change rate of voice
engine.setProperty('rate', 100)  # setting up new voice rate






