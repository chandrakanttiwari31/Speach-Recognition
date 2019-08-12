from time import *
import os
def getdate():
    a=asctime(localtime(time()))
    return a

def set():
    from takeCommand import takeCommand
    from speak import speak
    # input_name=takeCommand().lower()
    speak("Enter Client Name")
    input_name=input("enter name")  ###remove this
    client_list = {'one': input_name}
    lock_list = {'one': "Diet",'two':"Exercise"}
    try:
        client_name="one"
        print("Selected Client : ", client_list[client_name], "\n", end="")

        print("say one for Lock")
        print("say two for Retrieve")
        # op=takeCommand().lower()
        op = input("enter") ###remove this
        print(op)

        if "one" in op:
            for key, value in lock_list.items():
                print("Say", key, "to lock", value, "\n", end="")
            # lock_name=takeCommand().lower()
            lock_name = input()
            print("Selected Job : ", lock_list[lock_name])
            f = open(f"{os.path.join(os.getcwd(),f'health/{client_list[client_name]}_{lock_list[lock_name]}.txt')}", "a")
            k = 'yes'
            while (k !="no"):
                print("Enter", lock_list[lock_name], "\n", end="")
                mytext = input()
                # mytext=takeCommand().lower()
                f.write("[ " + str(getdate()) + " ] : " + mytext + "\n")
                speak("ADD MORE say yes or no")
                k = input("ADD MORE ? yes/no:")
                # k=takeCommand().lower()
                continue
            f.close()
        elif "two" in op:
            for key, value in lock_list.items():
                print("say", key, "to retrieve", value, "\n", end="")
            lock_name = input()####remove
            # lock_name=takeCommand().lower()
            print(client_list[client_name], "-", lock_list[lock_name], "Report :", "\n", end="")
            f = open(client_list[client_name] + "_" + lock_list[lock_name] + ".txt", "rt")
            contents = f.readlines()
            for line in contents:
                print(line, end="")

            f.close()
        else:
            print("Invalid Input !!!")
            speak("Invalid Input !!!")
    except Exception as e:
        print("Wrong Input !!!")
        speak("Wrong Input !!!")



