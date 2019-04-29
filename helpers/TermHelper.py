from helpers.ConstHolder import TermSetting
import os


class TermHelper:
    def get_terms(self):
        terms = []

        if not os.path.exists(TermSetting.FILENAME):
            return terms

        with open(TermSetting.FILENAME) as file:
            for line in file.readlines():
                terms.append(line.split(TermSetting.SEPARATOR))
        return terms

    def save_terms(self, terms):
        new_file = open(TermSetting.FILENAME, 'w')
        for i in range(0, len(terms)):
            line = ""
            for j in range(0, len(terms[i])):
                line += terms[i][j] + TermSetting.SEPARATOR
            new_file.write(line + '\n')
        new_file.close()
