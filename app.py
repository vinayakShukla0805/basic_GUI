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

        label2 = Label(self.root,text='Enter Password',width=40)
        label2.pack(pady=(10,10))

        self.password_input = Entry(self.root,width=50,show='*')
        self.password_input.pack(pady=(5,10),ipady=4)

        login_btn = Button(self.root,text='Login',width=30,height=2)
        login_btn.pack(pady=(5,5))

        label3 = Label(self.root,text='Not registered?',width=30)
        label3.pack(pady=(10,5))

        redirect_btn = Button(self.root,text='register',command=self.register_gui)
        redirect_btn.pack()

    def register_gui(self):
        self.clear_gui()
        print('Registration Open')

    def clear_gui(self):
        for i in self.root.pack_slaves():
            i.destroy()
nlp = NLPApp()