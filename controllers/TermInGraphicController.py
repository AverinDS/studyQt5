from helpers.ConstHolder import TranslatingConst
from helpers.FolderParser import FolderParser
from helpers.TermHelper import TermHelper


class TermInGraphicController:
    terms = []
    table_data = []
    termHelper = TermHelper()
    folder_parser = FolderParser()
    mode = TranslatingConst.NUMBER_SOFT_MATRIX

    def set_mode(self, mode):
        self.mode = mode

    def get_table_data(self, filename):
        if self.mode == TranslatingConst.NUMBER_SOFT_MATRIX:
            return self.get_number_soft_matrix_data(filename=filename)

        if self.mode == TranslatingConst.NUMBER_SOFT_VECTOR:
            return self.get_number_soft_vector_data(filename=filename)

        if self.mode == TranslatingConst.NUMBER_LINGUISTIC:
            return self.get_number_linguistic(filename=filename)

        if self.mode == TranslatingConst.NUMBER_LINGUISTIC_SOFT:
            return self.get_number_linguistic_soft(filename=filename)

        if self.mode == TranslatingConst.NUMBER_NUMBER:
            return self.get_number_number(filename=filename)

    def get_number_soft_matrix_data(self, filename):
        rows = []
        self.terms = self.termHelper.get_terms(filename=filename)
        points_x, points_y = self.folder_parser.get_points_from_file_by_filename(filename=filename)
        for i in range(0, len(points_x)):
            row = [points_x[i], points_y[i]]
            for term in self.terms:
                row.append(self.get_probability_to_terms(points_y[i], term))
            rows.append(row)
        term_names = [term[0] for term in self.terms]
        return rows, term_names

    def get_number_soft_vector_data(self, filename):
        rows, term_names = self.get_number_soft_matrix_data(filename=filename)
        for i in range(0, len(rows)):
            vector = "("
            for j in range(2, len(rows[i])):
                vector += str(rows[i][j]) + "; "
            vector += ")"
            rows[i] = vector
        return rows, term_names

    def get_number_linguistic(self, filename):
        rows, term_names = self.get_number_soft_matrix_data(filename)
        rows = self.remove_input_data(rows)
        for i in range(0, len(rows)):
            rows[i] = term_names[rows[i].index(max(rows[i]))]
        return rows, term_names

    def get_number_linguistic_soft(self, filename):
        return self.get_number_soft_matrix_data(filename)

    def get_number_number(self, filename):
        return self.get_number_linguistic(filename)

    def remove_input_data(self, rows):
        for i in range(0, len(rows)):
            rows[i] = [rows[i][j] for j in range(2, len(rows[i]))]
        return rows


    def get_probability_to_terms(self, y, term):
        a = float(term[1])
        b = float(term[2])
        c = float(term[3])

        if a <= y <= b:
            return 1 - ((b - y) / (b - a))

        if b <= y <= c:
            return 1 - ((y - b) / (c - b))

        return 0
