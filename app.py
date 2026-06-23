from tkinter import *


class NLPApp:
    def __init__(self):
        self.root = Tk()
        self.root.title("NLPApp")
        self.root.iconbitmap('resources/favicon.ico')
        self.root.geometry('400x600')
        self.root.config(bg='#34495E')
        self.loginGUI()
        self.root.mainloop()

    def loginGUI(self):
        heading = Label(self.root,text='NLPApp',bg='#34495E',fg='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))

        label1 = Label(self.root,text='Enter Email',width=40)
        label1.pack(pady=(10,10))

        self.email_input = Entry(self.root,width=50)
        self.email_input.pack(pady=(5,10),ipady=4)
nlp = NLPApp()