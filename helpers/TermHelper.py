import os

from helpers.ConstHolder import TermSetting, GeneratorSetting


class TermHelper:
    def get_terms(self, filename):
        terms = []

        if not os.path.exists(TermSetting.FOLDERNAME + "/" + filename):
            return terms

        with open(TermSetting.FOLDERNAME + "/" + filename) as file:
            for line in file.readlines():
                terms.append(line.split(TermSetting.SEPARATOR))
        return terms

    def save_terms(self, terms, filename):
        if not os.path.exists(TermSetting.FOLDERNAME):
            os.makedirs(TermSetting.FOLDERNAME)

        new_file = open(TermSetting.FOLDERNAME + "/" + filename + ".txt", 'w')
        for i in range(0, len(terms)):
            line = ""
            for j in range(0, len(terms[i])):
                line += terms[i][j] + TermSetting.SEPARATOR
            new_file.write(line + '\n')
        new_file.close()

    def generate_terms(self, max_value, min_value, filename):
        size_interval = (max_value + abs(min_value)) / (TermSetting.COUNT_OF_TERMS-1)
        index = min_value
        terms = []

        while len(terms) != TermSetting.COUNT_OF_TERMS:
            one_term = []
            begin = index - size_interval
            high = index
            end = index + size_interval
            one_term.append("Term" + str(len(terms)))
            one_term.append(str(begin))
            one_term.append(str(high))
            one_term.append(str(end))
            terms.append(one_term)
            index += size_interval

        self.save_terms(terms, filename)

