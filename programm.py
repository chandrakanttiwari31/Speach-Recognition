def program():
    from speak import speak
    from takeCommand import takeCommand
    speak("what you want in program")
    # take_input=takeCommand().lower()
    take_input = input("what you want in program :")##takeinput()"remove
    take_input = take_input.lower()####remove
    res=take_input.split(" ")

    try:
        if 'close' in res:
            pass
        else:
            res = int(res[0])
        if 'prime' in take_input:
            n = res
            for i in range(2, n + 1):
                if (n % i == 0):
                    break
            if (i == n):
                speak(f"{n} is a prime number")
            else:
                speak(f"{n} is not a prime number")
            program()
        elif 'palindrome' in take_input:
            n = res
            u = n
            sum = 0
            while (u != 0):
                r = u % 10
                sum = int(str(sum) + str(r))
                u = u // 10
            if (n == sum):
                speak(f"{n} is palindrome number")
            else:
                speak(f"{n} is not a palindrome number")
            program()
        elif 'armstrong' in take_input:
            n = res
            u = n
            sum = 0
            while (u != 0):
                r = u % 10
                sum = sum + r ** 3
                u = u // 10

            if (n == sum):
                speak(f"{n} is Armstrome ")
            else:
                speak(f"{n} is not a Armstrome number")
            program()
        elif 'close' in take_input:
            speak("dear sir,your program has closed")
        else:
            speak("Invalid input, try again!")
            program()

    except:
        speak("please write in a write sequence first number!")
        print("please write in a write sequence first number!")
        program()

