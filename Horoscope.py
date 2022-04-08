#Program to generate horoscope from DOB provided by user by first finding the zodiac-sign using a loop function in the program, 
#and then generating the horoscope by passing zodiac-sign to an open-source Horoscope API which returns that day's horoscope of 
#the passed zodiac-sign.

from tkinter import *
import requests

#exit function:
def close_window():
    window.destroy()

#click function:
def click():
    e_day = int(dayip.get())
    e_month = monthip.get()
    e_year = yearip.get()
    output.delete(0.0,END)
    ZodiacOp.delete(0.0,END)
    ZSign = Zodiac(e_day,e_month,e_year)
    if ZSign == "ERROR":
        output.insert(END, "ERROR : Wrong date entered !\n        Please Try Again.")
    else:
        ZodiacOp.insert(END, ZSign)
        output.insert(END, HoroscopeAPI(ZSign))

#Finding Zodiac Sign:
def Zodiac(d,m,y):
    if (y=="       ") or (m=="February" and d>29) or ((m=="April" or m=="June" or m=="September" or m=="November")and d==31):
        return "ERROR"
    else:
        if (m=="March" and d>=21) or (m=="April" and d<=20):
            return "Aries"
        elif (m=="April" and d>=21) or (m=="May" and d<=21):
            return "Taurus"
        elif (m=="May" and d>=22) or (m=="June" and d<=21):
            return "Gemini"
        elif (m=="June" and d>=22) or (m=="July" and d<=23):
            return "Cancer"
        elif (m=="July" and d>=24) or (m=="August" and d<=23):
            return "Leo"
        elif (m=="August" and d>=24) or (m=="September" and d<=23):
            return "Virgo"
        elif (m=="September" and d>=24) or (m=="October" and d<=23):
            return "Libra"
        elif (m=="October" and d>=24) or (m=="November" and d<=22):
            return "Scorpio"
        elif (m=="November" and d>=23) or (m=="December" and d<=21):
            return "Sagittarius"
        elif (m=="December" and d>=22) or (m=="January" and d<=20):
            return "Capricorn"
        elif (m=="January" and d>=21) or (m=="February" and d<=19):
            return "Aquarius"
        elif (m=="February" and d>=20) or (m=="March" and d<=20):
            return "Pisces"
        else:
            return "ERROR"
        

#Finding daily Horoscope:
def HoroscopeAPI(ZSign):
    resp = requests.post('https://aztro.sameerkumar.website/?sign='+ZSign+'&day=today')
    #resp = requests.get("http://horoscope-api.herokuapp.com/horoscope/today/"+ZSign)
    data = resp.json()
    #return data['horoscope']
    return data['description']

#main :
window = Tk()
window.geometry('500x500')
window.title("Daily Horoscope")
#window.configure(background="white")

#input :
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
days = [x for x in range(1,32)]
years = [x for x in range(2021,1950,-1)]

#Days Drop-down menu:
dayip = StringVar()
dayip.set("       ")
daydrop = OptionMenu(window, dayip, *days) .grid(row=2, column=0, sticky=N)


#Month Drop-down menu:
monthip = StringVar()
monthip.set("       ")
monthdrop = OptionMenu(window, monthip, *months) .grid(row=3, column=0, sticky=N)

#Year Drop-down menu:
yearip = StringVar()
yearip.set("       ")
yeardrop = OptionMenu(window, yearip, *years) .grid(row=4, column=0, sticky=N)

Logo = PhotoImage(file="Daily-Horoscope2.gif")
Label (window, image=Logo) .grid(row=0, column=0, sticky=N+S)
#Label (window, text="HOROSCOPE\n", bg="black", fg="white", font="times 14 bold") .grid(row=0, column=0, sticky=N)

#Labels:
Label (window, text="\nEnter your Date of Birth :",  font="Aerial 12 bold") .grid(row=1, column=0, sticky=W)
#Day:
Label (window, text="Day:",  font="none 10") .grid(row=2, column=0, sticky=W)
#Month:
Label (window, text="Month:",  font="none 10") .grid(row=3, column=0, sticky=W)
#Year:
Label (window, text="Year:",  font="none 10") .grid(row=4, column=0,sticky=W)



#Entry box:
#DOBentry = Entry(window, width=20, bg="white")
#DOBentry.grid(row=1, column=1, sticky=E)
#DayEntry = Entry(window, width=7, bg="white")
#DayEntry.grid(row=2, column=0, sticky=N)
#YearEntry = Entry(window, width=7, bg="white")
#YearEntry.grid(row=4, column=0, sticky=N)

#Submit Button:
Button(window, text="SUBMIT", width=6, bg="cyan", fg="black", command=click) .grid(row=5, column=0, sticky=N, pady=4)

#Zodiac Sign Label & Entry:
Label (window, text="Your ZODIAC sign is : ", font="Aerial 10 bold") .grid(row=7, column=0, sticky=W)
ZodiacOp = Text(window, width=14, height=1, background="white")
ZodiacOp.grid(row=7, column=0, sticky=N)

#Output Box:
output = Text(window, width=62, height=6, wrap=WORD, background="white")
output.grid(row=8, column=0, columnspan=1, sticky=N)

#Exit button:
Button(window, text="EXIT", width=4, bg="cyan", fg="black", command=close_window) .grid(row=9, column=0, pady=4)

#Running the main loop :
window.mainloop()