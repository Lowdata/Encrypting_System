from cryptography.fernet import Fernet
import tkinter as tk                # python 3
from tkinter import font as tkfont  # python 3

    # Generating the key and writing it to a file
def genwrite_key():
    key = Fernet.generate_key()
    with open("pass.key", "wb") as key_file:
        key_file.write(key)
# Function to load the key
def call_key():
                  return open("pass.key", "rb").read()
   
    
    
class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")
        self.geometry("800x400+10+10")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()



class StartPage(tk.Frame):

            
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Welcome to Exposys Lab ", font=controller.title_font, fg='red')
        label.pack(side="top", fill="x", pady=10)
        lbl=tk.Label(self, text="Username", fg='blue', font=("Helvetica", 10))
        lbl.place(x=100, y=50)
        lbl=tk.Label(self, text="Password", fg='red', font=("Helvetica", 10))
        lbl.place(x=100, y=90)
        txtfld1=tk.Entry(self, text="USERNAME",bd=5)
        txtfld1.place(x=250, y=50)
        result=txtfld1.get()
        txtfld2=tk.Entry(self, text="PASSWORD", bd=5)
        txtfld2.place(x=250, y=90)
        button1 = tk.Button(self, text="Login",command=lambda: [self.controller.show_frame("PageOne"),self.getvalue( txtfld1,txtfld2)])

        button1.pack(pady=80)
    def getvalue(self,x,y):
        result1=x.get()
        print(result1)
        result2=y.get()
        print(result2)
        


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Enter your message which you want to send to user", font=controller.title_font)
        label.pack(side="top", fill="x", pady=5)
        button = tk.Button(self, text="Login",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack(padx=100,pady=5)
        label = tk.Label(self, text="Write text to encrypt:")
        label.place(x=10, y=80)
        txtfld=tk.Entry(self, text="ENCRPYT", bd=5,width=70)
        txtfld.place(x=20, y=100)
        button1 = tk.Button(self, text="ENCRPYT",
                           command=lambda: [self.getvalue(txtfld,txtfld1)])
        button1.pack(padx=20,pady=50)
        label = tk.Label(self, text="Decrpyted code:")
        label.place(x=10, y=180)
        txtfld1=tk.Entry(self, text="ENCRPYT", bd=5,width=70)
        txtfld1.place(x=20, y=200)
    def getvalue(self,x,y):
        result=x.get()
        genwrite_key()
        key = call_key()
        slogan = result.encode()
        a = Fernet(key)
        coded_slogan = a.encrypt(slogan)
        print(coded_slogan)
        b = Fernet(key)
        decoded_slogan = b.decrypt(coded_slogan)
        print("decoded_message is",decoded_slogan)
        y.insert(tk.END,decoded_slogan)
       


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()