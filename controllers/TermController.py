from helpers.TermHelper import TermHelper


class TermController:
    termHelper = TermHelper()

    # [[descr, begin, top, end]]
    def get_data(self, filename):
        return self.termHelper.get_terms(filename)

    def save_data(self, list_terms, filename):
        self.termHelper.save_terms(list_terms, filename)

