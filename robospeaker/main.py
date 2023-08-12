import win32com.client as wincom
speak = wincom.Dispatch("SAPI.SpVoice")


if __name__ == '__main__' :
    print("Welcome to Robospeaker 1.1. Created by Sabyasachi , to close the program press 'q' ")
    while True:
        x = input("Enter what you want me to Speak : ")
        if x == 'q':
            speak.Speak("Exiting from the program")
            break

        speak.Speak(x)