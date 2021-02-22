from const import *


def check_click_button(x, y):

    for button in range(1, 4):

        position = [FIRST_TXT_POSITION, SECOND_TXT_POSITION, THIRD_TXT_POSITION][button - 1]

        if (position[0] + 200 <= x <= position[0] + 200 + SIZE_CELL_X and
                position[1] <= y <= position[1] + SIZE_CELL_Y):

            return button

    return 0