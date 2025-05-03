from customtkinter import *
from tkinter import *
from PIL import Image 
import customtkinter 


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")



root=CTk()
root.geometry("500x500 ")
img=CTkImage(light_image=Image.open("gym.webp"), size=(900,900))
CTkScrollableFrame(root, image=img).pack()

root.mainloop()