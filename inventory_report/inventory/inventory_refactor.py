from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.inventory.inventory_iterator import InventoryIterator
from collections.abc import Iterable


class InventoryRefactor(Iterable):
    def __init__(self, import_strategy):
        self.importer = import_strategy
        self.data = []

    def __iter__(self):
        return InventoryIterator(self.data)

    def generate_relatory(self, relatory_type):
        if relatory_type.title() == "Simples":
            return SimpleReport.generate(self.data)
        else:
            return CompleteReport.generate(self.data)

    def import_data(self, path, relatory_type):
        self.data += self.importer.import_data(path)
        return self.generate_relatory(relatory_type)
