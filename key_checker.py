class Key_Brain:
    def __init__(self):
        self.can_add_to_correct_key_press = True
        self.paragraph = None
        self.correct_key_pressed = 0
        self.incorrect_key_pressed = 0
        self.got_right = 0
        self.got_wrong = 0

    def check_key_pressed(self, paragraph, user_pressed):
        self.paragraph = paragraph
        if user_pressed == self.paragraph[0]:
            if self.can_add_to_correct_key_press:
                self.correct_key_pressed += 1
                return self.paragraph[1:]
            else:
                self.can_add_to_correct_key_press = True
                return self.paragraph[1:]
        else:
            self.can_add_to_correct_key_press = False
            self.incorrect_key_pressed += 1
            return self.paragraph

    def percentage_right_to_wrong(self):
        times_key_was_pressed = self.correct_key_pressed + self.incorrect_key_pressed
        self.got_right = round((self.correct_key_pressed / times_key_was_pressed) * 100, 1)
        self.got_wrong = round((self.incorrect_key_pressed / times_key_was_pressed) * 100, 1)

        return self.got_right, self.got_wrong
