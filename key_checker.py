import keyboard


class Key_Brain:
    def __init__(self):
        self.can_add_to_correct_key_press = True
        self.list_of_chars = None
        self.correct_key_pressed = 0
        self.incorrect_key_pressed = 0
        self.got_right = 0
        self.got_wrong = 0

    def check_key_pressed(self, list_of_chars):
        self.list_of_chars = list_of_chars
        if keyboard.is_pressed(self.list_of_chars[0]):
            print(self.list_of_chars)
            if self.can_add_to_correct_key_press:
                self.correct_key_pressed += 1
                self.list_of_chars.pop(0)
                return self.list_of_chars
            else:
                self.can_add_to_correct_key_press = True
                self.list_of_chars.pop(0)
                return self.list_of_chars
            # update gui
        else:
            print(self.list_of_chars)
            self.can_add_to_correct_key_press = False
            self.incorrect_key_pressed += 1
            return self.list_of_chars

    def percentage_right_to_wrong(self):
        times_key_was_pressed = self.correct_key_pressed + self.incorrect_key_pressed
        self.got_right = (self.correct_key_pressed / times_key_was_pressed) * 100
        self.got_wrong = (self.incorrect_key_pressed / times_key_was_pressed) * 100

        return self.got_right, self.got_wrong
