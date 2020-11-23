import os
import pyttsx3
import speech_recognition as sr

class pythonhub:
    def takeCommands(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('Listening...')

            r.pause_threshold = 0.7
            audio = r.listen(source)

            try:
                print("Recognizing...")
                Query = r.recognize_google(audio, language='en-in')
                print("the query is printed='", Query, " ' ")
            except Exception as e:
                print(e)

                print("Repetition needed")
                return "NONE"
        return Query
    
    def Speak(self, audio):
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.say(audio)
        engine.runAndWait()
    
    def quitSelf(self):
        self.Speak("Do you want to shut down?")

        take = self.takeCommands()
        choice = take
        if "yes" in choice:
            print("Shutting down")
            self.Speak("Shutting Down Michelangelo's Mac")
        if "no" in choice:
            print("Thanks")
            self.Speak("Thanks Michelangelo")

if __name__ == '__main__':
    Maam = pythonhub()
    Maam.quitSelf()
