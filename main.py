from takeCommand import takeCommandimport datetimeimport wikipedia  # pip install wikipediaimport webbrowserimport osimport jsonimport smtplibimport programmfrom health import setimport calendarfrom speak import speakfrom soldier import soldierwith open('dt.json', 'r') as c:    params = json.load(c)["params"]def wishMe():    hour = int(datetime.datetime.now().hour)    if hour >= 0 and hour < 12:        speak("Good Morning!")    elif hour >= 12 and hour < 18:        speak("Good Afternoon!")    else:        speak("Good Evening!")    speak("I am Jarvis Sir. Please tell me how may I help you")def sendEmail(to, content):    with open(params['secure_file'], "r") as a:        a1 = a.readline(28)        a.seek(28 + 13)        a2 = a.readline(14)    server = smtplib.SMTP('smtp.gmail.com', 587)    server.ehlo()    server.starttls()    server.login("tiwarick1996@gmail.com","*******")    server.sendmail('tiwarick1996@gmail.com', to, content)    server.close()if __name__ == '__main__':    wishMe()    while True:        # if 1:        query = input("write something!")        # query = takeCommand().lower()        if(query[0:4]=="suno"):        # Logic for executing tasks based on query            if 'wikipedia' in query:                speak('Searching Wikipedia...')                query = query.replace("wikipedia", "")                results = wikipedia.summary(query, sentences=2)                speak("According to Wikipedia")                print(results)                speak(results)            elif 'open youtube' in query:                webbrowser.open("https://www.youtube.com/")            elif 'calender' in query:                print(calendar.calendar(2019))            elif 'close youtube' in query:                os.system('TASKKILL /F /IM "chrome.exe"')            elif 'program' in query:                programm.program()            elif 'about you' in query:                print("my name is jarvis and i am here to help you! I am a multiprocessor assistent and "                      "I will do what ever you say Thank you")                speak("my name is jarvis and i am here to help you! I am a multiprocessor assistent and "                      "will do what ever you say Thank you")            elif 'health' in query:                set()            elif 'open google' in query:                webbrowser.open("https://www.google.com/")            elif 'open stackoverflow' in query:                webbrowser.open("stackoverflow.com")            elif 'play video' in query:                music_dir = params['video_dir']                songs = os.listdir(music_dir)                print(songs)                video_option = input("which video do you want to watch: ")                # video_option = takeCommand().lower()                for i in songs:                    if video_option.lower() in i.lower():                        os.startfile(os.path.join(music_dir, i))                        break                else:                    print("song not found")                    speak("song not found")            elif 'close video' in query:                try:                    a=os.system(f"TASKKILL /IM {params['video_player']} ")                    if(a!=0):                        print("video is not open!!!but you are "                              "trying to close!")                        speak("video is not open!!!but you are "                              "trying to close!")                    else:                        print("video is closed")                        speak("video is closed")                except:                    print(f"something went wrong ")            elif 'the time' in query:                strTime = datetime.datetime.now().strftime("%H:%M:%S")                speak(f"Sir, the time is {strTime}")            elif 'sequence' in query:                changes_path=input("enter full path")                file_mode=input("enter mode of the file like jpg,mp4,mp3 :")                try:                    soldier(changes_path,file_mode)                    print("Work done")                    speak("Work done")                except:                    print("sorry we could not do changes in your file")                    speak("sorry we could not do changes in your file")            elif 'age' in query:                from date_of_birth import AgeCalculate                AgeCalculate()            elif 'open code' in query:                codePath = params['visual_studio_code_path']                os.startfile(codePath)            elif 'close code' in query:                os.system('TASKKILL /F /IM "Code.exe"')            elif 'open notepad' in query:                codePath = params['notepad_path']                os.startfile(codePath)            elif 'close notepad' in query:                os.system('TASKKILL /F /IM "notepad.exe"')            elif 'open sublime' in query:                codePath = params['sublime_path']                os.startfile(codePath)            elif 'close sublime' in query:                os.system('TASKKILL /F /IM "sublime_text.exe"')            elif 'open chrome' in query:                codePath = params['chrome_path']                os.startfile(codePath)            elif 'close chrome' in query:                os.system('TASKKILL /F /IM "chrome.exe"')            elif 'email to chandan' in query:                try:                    speak("What should I say?")                    content = input("write here")                    to = "deepaktiwari221299@gmail.com"                    sendEmail(to, content)                    speak("Email has been sent!")                except Exception as e:                    print(e)                    speak("Sorry my friend dt bhai. I am not able to send this email")            elif 'exit' in query:                break            else:                print("Sorry Sir, we could not proceed you! please be clear")                speak("Sorry Sir, we could not proceed you! please be clear")        else:            print("Sorry Sir, we could not recognise you! please use suno for admin!")            speak("Sorry Sir, we could not recognise you! please use suno for admin!")    speak("Thank you Sir")