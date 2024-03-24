from tkinter import *
from datetime import timedelta



class Timer:
    def __init__(self, master):
        self.master = master
        self.counter = timedelta(seconds=0)
        self.running = False

        self.label = Label(master, text="Se Tester !", fg="black", font="Verdana 30 bold")
        self.label.pack()

        self.frame = Frame(master)
        self.frame.pack(anchor='center', pady=5)

        self.start_button = Button(self.frame, text="Start", width=6, command=self.start)
        self.stop_button = Button(self.frame, text='Stop', width=6, state='disabled', command=self.stop)
        self.reset_button = Button(self.frame, text='Reset', width=6, state='disabled', command=self.reset)

        self.start_button.pack(side="left")
        self.stop_button.pack(side="left")
        self.reset_button.pack(side="left")



    def format_time(self):
        minutes, seconds = divmod(self.counter.seconds, 60)
        return '{:02d}:{:02d}'.format(minutes, seconds)

    def counter_label(self):
        if self.running:
            string = self.format_time()
            self.label.config(text=string)
            self.counter += timedelta(seconds=1)
        self.label.after(1000, self.counter_label)

    def start(self):
        self.running = True
        self.counter_label()
        self.start_button['state'] = 'disabled'
        self.stop_button['state'] = 'normal'
        self.reset_button['state'] = 'normal'

    def stop(self):
        self.running = False
        self.start_button['state'] = 'normal'
        self.stop_button['state'] = 'disabled'
        self.reset_button['state'] = 'normal'

    def reset(self):
        self.counter = timedelta(seconds=0)
        if not self.running:
            self.reset_button['state'] = 'disabled'
            self.label['text'] = 'Se tester'
        else:
            self.label['text'] = 'Démarrage'



