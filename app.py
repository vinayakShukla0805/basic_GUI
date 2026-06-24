from tkinter import *


class NLPApp:
    def __init__(self):
        self.root = Tk()
        self.root.title("NLPApp")
        try:
            self.root.iconbitmap('resources/favicon.ico')
        except:
            pass
        self.root.geometry('400x600')
        self.root.config(bg="#34495E")
        self.loginGUI()
        self.root.mainloop()

    def loginGUI(self):
        self.clear_gui()
        heading = Label(self.root,text='NLPApp',bg="#FFFFFF",fg='black')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))

        label1 = Label(self.root,text='Enter Email',width=40,bg="#FFFFFF",fg='black')
        label1.pack(pady=(10,10))

        self.email_input = Entry(self.root,width=50,bg="#FFFFFF",fg='black')
        self.email_input.pack(pady=(5,10),ipady=4)

        label2 = Label(self.root,text='Enter Password',width=40,bg="#FFFFFF",fg='black')
        label2.pack(pady=(10,10))

        self.password_input = Entry(self.root,width=50,show='*',bg="#FFFFFF",fg='black')
        self.password_input.pack(pady=(5,10),ipady=4)

        login_btn = Button(self.root,text='Login',width=30,height=2,command=self.login)
        login_btn.pack(pady=(5,5))

        label3 = Label(self.root,text='Not registered?',width=30,bg="#FFFFFF",fg='black')
        label3.pack(pady=(10,5))

        redirect_btn = Button(self.root,text='register',command=self.register_gui)
        redirect_btn.pack()

    def register_gui(self):
        self.clear_gui()
        heading = Label(self.root,text='NLPApp',bg="#FFFFFF",fg='black')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))

        label0 = Label(self.root,text='Enter Name',width=40,bg="#FFFFFF",fg='black')
        label0.pack(pady=(10,10))

        self.name_input = Entry(self.root,width=50,bg="#FFFFFF",fg='black')
        self.name_input.pack(pady=(5,10),ipady=4)

        label1 = Label(self.root,text='Enter Email',width=40,bg="#FFFFFF",fg='black')
        label1.pack(pady=(10,10))

        self.email_input = Entry(self.root,width=50,bg="#FFFFFF",fg='black')
        self.email_input.pack(pady=(5,10),ipady=4)

        label2 = Label(self.root,text='Enter Password',width=40,bg="#FFFFFF",fg='black')
        label2.pack(pady=(10,10))

        self.password_input = Entry(self.root,width=50,show='*',bg="#FFFFFF",fg='black')
        self.password_input.pack(pady=(5,10),ipady=4)

        register_btn = Button(self.root,text='Register',width=30,height=2,command=self.register)
        register_btn.pack(pady=(5,5))

        label3 = Label(self.root,text='Already register?',width=30,bg="#FFFFFF",fg='black')
        label3.pack(pady=(10,5))

        redirect_btn = Button(self.root,text='Login',command=self.loginGUI)
        redirect_btn.pack()

    def clear_gui(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def login(self):
        email = self.email_input.get()
        password = self.password_input.get()
        # Add login logic here
        print(f"Login attempt with email: {email}")

    def registering(self):
        # fetch the from the exiting GUI
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()
        # Add register logic here
        print(f"Register attempt with name: {name}, email: {email}")

nlp = NLPApp()