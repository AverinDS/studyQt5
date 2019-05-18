from helpers.ConstHolder import TranslatingConst, TermSetting
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
            return self.get_number_linguistic_soft(filename=filename, isSingleResult=True)

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

    def get_number_linguistic_soft(self, filename, isSingleResult=False):
        rows, term_names = self.get_number_soft_matrix_data(filename)
        rows = self.remove_input_data(rows)
        probabilities = []
        for i in range(0, len(rows)):
            probabilities.append(max(rows[i]))
            rows[i] = term_names[rows[i].index(max(rows[i]))]
        if not isSingleResult:
            return rows, term_names, probabilities
        else:
            for i in range(0, len(rows)):
                rows[i] = str(rows[i]) + " (" + str(probabilities[i]) + ")"
            return rows, term_names

    def get_number_linguistic(self, filename):
        rows, term_names, probabilities = self.get_number_linguistic_soft(filename)
        return rows, term_names

    def get_number_number(self, filename):
        rows, term_names = self.get_number_soft_matrix_data(filename)
        terms = self.termHelper.get_terms(filename=filename)
        numbers = []
        for i in range(0, len(rows)):
            sum_probabilities = 0
            sum_probabilities_x = 0
            for j in range(2, len(term_names) + 2):
                sum_probabilities_x += float(terms[j-2][2]) * rows[i][j]
                sum_probabilities += rows[i][j]
            numbers.append(sum_probabilities_x / sum_probabilities)

        for i in range(0, len(rows)):
            rows[i] = numbers[i]
        return rows, term_names

    def remove_input_data(self, rows):
        for i in range(0, len(rows)):
            rows[i] = [rows[i][j] for j in range(2, len(rows[i]))]
        return rows

    def get_probability_to_terms(self, y, term):
        a = float(term[1])
        b = float(term[2])
        c = float(term[3])

        if a <= y <= b:
            return round(1 - ((b - y) / (b - a)), TermSetting.ROUND_TO)

        if b <= y <= c:
            return round(1 - ((y - b) / (c - b)), TermSetting.ROUND_TO)

        return 0
