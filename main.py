from sentence_generator import Brain
from key_checker import Key_Brain
generator = Brain()
checker = Key_Brain()


def convert_paragraph_to_list(paragraph: str):
    characters_in_paragraph = [x for x in paragraph]
    return characters_in_paragraph


def normal_paragraph():
    characters_in_paragraph = convert_paragraph_to_list(generator.generate_normal_paragraph())
    # This normal paragraph functon should give options for timed or untimed tests
    # then the timed and untimed options should show timed options (1, 3, and 5 minutes) untimed (1 , 2 , and 3 pages)
    # then we would check if key is being pressed after test begins but this is a prototype
    while True:
        checker.check_key_pressed(characters_in_paragraph)



def random_paragraph():
    characters_in_paragraph = convert_paragraph_to_list(generator.generate_random_paragraph())
    # This normal paragraph functon should give options for timed or untimed tests
    # then the timed and untimed options should show timed options (1, 3, and 5 minutes) untimed (1 , 2 , and 3 pages)
    # then we would check if key is being pressed after test begins but this is a prototype
    while True:
        checker.check_key_pressed(characters_in_paragraph)


def start_app():
    # Display GUI
    # rand but command is 'random_paragraph()' and normal but is 'normal_paragraph()'
    user_input = int(input('Enter "1" for Normal Paragraph and "2" for Random Paragraph: '))
    if user_input == 1:
        normal_paragraph()
    else:
        random_paragraph()


# untimed version stops when at the end of the list.
#  - page version range from 1-3 pages worth of paragrapghs
# timed version will stop when the countdown ends
#  - 1 - 3 minutes

# GUI will be done here

start_app()
