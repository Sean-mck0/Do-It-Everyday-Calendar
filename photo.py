import tkinter as tk
from PIL import Image, ImageTk
window = tk.Tk()
image1 = Image.open("C:\\Users\\wtfcr\\Pictures\\Saved Pictures\\off_button.png")

off_button = ImageTk.PhotoImage(image1)

#def create_button(buttonname):
#    buttonname = tk.Button(window, image=off_button)




#create_button("buttonname")
button1 = tk.Button(window, image=off_button)

window.title("Do It Everyday")
