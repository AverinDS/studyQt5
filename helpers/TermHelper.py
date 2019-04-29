class TermParser:
    def get_terms(self):
        terms = []
        with open("TERMS.csv") as file:
            for line in file.readlines():
                terms.append(line.split("|"))
        return terms
