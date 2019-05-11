from helpers.FolderParser import FolderParser
from helpers.TermHelper import TermHelper


class TermInGraphicController:
    terms = []
    table_data = []
    termHelper = TermHelper()
    folder_parser = FolderParser()

    def get_table_data(self, filename):
        rows = []
        self.terms = self.termHelper.get_terms()
        points_x, points_y = self.folder_parser.get_points_from_file_by_filename(filename=filename)
        for i in range(0, len(points_x)):
            row = [points_x[i], points_y[i]]
            for term in self.terms:
                row.append(self.get_probability_to_terms(points_y[i], term))
            rows.append(row)
        term_names = [term[0] for term in self.terms]
        return rows, term_names


    def get_probability_to_terms(self, y, term):
        a = float(term[1])
        b = float(term[2])
        c = float(term[3])

        if a <= y <= b:
            return 1 - ((b - y) / (b - a))

        if b <= y <= c:
            return 1 - ((y - b) / (c - b))

        return 0
