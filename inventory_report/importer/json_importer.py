from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if ".json" not in path:
            raise ValueError('Arquivo inválido"')
        products_list = []
        with open(path, mode="r") as file:
            products_data = json.load(file)
            products_list = products_data
        return products_list
