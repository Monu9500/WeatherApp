from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city = city_name.get()
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=642e01ce32544b5d4d9b19f3da124a99"
    try:
        data = requests.get(url).json()

        if data.get("cod") != 200:  # Check if city is found
            w_label1.config(text="N/A")
            Wb_label1.config(text="City not found")
            temp_label1.config(text="N/A")
            per_label1.config(text="N/A")
            return

        w_label1.config(text=data["weather"][0]["main"])
        Wb_label1.config(text=data["weather"][0]["description"])
        temp_label1.config(text=f"{data['main']['temp'] - 273.15:.2f} °C")
        per_label1.config(text=data["main"]["pressure"])

    except Exception as e:
        w_label1.config(text="Error")
        Wb_label1.config(text=str(e))
        temp_label1.config(text="N/A")
        per_label1.config(text="N/A")


win = Tk()
win.title("Weather Detection")
win.config(bg="blue")
win.geometry("500x570")

name_label = Label(win, text="Weather Detection",
                   font=("Times New Roman", 30, "bold"))
name_label.place(x=25, y=50, height=50, width=450)

city_name = StringVar()
list_name = ["Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","Delhi","Puducherry"]

com = ttk.Combobox(win, values=list_name,
                   font=("Times New Roman", 20, "bold"),
                   textvariable=city_name)
com.place(x=25, y=120, height=50, width=450)

W_label = Label(win, text="Weather Climate:",
                font=("Times New Roman", 20))
W_label.place(x=25, y=260, height=50, width=210)

w_label1 = Label(win, text="", font=("Times New Roman", 20))
w_label1.place(x=250, y=260, height=50, width=210)

Wb_label = Label(win, text="Weather Description:",
                 font=("Times New Roman", 17))
Wb_label.place(x=25, y=330, height=50, width=210)

Wb_label1 = Label(win, text="", font=("Times New Roman", 17))
Wb_label1.place(x=250, y=330, height=50, width=210)

temp_label = Label(win, text="Temperature:",
                   font=("Times New Roman", 20))
temp_label.place(x=25, y=400, height=50, width=210)

temp_label1 = Label(win, text="", font=("Times New Roman", 15))
temp_label1.place(x=250, y=400, height=50, width=210)

per_label = Label(win, text="Pressure:",
                  font=("Times New Roman", 20))
per_label.place(x=25, y=470, height=50, width=210)

per_label1 = Label(win, text="", font=("Times New Roman", 20))
per_label1.place(x=250, y=470, height=50, width=210)

done_button = Button(win, text="Done",
                     font=("Times New Roman", 20, "bold"),
                     command=data_get)
done_button.place(y=190, height=50, width=100, x=200)

win.mainloop()
