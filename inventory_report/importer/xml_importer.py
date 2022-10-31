from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if ".xml" not in path:
            raise ValueError('Arquivo inválido"')
        products_list = []
        with open(path, mode="rb") as file:
            dict_file = xmltodict.parse(file)
            data = dict_file
            products_list = data["dataset"]["record"]
        return products_list
