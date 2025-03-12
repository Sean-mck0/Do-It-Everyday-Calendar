from datetime import datetime
import tkinter as tk
from PIL import Image, ImageTk
import time
from tkinter import Toplevel, Label
import json
import os



# Create tkinter window
window = tk.Tk()
today = datetime.now()
current_month = (datetime.now().month - 1)

json_file_path = r"C:\Users\wtfcr\Desktop\coding projects\doiteveryday\button_states.json"


with open(json_file_path, "r") as file:
    data = json.load(file)
    



month_key = datetime.now().strftime("%B")



# Create a list of the number of days in each month
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]



# Load images
image1 = Image.open(r"C:\Users\wtfcr\Pictures\Saved Pictures\off_button.png")
image2 = Image.open(r"C:\Users\wtfcr\Pictures\Saved Pictures\on_button.png")

# Convert PIL images to PhotoImage
off_button = ImageTk.PhotoImage(image1)
on_button = ImageTk.PhotoImage(image2)

# Function to determine if the year is a leap year and amend days in February
def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days_in_month[1] = 29
    else:
        days_in_month[1] = 28

# Function to toggle the button image
def toggle_button(button):
    if button.config('image')[-1] == str(off_button):
        button.config(image=on_button)
        data[month_key][button.cget('text')] = 1
        
        with open(json_file_path, "w") as file:
            json.dump(data, file)

    else:
        button.config(image=off_button)


#create a countdown function
def countdown(t, label):
    while t:
        minutes, seconds = divmod(t, 60)
        timer = timer = '{:02d}:{:02d}'.format(minutes, seconds) 
        label.config(text=f"time remaining: {timer}")
        label.update()
        time.sleep(1) 
        t -= 1
    label.config(text="you have completed your daily task")
    label.update()



#function to create seperate window
def create_timer_win():
    top = Toplevel()
    top.geometry("180x100")
    top.title("timer")
    label2 = Label(top, text="time remaining: ")
    label2.pack()
    countdown(10, label2)

    

# Function to create a button with toggle functionality
def create_button(row, column, day):
    initial_image = off_button if data[month_key][day] == 0 else on_button
    # Create the button and pass the toggle function with the button as an argument
    button = tk.Button(window, image=initial_image,text = day, command=lambda: [toggle_button(button), create_timer_win()])
    button.grid(row=row, column=column)

# Create the button using the function
row = 1
column = 0
#creates a funciton to create the buttons for each day in the month
for x in range(days_in_month[current_month]):
    
    create_button(row, column, x)
    if column == 6:
        row +=1
        column = 0
    else:
        column +=1


# Set window title
window.title("Do It Everyday")
window.mainloop()
