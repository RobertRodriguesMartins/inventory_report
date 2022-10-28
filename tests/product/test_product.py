import pytest
from inventory_report.inventory.product import Product


@pytest.fixture
def generate_test_product():
    class ProductTest(Product):
        pass

    return ProductTest


def test_cria_produto(generate_test_product):
    atributes = [
        "nome_do_produto",
        "nome_da_empresa",
        "data_de_fabricacao",
        "data_de_validade",
        "numero_de_serie",
        "instrucoes_de_armazenamento",
    ]

    data = [f"d{i}" for i, d in enumerate(atributes)]
    product = Product(1, *data)
    assert product.id == 1
    assert isinstance(product.id, int)

    for index, pr in enumerate(atributes):
        assert hasattr(product, pr)
        assert getattr(product, pr) == data[index]
        assert isinstance(getattr(product, pr), str)

    with pytest.raises(TypeError):
        assert generate_test_product()
