from sentence_generator import Brain
from key_checker import Key_Brain
from tkinter import *
import keyboard

MINUTE = 60


def transition(current_window):
    for widget in current_window.winfo_children():
        widget.destroy()


def center_window(current_window):
    width = 400
    height = 200
    screen_width = current_window.winfo_screenwidth()  # Width of the screen
    screen_height = current_window.winfo_screenheight()  # Height of the screen

    # Calculate Starting X and Y coordinates for Window
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)

    current_window.geometry('%dx%d+%d+%d' % (width, height, x, y))


class GUI:
    def __init__(self):
        self.input_box = None
        self.first_character = ''
        self.current_text = ''
        self.canvas = None
        self.pages = 1
        self.countdown = 0
        self.window = Tk()
        # print('hello world I am GUI Brain')
        center_window(current_window=self.window)
        Label(self.window, text='Typing Speed Tester').pack(pady=(50, 25))
        Button(self.window, text='Start', command=self.mode_selection).pack()
        self.window.mainloop()

    def mode_selection(self):
        transition(self.window)
        norm_mode_but = Button(self.window, text='Normal Mode', command=lambda: self.timed_or_untimed(normal=True))
        rand_mode_but = Button(self.window, text='Random Mode', command=lambda: self.timed_or_untimed(normal=False))
        norm_mode_but.pack(pady=(50, 25))
        rand_mode_but.pack()

    def timed_or_untimed(self, normal: bool):
        transition(self.window)
        timed_mode_but = Button(self.window, text='Timed',
                                command=lambda: self.amount_to_do(normal=normal, timed=True))
        untimed_mode_but = Button(self.window, text='Untimed',
                                  command=lambda: self.amount_to_do(normal=normal, timed=False))
        timed_mode_but.pack(pady=(50, 25))
        untimed_mode_but.pack()

    def amount_to_do(self, normal: bool, timed: bool):
        transition(self.window)
        if timed:
            mode_1min_but = Button(self.window, text='1 Minute',
                                   command=lambda: self.start_typing(normal=normal, timed=timed, how_many=1))
            mode_3min_but = Button(self.window, text='3 Minutes',
                                   command=lambda: self.start_typing(normal=normal, timed=timed, how_many=3))
            mode_5min_but = Button(self.window, text='5 Minutes',
                                   command=lambda: self.start_typing(normal=normal, timed=timed, how_many=5))
        else:
            mode_1min_but = Button(self.window, text='1 Page',
                                   command=lambda: self.start_typing(normal=normal, timed=timed, how_many=1))
            mode_3min_but = Button(self.window, text='3 Pages',
                                   command=lambda: self.start_typing(normal=normal, timed=timed, how_many=3))
            mode_5min_but = Button(self.window, text='5 Pages',
                                   command=lambda: self.start_typing(normal=normal, timed=timed, how_many=5))
        mode_1min_but.pack(pady=(50, 25))
        mode_3min_but.pack(pady=(0, 25))
        mode_5min_but.pack()

    def start_typing(self, normal: bool, timed: bool, how_many: int):
        input_ = StringVar()
        generator = Brain()
        checker = Key_Brain()
        transition(self.window)
        self.window.geometry('1080x720')
        self.canvas = Canvas(self.window, width=500, height=300, bg="yellow", relief=SUNKEN)
        self.canvas.pack(pady=(50, 25))
        self.input_box = Entry(self.window, textvariable=input_)
        self.input_box.pack()
        self.countdown = 1
        self.pages = 1
        wrap_width = 380
        txt_start_x = 10
        txt_start_y = 10
        # Test   ------------
        text = ''
        if normal:
            text = 'normal'
        else:
            text = 'random'
        # Test End ------------
        if normal:
            paragraphs_to_use = generator.generate_normal_paragraph()
            first_character = paragraphs_to_use[0]

            if timed:
                self.countdown = how_many * MINUTE
                self.current_text = self.canvas.create_text(txt_start_x, txt_start_y, text=paragraphs_to_use, fill="black", font='Helvetica 15 bold', width=wrap_width, anchor=NW)
                self.first_character = self.canvas.create_text(txt_start_x, txt_start_y, text=first_character, fill="blue", font='Helvetica 15 bold underline', width=wrap_width, anchor=NW)
                print(f"{self.countdown} secs on the clock for {text} paragraph This paragraph is timed.")
            else:
                self.pages = self.pages * how_many
                self.canvas.create_text(0, 50, text=paragraphs_to_use, fill="black", font='Helvetica 15 bold underline', width=wrap_width, anchor=NW)
                print(f"{self.pages} pages to type for {text} paragraph. This paragraph is untimed.")
        else:
            paragraphs_to_use = generator.generate_random_paragraph()
            if timed:
                self.countdown = how_many * MINUTE
                self.canvas.create_text(0, 50, text=paragraphs_to_use, fill="black", font='Helvetica 15 bold underline', width=wrap_width, anchor=NW)
                print(f"{self.countdown} secs on the clock for {text} paragraph This paragraph is timed.")
            else:
                self.pages = self.pages * how_many
                self.canvas.create_text(0, 50, text=paragraphs_to_use, fill="black", font='Helvetica 15 bold underline', width=wrap_width, anchor=NW)
                print(f"{self.pages} pages to type for {text} paragraph. This paragraph is untimed.")
