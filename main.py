def main():  # ik that in py we dont need the main funxtion but its here for restarting the bot..head over to line 138

    import pyttsx3
    import speech_recognition as sr
    import datetime
    import wikipedia
    import webbrowser
    import os
    import smtplib
    import pywhatkit
    import pyjokes

    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    # code by kusti420 
    # code by Varun Banka
        print(f"""{"" * 4}
                                                                   listening...          
    {"" * 6}""")


    def speak(audio):
        engine.say(audio)
        # code by Varun Banka & Kusti420
        engine.runAndWait()


    def wishMe():
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            speak("Good Morning!")

        elif hour>=12 and hour<18:
            speak("Good Afternoon!")   

        else:
            speak("Good Evening!")  

        speak("I am an AI powered virtual assistent. How can I help? ")       

    def takeCommand():
        #It takes microphone input from the user and returns string output

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")    
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:  
            print("Say that again please...")  
            return "None"
        return query

    def sendEmail(to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('youremail@gmail.com', 'your-password')
        server.sendmail('youremail@gmail.com', to, content)
        server.close()

    if __name__ == "__main__":
        wishMe()
        while True:
        # if 1:
            query = takeCommand().lower()

            # Logic for executing tasks based on query
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'open youtube' in query:
                webbrowser.open("youtube.com")

            elif 'open google' in query:
                webbrowser.open("google.com")

            elif 'joke' in query:
                speak(pyjokes.get_joke())


            elif 'open stackoverflow' in query:
                webbrowser.open("stackoverflow.com")   


            elif 'music' in query:
                webbrowser.open("google.com")

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f"Sir, the time is {strTime}")

            elif 'email' in query:
                try:
                    speak("What should I say?")
                    content = takeCommand()
                    to = "bankavarun18@gmail.com"    
                    sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Looks like something went wrong, please try again later")

            elif r.recognize_google(audio) == "what is your name":
                bots_reply = "I am a bot"
            elif r.recognize_google(audio) == "what is your favorite color":
                bots_reply = "I like red"
            elif r.recognize_google(audio) == "what is your favorite food":
                bots_reply = "I like pizza"
            elif r.recognize_google(audio) == "what is your favorite movie":
                bots_reply = "I like Jobs"
            elif r.recognize_google(audio) == "what is your favorite song":
                bots_reply = "I like all the songs on the following playlist " \
                                 "https://open.spotify.com/playlist/6V5Vr5ik0u16lpoH6w2xYo?si=c809ac07413144b6"
            elif r.recognize_google(audio) == "what is your favorite sport":
                bots_reply = "I like football"
            elif r.recognize_google(audio) == "what is your favorite animal":
                bots_reply = "I like dogs"   

            else:
                speak("That maybe beyond my abilities at the moment")


main()

while True:
    wouldYouLikeToStartAgain = input(
        "Would you like to run this tool again y/n ? \n")
    if wouldYouLikeToStartAgain == "y" or wouldYouLikeToStartAgain == "Y" or wouldYouLikeToStartAgain == "Yes" or wouldYouLikeToStartAgain == "Yep" or wouldYouLikeToStartAgain == "yes" or wouldYouLikeToStartAgain == "yep" or wouldYouLikeToStartAgain == "sure":
        main()
    elif wouldYouLikeToStartAgain == "n" or wouldYouLikeToStartAgain == "N" or wouldYouLikeToStartAgain == "No" or wouldYouLikeToStartAgain == "Nope" or wouldYouLikeToStartAgain == "yes" or wouldYouLikeToStartAgain == "nope" or wouldYouLikeToStartAgain == "nah" or wouldYouLikeToStartAgain == "Nah":
        print("Cool thanks for using the programme")
        break
    else:
        print("That maybe beyond my abilities at the moment")
