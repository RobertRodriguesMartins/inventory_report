import io
import sys
from inventory_report.inventory.product import Product


def test_relatorio_produto():
    expected_report = """O produto farinha fabricado em 01-05-2021 por Farinini com validade até 02-06-2023 precisa ser armazenado ao abrigo de luz."""
    product = Product(
        1,
        "farinha",
        "Farinini",
        "01-05-2021",
        "02-06-2023",
        "any",
        "ao abrigo de luz",
    )
    my_test_stream = io.StringIO()
    with io.StringIO() as my_stream:
        print(product, file=my_stream, end="")
        print(expected_report, file=my_test_stream, end="")
        assert my_stream.getvalue() == my_test_stream.getvalue()

    my_test_stream.close()
