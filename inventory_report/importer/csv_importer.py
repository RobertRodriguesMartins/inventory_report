from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if ".csv" not in path:
            raise ValueError('Arquivo inválido"')
        products_list = []
        with open(path, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            products_data = [row_as_dict for row_as_dict in reader]
            products_list = products_data
        return products_list
