import keyboard


class Key_Brain:
    def __init__(self):
        self.can_add_to_correct_key_press = True
        self.paragraph = None
        self.correct_key_pressed = 0
        self.incorrect_key_pressed = 0
        self.got_right = 0
        self.got_wrong = 0

    def check_key_pressed(self, paragraph):
        self.paragraph = paragraph
        if keyboard.is_pressed(self.paragraph[0]):
            print(self.paragraph)
            if self.can_add_to_correct_key_press:
                self.correct_key_pressed += 1
                return self.paragraph[1:]
            else:
                self.can_add_to_correct_key_press = True
                return self.paragraph[1:]
            # update gui
        else:
            print(self.paragraph)
            self.can_add_to_correct_key_press = False
            self.incorrect_key_pressed += 1
            return self.paragraph

    def percentage_right_to_wrong(self):
        times_key_was_pressed = self.correct_key_pressed + self.incorrect_key_pressed
        self.got_right = (self.correct_key_pressed / times_key_was_pressed) * 100
        self.got_wrong = (self.incorrect_key_pressed / times_key_was_pressed) * 100

        return self.got_right, self.got_wrong
