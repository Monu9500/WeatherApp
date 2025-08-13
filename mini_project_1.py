from tkinter import *
from tkinter import ttk

import requests


city_name="jodhpur"
data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city_name+"&appid=642e01ce32544b5d4d9b19f3da124a99").json()
print(data)











# win=Tk()
# win.title("Whether Detection")
# win.config(bg="blue")
# win.geometry("500x570")

# name_label=Label(win,text="Whether Detection",
#                  font=("Time New Roman",30,"bold"))
# name_label.place(x=25,y=50,height=50,width=450)


# list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
# com = ttk.Combobox(win,text="Whether Detection",values=list_name,font=("Time New Roman",20,"bold"))
# com.place(x=25,y=120,height=50,width=450)



# done_button = Button(win,text="Done",
#                      font=("Time New Roman",20,"bold"))
# done_button.place(y=190,height=50,width=100,x=200)


# W_label=Label(win,text="Whether Climate:",
#                  font=("Time New Roman",20))
# W_label.place(x=25,y=260,height=50,width=210)

# w_label1=Label(win,text="",
#                  font=("Time New Roman",20))
# w_label1.place(x=250,y=260,height=50,width=210)





# Wb_label=Label(win,text="Whether Description:",
#                  font=("Time New Roman",17))
# Wb_label.place(x=25,y=330,height=50,width=210)

# Wb_label1=Label(win,text="",
#                  font=("Time New Roman",17))
# Wb_label1.place(x=250,y=330,height=50,width=210)




# temp_label=Label(win,text="Temperature:",
#                  font=("Time New Roman",20))
# temp_label.place(x=25,y=400,height=50,width=210)

# temp_label1=Label(win,text="",
#                  font=("Time New Roman",20))
# temp_label1.place(x=250,y=400,height=50,width=210)




# per_label=Label(win,text="Pressure:",
#                  font=("Time New Roman",20))
# per_label.place(x=25,y=470,height=50,width=210)

# per_label1=Label(win,text="",
#                  font=("Time New Roman",20))
# per_label1.place(x=250,y=470,height=50,width=210)


# win.mainloop()