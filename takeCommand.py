
def takeCommand():
    ''' It takes microphone input from the user and returns string output'''
    import speech_recognition as sr
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("say something...")
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


