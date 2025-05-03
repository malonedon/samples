import customtkinter
from customtkinter import *
import tkinter
from tkinter import *
from PIL import Image 


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


#window root
root=customtkinter.CTk()
root.geometry("1000x4000 ")
root.title("Gym fitness")

#window frame
frame=CTkFrame(root)
frame.pack()
#background image
bg_image=PhotoImage(file="gym.png")
CTkLabel(root,image=bg_image,text="").place(relwidth=1,relheight=1)

#software name label
software_name="Login"
CTkLabel(root,text=software_name,font=("helvetica",100)).pack()
#signup  entry
fullname=CTkEntry(root,placeholder_text="Enter your Fullname",font=("georgia",20,) ,width=300,corner_radius=50, )
fullname.pack(pady=10)

password=CTkEntry(root,placeholder_text="Enter your Password",font=("georgia",20) ,width=300,corner_radius=50)
password.pack(pady=10)

#button functions
def login():
    tkinter.messagebox.showinfo("Register","Loading")
    root.destroy()
    import  home
    pass

#signup button
register_button_image=PhotoImage(file="register.png",)
CTkButton(root,text="Login",height=50,width=50,command=login).pack(side="left",padx=600)

root.mainloop()
