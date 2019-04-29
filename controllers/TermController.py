from helpers.TermHelper import TermHelper


class TermController:
    termHelper = TermHelper()

    # [[descr, begin, top, end]]
    def get_data(self):
        return self.termHelper.get_terms()

    def save_data(self, list_terms):
        self.termHelper.save_terms(list_terms)

