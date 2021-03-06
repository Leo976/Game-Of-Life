from const import *
from square import Square
import copy
import random

class Matrix:

    def __init__(self):

        file = open('matrix.txt')

        text = file.read()
        text = text.split()

        auto_generate = text[len(text) - 1]

        text = text[:-3]  # delete 'auto_generate', '=' and 'True'
        text = [[int(j) for j in list(i)] for i in text]

        self.__matrix = text
        self.__line_count = len(self.__matrix)
        self.__column_count = len(self.__matrix[0])

        file.close()

        if bool(auto_generate):
            for line in range(self.__line_count):
                for column in range(self.__column_count):
                    self.__matrix[line][column] = random.randint(0, 1)

    def print(self):

        for line in self.__matrix:
            print(*line, sep='')

    def draw(self, window):

        for line in range(self.__line_count):
            for column in range(self.__column_count):

                if self.__matrix[line][column] == 0:
                    square = Square(SIZE_CELL_X, SIZE_CELL_Y, column * SIZE_CELL_X, line * SIZE_CELL_Y, WHITE)
                else:
                    square = Square(SIZE_CELL_X, SIZE_CELL_Y, column * SIZE_CELL_X, line * SIZE_CELL_Y, RED)

                square.draw(window)

    def export(self):

        txt = ''

        for line in self.__matrix:
            for case in line:
                txt += str(case)
            txt += '\n'

        file = open('new_matrix.txt', 'w+')
        file.write(txt)
        file.close()

    #   refreshes the matrix, transforms the cells
    def update(self):

        matrix_copy = copy.deepcopy(self.__matrix)

        for line in range(self.__line_count):
            for column in range(self.__column_count):

                cell_count = self.__cell_count_around(line, column)

                if matrix_copy[line][column] == 0 and cell_count == 3:
                    matrix_copy[line][column] = 1

                elif matrix_copy[line][column] == 1 and (cell_count > 3 or cell_count < 2):
                    matrix_copy[line][column] = 0

        self.__matrix = copy.deepcopy(matrix_copy)

    #   transforms a cell if the player clicks on a case
    def switch_cell(self, x, y):
        print("no")
        # if (FIRST_POSITION_CELL_X <= x <= FIRST_POSITION_CELL_X + SIZE_CELL_X * self.__line_count and
        #         FIRST_POSITION_CELL_Y <= y <= FIRST_POSITION_CELL_Y + SIZE_CELL_Y * self.__column_count):
        #     line = (x - FIRST_POSITION_CELL_X) // SIZE_CELL_X
        #     column = (y - FIRST_POSITION_CELL_Y) // SIZE_CELL_Y
        #
        #     self.__matrix[line][column] = 0 if self.__matrix[line][column] == 1 else 1

    #   counts the cells number around a case
    def __cell_count_around(self, line, column):

        cell_count = -1 if self.__matrix[line][column] == 1 else 0

        for new_line in range(line - 1, line + 2):
            for new_column in range(column - 1, column + 2):
                if not (self.__out_of_dimension(new_line, new_column)):
                    cell_count += self.__matrix[new_line][new_column]

        return cell_count

    #   checks if the values are not out dimension of the matrix
    def __out_of_dimension(self, line, column):

        return line < 0 or column < 0 or line >= self.__line_count or column >= self.__column_count
