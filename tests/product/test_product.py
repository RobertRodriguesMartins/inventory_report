import pytest
from inventory_report.inventory.product import Product


@pytest.fixture
def generate_test_product():
    class ProductTest(Product):
        pass

    return ProductTest


def test_cria_produto(generate_test_product):
    data = ["mm"] * 6
    assert Product(1, *data).id == 1
    with pytest.raises(TypeError) as err:
        assert generate_test_product()
