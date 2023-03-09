from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
import sys


def report_generator(strategies, relatory_path, relatory_type):
    for strategy in strategies:
        instance = InventoryRefactor(strategy)
        try:
            report = instance.import_data(relatory_path, relatory_type)
            print(report, end="")
        except ValueError:
            if isinstance(instance, XmlImporter):
                sys.exit("invalid file format")


def main():
    try:
        relatory_path = sys.argv[1]
        relatory_type = sys.argv[2]
        strategies = [CsvImporter, JsonImporter, XmlImporter]
        report_generator(strategies, relatory_path, relatory_type)
    except IndexError:
        print("Verifique os argumentos", file=sys.stderr)

main();
