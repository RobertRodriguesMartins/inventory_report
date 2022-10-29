from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import xmltodict
import json


class Inventory:
    @classmethod
    def generate_relatory(cls, relatory_type, products_list):
        if relatory_type.title() == "Simples":
            return SimpleReport.generate(products_list)
        else:
            return CompleteReport.generate(products_list)

    @classmethod
    def import_data(cls, path, relatory_type):
        products_list = []
        if ".json" in path:
            with open(path, mode="r") as file:
                products_data = json.load(file)
                products_list = products_data
        elif ".csv" in path:
            with open(path, mode="r", newline="") as file:
                reader = csv.DictReader(file)
                products_data = [row_as_dict for row_as_dict in reader]
                products_list = products_data
        else:
            with open(path, mode="rb") as file:
                dict_file = xmltodict.parse(file)
                data = dict_file
                products_list = data["dataset"]["record"]

        return cls.generate_relatory(relatory_type, products_list)
