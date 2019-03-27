from helpers.FolderParser import FolderParser


class TableController:
    folder_parser = FolderParser()

    def get_table_data(self):
        return self.folder_parser.parse()
