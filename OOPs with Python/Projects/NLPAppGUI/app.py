from tkinter import *;
from tkinter import messagebox;
from mydb import Database

class NLPApp:
    
    def __init__(self):
        self.db = Database()
        self.root = Tk()
        self.root.title('NLP App')
        self.root.geometry('350x600')
        self.root.configure(bg='#01161E')
        self.login_gui()
        self.root.mainloop()

    def perform_registration(self):
        name = self.entry_name.get()
        email = self.entry_email.get()
        password = self.entry_password.get()

        response = self.db.add_user(name, email, password)

        if response:
            messagebox.showinfo('success', 'Registration Successful.')
            self.login_gui()
        else:
            messagebox.showerror('Error', 'You are already registered wiht us.')

    def perform_login(self):
        email = self.entry_login_email.get()
        password = self.entry_login_password.get()
        
        try:
            response = self.db.search_and_validate_user(email, password)
            if response:
                messagebox.showinfo('Success', 'Login Successful')
                self.home_gui()
        except Exception as e:
            messagebox.showerror('Error', e.args[0])


    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def login_gui(self):
        self.clear()

        title = Label(self.root, text='NLP App', background='#01161E', foreground='white')
        title.pack(pady=(20, 20))
        title.configure(font=('verdana', 24, 'bold'))

        label_email = Label(self.root, text='Email', background= '#01161E', foreground='white')
        label_email.pack(pady=(0, 10))
        label_email.configure(font=('verdana', 14, 'bold'))
        self.entry_login_email = Entry(self.root, width=50)
        self.entry_login_email.pack(ipady=5)

        label_password = Label(self.root, text='Password', background= '#01161E', foreground='white')
        label_password.pack(pady=(0, 10))
        label_password.configure(font=('verdana', 14, 'bold'))
        self.entry_login_password = Entry(self.root, width=50, show='*')
        self.entry_login_password.pack(ipady=5)

        button_login = Button(self.root, text='Login', command=self.perform_login)
        button_login.pack(pady=(10, 10))
        button_login.configure(font=('verdana', 11, 'italic'))

        label_redirect = Label(self.root, text='Not a member?', background='#01161E', foreground='white')
        label_redirect.pack(pady=(10, 10))
        
        button_redirect = Button(self.root, text='Register', command=self.register_gui)
        button_redirect.pack(pady=(10, 0))

    def register_gui(self):
        self.clear()

        title = Label(self.root, text='NLP App', background='#01161E', foreground='white')
        title.pack(pady=(20, 20))
        title.configure(font=('verdana', 24, 'bold'))

        label_name = Label(self.root, text='Name', background= '#01161E', foreground='white')
        label_name.pack(pady=(0, 10))
        label_name.configure(font=('verdana', 14, 'bold'))
        self.entry_name = Entry(self.root, width=50)
        self.entry_name.pack(ipady=5)

        label_email = Label(self.root, text='Email', background= '#01161E', foreground='white')
        label_email.pack(pady=(0, 10))
        label_email.configure(font=('verdana', 14, 'bold'))
        self.entry_email = Entry(self.root, width=50)
        self.entry_email.pack(ipady=5)

        label_password = Label(self.root, text='Password', background= '#01161E', foreground='white')
        label_password.pack(pady=(0, 10))
        label_password.configure(font=('verdana', 14, 'bold'))
        self.entry_password = Entry(self.root, width=50, show='*')
        self.entry_password.pack(ipady=5)

        button_register = Button(self.root, text='Register', command=self.perform_registration)
        button_register.pack(pady=(10, 10))
        button_register.configure(font=('verdana', 11, 'italic'))

        label_redirect = Label(self.root, text='Not a member?', background='#01161E', foreground='white')
        label_redirect.pack(pady=(10, 10))
        
        button_redirect = Button(self.root, text='Login', command=self.login_gui)
        button_redirect.pack(pady=(10, 0))

    def home_gui(self):
        self.clear()

        title = Label(self.root, text='NLP App', background='#01161E', foreground='white')
        title.pack(pady=(20, 20))
        title.configure(font=('lexend', 24, 'bold'))

        sentiment_button = Button(self.root, text='Sentiment Analysis', width=25, command=self.sentiment_gui)
        sentiment_button.pack(pady=(20,20), ipadx=30, ipady=10)
        sentiment_button.configure(font=('lexend', 12))

        ner_button = Button(self.root, text='Named Entity Recognition', width=25, command=self.ner_gui)
        ner_button.pack(pady=(20,20), ipadx=30, ipady=10)
        ner_button.configure(font=('lexend', 12))

        lang_detection_button = Button(self.root, text='Language Detection', width=25, command=self.lang_detection_gui)
        lang_detection_button.pack(pady=(20,20), ipadx=30, ipady=10)
        lang_detection_button.configure(font=('lexend', 12))

    def sentiment_gui(self):
        self.clear()

        title = Label(self.root, text='NLP App', background='#01161E', foreground='white')
        title.pack(pady=(20, 20))
        title.configure(font=('lexend', 24, 'bold'))

        sub_title = Label(self.root, text='Sentiment Analysis', background='#01161E', foreground='white')
        sub_title.pack(pady=(0, 20))
        sub_title.configure(font=('lexend', 16, 'bold'))

        text_label = Label(self.root, text='Enter the text', background='#01161E', foreground='white')
        text_label.pack(pady=(10, 10))
        text_label.configure(font=('lexend', 11))

        self.text_entry = Entry(self.root, width=50)
        self.text_entry.pack(ipady=5)

        analyze_sentiment_button = Button(self.root, text='Analyze Sentiment', command=self.analyze_sentiment)
        analyze_sentiment_button.pack(pady=(20, 20))
        analyze_sentiment_button.configure(font=('lexend', 11))

        go_back_button = Button(self.root, text='Go Back', command=self.home_gui)
        go_back_button.pack(pady=(20, 20))
        go_back_button.configure(font=('lexend', 8))

    def analyze_sentiment(self):
        pass

    def ner_gui(self):
        self.clear()

        title = Label(self.root, text='NLP App', background='#01161E', foreground='white')
        title.pack(pady=(20, 20))
        title.configure(font=('lexend', 24, 'bold'))

        sub_title = Label(self.root, text='Named Entity Recognition', background='#01161E', foreground='white')
        sub_title.pack(pady=(0, 20))
        sub_title.configure(font=('lexend', 16, 'bold'))

        text_label = Label(self.root, text='Enter the text', background='#01161E', foreground='white')
        text_label.pack(pady=(10, 10))
        text_label.configure(font=('lexend', 11))

        self.text_entry = Entry(self.root, width=50)
        self.text_entry.pack(ipady=5)

        entity_label = Label(self.root, text='Enter the Entity Name', background='#01161E', foreground='white')
        entity_label.pack(pady=(10, 10))
        entity_label.configure(font=('lexend', 11))

        self.entity_entry = Entry(self.root, width=50)
        self.entity_entry.pack(ipady=5)

        analyze_entity_button = Button(self.root, text='Analyze Entities', command=self.analyze_entity)
        analyze_entity_button.pack(pady=(20, 20))
        analyze_entity_button.configure(font=('lexend', 11))

        go_back_button = Button(self.root, text='Go Back', command=self.home_gui)
        go_back_button.pack(pady=(20, 20))
        go_back_button.configure(font=('lexend', 8))

    def analyze_entity(self):
        pass

    def lang_detection_gui(self):
        self.clear()

        title = Label(self.root, text='NLP App', background='#01161E', foreground='white')
        title.pack(pady=(20, 20))
        title.configure(font=('lexend', 24, 'bold'))

        sub_title = Label(self.root, text='Language Detection', background='#01161E', foreground='white')
        sub_title.pack(pady=(0, 20))
        sub_title.configure(font=('lexend', 16, 'bold'))

        text_label = Label(self.root, text='Enter the text', background='#01161E', foreground='white')
        text_label.pack(pady=(10, 10))
        text_label.configure(font=('lexend', 11))

        self.text_entry = Entry(self.root, width=50)
        self.text_entry.pack(ipady=5)

        analyze_lang_button = Button(self.root, text='Detect Language', command=self.detect_language)
        analyze_lang_button.pack(pady=(20, 20))
        analyze_lang_button.configure(font=('lexend', 11))

        go_back_button = Button(self.root, text='Go Back', command=self.home_gui)
        go_back_button.pack(pady=(20, 20))
        go_back_button.configure(font=('lexend', 8))

    def detect_language(self):
        pass

nlp_app = NLPApp()