from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv


class Inventory:
    @classmethod
    def import_data(cls, path, relatory_type):
        products_list = []
        with open(path, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            products_data = [row_as_dict for row_as_dict in reader]
            products_list = products_data
        if relatory_type.title() == "Simples":
            return SimpleReport.generate(products_list)
        elif relatory_type.title() == "Completo":
            return CompleteReport.generate(products_list)
