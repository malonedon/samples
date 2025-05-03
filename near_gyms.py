import customtkinter
from customtkinter import *
from tkinter import *
import tkinter
from PIL import Image 


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


#window root
root=customtkinter.CTk()
root.geometry("1000x1000 ")
root.title("Gym fitness")

#window frame
frame=CTkFrame(root)
frame.pack()
#background image
bg_image=PhotoImage(file="weights_background.png")
CTkLabel(root,image=bg_image,text="").place(relwidth=1,relheight=1)

#software name label
software_name="Gym fitness home"
CTkLabel(root,text=software_name,font=("helvetica",60)).pack()
#signup  entry
search_entry=CTkEntry(root,placeholder_text="Search food diat",font=("georgia",20,) ,width=300,corner_radius=50, )
search_entry.pack()
search_button=CTkButton(root,text="Search")
search_button.pack()
#segmented button
def choice(x):
    value=seg.get()
    if  value == "Near gyms":
        tkinter.messagebox.showinfo("",value)
        root.destroy()
        import near_gyms
    if  value == "Categories":
        tkinter.messagebox.showinfo("",value)
        root.destroy()
        import gym_categories
    if  value == "My profile":
        tkinter.messagebox.showinfo("",value)
        root.destroy()
        import my_profile
        


        
my_values=["Near gyms","Categories","My profile"]
seg=CTkSegmentedButton(root,values=my_values,command=choice,corner_radius=50,height=50,width=200)
seg.set("Near gyms")
seg.pack()

map=PhotoImage(file="categories/map/map.png")
CTkButton(root,text="",image=map,width=50,height=50,).pack()


#signup button
register_button_image=PhotoImage(file="register.png",)
CTkButton(root,text="Logout",height=50,width=50).pack(side="left",padx=600)

root.mainloop()
