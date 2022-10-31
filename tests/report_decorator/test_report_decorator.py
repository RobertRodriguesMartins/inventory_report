from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport
import pytest


@pytest.fixture
def data():
    invalid_fabrication_date = [
        {
            "id": 1,
            "nome_do_produto": "teste",
            "nome_da_empresa": "Alfa_Test",
            "data_de_fabricacao": "2021-01-01",
            "data_de_validade": "2022-02-02",
            "numero_de_serie": "HA1-13",
            "instrucoes_de_armazenamento": "NA",
        }
    ] * 3
    valid_validation_date = [
        {
            "id": 2,
            "nome_do_produto": "teste2",
            "nome_da_empresa": "Alfa_Test2",
            "data_de_fabricacao": "2022-01-01",
            "data_de_validade": "2023-01-01",
            "numero_de_serie": "HA1-13",
            "instrucoes_de_armazenamento": "NA",
        }
    ] * 2

    products_list = invalid_fabrication_date + valid_validation_date
    return list(products_list)


def test_decorar_relatorio(data):
    green_phrases = [
        "Data de fabricação mais antiga",
        "Data de validade mais próxima",
        "Empresa com mais produtos",
    ]
    products_list = data
    colored_report = ColoredReport(SimpleReport)
    report = colored_report.generate(products_list)
    report_test = report.split("\n")
    for index, phrase in enumerate(report_test):
        should_be_green, simple_report = phrase.split(":")
        assert f"\033[32m{green_phrases[index]}" == should_be_green
        try:
            assert "\033[36m" in simple_report
        except AssertionError:
            assert "\033[31m" in simple_report
