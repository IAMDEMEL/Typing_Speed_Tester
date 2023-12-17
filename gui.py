from sentence_generator import Brain
from key_checker import Key_Brain
from tkinter import *
import time

MINUTE = 60
FONT = 'Helvetica 15 bold'
begone = False


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
        self.timed = None
        self.user_chose = None
        self.got_right = None
        self.got_wrong = None
        self.clock = None
        self.first_char = ''
        self.paragraphs_to_use = ''
        self.checker = None
        self.input_ = None
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
        self.timed = timed
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
        self.user_chose = (normal, timed, how_many)
        self.paragraphs_to_use = ''
        self.checker = Key_Brain()
        self.input_ = StringVar()
        generator = Brain()
        transition(self.window)
        self.window.geometry('1080x720')
        self.countdown = 1
        self.pages = 1

        if normal and timed:
            self.paragraphs_to_use = generator.generate_normal_paragraph()
            self.update_paragraph(how_many, timed)
        elif not normal and timed:
            self.paragraphs_to_use = generator.generate_random_paragraph()
            self.update_paragraph(how_many, timed)
        elif normal and not timed:
            for i in range(how_many):
                self.paragraphs_to_use += generator.generate_normal_paragraph()
            self.update_paragraph(how_many, timed)
        elif not normal and not timed:
            for i in range(how_many):
                self.paragraphs_to_use = {generator.generate_random_paragraph()}
            self.update_paragraph(how_many, timed)

    def update_paragraph(self, how_many, timed):
        self.canvas = Canvas(self.window, width=500, height=300, bg="yellow", relief=SUNKEN)
        self.input_box = Entry(self.window, textvariable=self.input_)
        self.clock = Label(self.window, text='00', font=FONT)
        self.first_char = self.paragraphs_to_use[0]
        wrap_width = 380
        txt_start_x = 10
        txt_start_y = 10
        if timed:
            self.countdown = how_many * MINUTE
            self.clock.config(text=str(time.strftime("%M:%S", time.gmtime(float(self.countdown)))))
            self.clock.pack(pady=(50, 25))
            self.canvas.pack(pady=(0, 25))
            self.input_box.pack()
            self.current_text = self.canvas.create_text(txt_start_x, txt_start_y, text=self.paragraphs_to_use,
                                                        fill="black", font=FONT, width=wrap_width,
                                                        anchor=NW)
            self.first_character = self.canvas.create_text(txt_start_x, txt_start_y, text=self.first_char, fill="blue",
                                                           font=f'{FONT} underline', width=wrap_width,
                                                           anchor=NW)
            self.input_.trace('w', self.check_pressed)
        else:
            self.pages = self.pages * how_many
            self.canvas.pack(pady=(50, 25))
            self.input_box.pack()
            self.current_text = self.canvas.create_text(txt_start_x, txt_start_y, text=self.paragraphs_to_use,
                                                        fill="black", font=FONT, width=wrap_width,
                                                        anchor=NW)
            self.first_character = self.canvas.create_text(txt_start_x, txt_start_y, text=self.first_char, fill="blue",
                                                           font=f'{FONT} underline', width=wrap_width,
                                                           anchor=NW)
            self.input_.trace('w', self.check_pressed)

    def check_pressed(self, *args):
        global begone
        if not begone:
            begone = True
            self.reduce_countdown()

        new_par = self.checker.check_key_pressed(paragraph=self.paragraphs_to_use, user_pressed=self.input_.get())
        if len(new_par) >= 1:
            if self.first_char == new_par[0] and len(new_par) == len(self.paragraphs_to_use):
                self.canvas.itemconfig(self.first_character, fill='red')
                self.input_box.delete(0, END)
            else:
                self.first_char = new_par[0]
                self.paragraphs_to_use = new_par
                self.canvas.itemconfig(self.first_character, fill='blue')
                self.canvas.itemconfig(self.first_character, text=self.first_char)
                self.canvas.itemconfig(self.current_text, text=self.paragraphs_to_use)
                self.input_box.delete(0, END)
        else:
            self.end_session()

    def end_session(self):
        global begone
        begone = False
        transition(self.window)
        self.window.geometry('400x250')
        self.got_right, self.got_wrong = self.checker.percentage_right_to_wrong()
        right_accuracy = Label(self.window, text=f'{self.got_right}%')
        wrong_accuracy = Label(self.window, text=f'{self.got_wrong}%')
        try_again_but = Button(self.window, text='Try Again', command=lambda: self.start_typing(
            self.user_chose[0], self.user_chose[1], self.user_chose[2]))
        menu_but = Button(self.window, text='Menu', command=self.mode_selection)
        right_accuracy.pack()
        wrong_accuracy.pack()
        try_again_but.pack()
        menu_but.pack()

    def reduce_countdown(self):
        if self.countdown > 0:
            if begone:
                self.countdown -= 1
                self.clock.config(text=str(time.strftime("%M:%S", time.gmtime(float(self.countdown)))))
                self.window.after(1000, self.reduce_countdown)
        else:
            if self.timed:
                self.end_session()
