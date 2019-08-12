def AgeCalculate():
    from speak import speak
    from datetime import datetime
    try:
        print("please enter your birthday")
        speak("Year")
        bd_y=int(input("Year:"))
        speak("Month")
        bd_m=int(input("Month(1-12):"))
        speak("Date")
        bd_d=int(input("Date:"))
        calculate = datetime.now() - datetime(bd_y, bd_m, bd_d)
        year=calculate.days/365
        month=(year-int(year))*12
        print(f"You are now {int(year)} year's and {int(month)} months old: ")
        speak(f"You are now {int(year)} year's and {int(month)} months old: ")
        speak("Thank you")
    except:
        print("!!Something Went Wrong!!")
        speak("Something Went Wrong")
