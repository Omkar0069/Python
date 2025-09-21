import pyjokes
import pyttsx3
engine = pyttsx3.init()
print("Printing Jokes....")
joke = pyjokes.get_joke()
print(joke)
engine.say(joke)
engine.runAndWait()

'''Types of Module: (ctrl + / to comment)
1.Built in Module(already install in python)
2.External Module(Installed using pip)'''