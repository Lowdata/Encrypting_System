from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import SEL, Tk, font as tkfont


#we need to generate a key for the project 

def generate_key():
    key = Fernet.generate_key()
    with open("Generated_key.key", "wb") as key_file:
        key_file.write(key)

#We need a key calling function now
def key_caller():
    return open("Generated_key.key", "rb").read()

#Now comes the interface
#Create a class first

class Part1(tk,Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk__init__(self, *args, **kwargs)

#Yup its the title
        self.title_font = tkfont.Font(damily='Helvetica', size=20, weight="bold", slant="italic")

    #Now we will create containers and frames and in the containers we will stack the frames 


        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames ={}

        for F in (StartPage, FirstPage):

            page_name = F.__name__
        
            frame =F(parent=container, controller=self)
            self.frames[page_name] = frame
    #so now we will be putting all the pages in the same place on top of each other and the one on the top will be visible to the user.
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("StartPage")
        self.geometry("800x400+10+10")
    
    def show_frame(self, page_name):
        #show a frame for the given page name
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

