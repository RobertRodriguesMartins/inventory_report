from datetime import date
import io
from inventory_report.inventory.product import Product


class DateManager:
    @classmethod
    def calculate_older_fabrication_date(cls, product_spec_list):
        fabrication_dates = [
            date.fromisoformat(product_info["data_de_fabricacao"])
            for product_info in product_spec_list
            if "data_de_fabricacao" in product_info
        ]
        older_date = ""
        for i in fabrication_dates:
            if not isinstance(older_date, date):
                older_date = i
            elif i < older_date:
                older_date = i
        return older_date

    @classmethod
    def calculate_closest_validation_date(cls, product_spec_list):
        products_validation_date = [
            date.fromisoformat(product_info["data_de_validade"])
            for product_info in product_spec_list
        ]
        valid_dates = [
            valid_date
            for valid_date in products_validation_date
            if date.today() < valid_date
        ]

        closest_date = ""
        curr_date_ordinal = date.today().toordinal()
        for i in valid_dates:
            ordinal_diff = i.toordinal() - curr_date_ordinal
            if not isinstance(closest_date, tuple):
                closest_date = (i, ordinal_diff)
            elif closest_date[1] > ordinal_diff:
                closest_date = (i, ordinal_diff)
        return closest_date[0]

    @classmethod
    def calculate_companies_products_quantity(cls, product_spec_list):
        companies = {}

        for company in product_spec_list:
            company_name = company["nome_da_empresa"]
            if company_name not in companies:
                companies[company_name] = 1
            else:
                companies[company_name] += 1

        company_with_most_sales = ("", 0)
        for company_name, product_qt in companies.items():
            if company_with_most_sales[1] < product_qt:
                company_with_most_sales = (company_name, product_qt)
        return company_with_most_sales[0]


class SimpleReport(Product):
    def __init__(
        self,
        id,
        nome_do_produto,
        nome_da_empresa,
        data_de_fabricacao,
        data_de_validade,
        numero_de_serie,
        instrucoes_de_armazenamento,
    ):
        super().__init__(
            id,
            nome_do_produto,
            nome_da_empresa,
            data_de_fabricacao,
            data_de_validade,
            numero_de_serie,
            instrucoes_de_armazenamento,
        )

    @classmethod
    def generate(cls, products_list):
        fabrication_date = DateManager.calculate_older_fabrication_date(
            products_list
        )
        validation_date = DateManager.calculate_closest_validation_date(
            products_list
        )
        biggest_company = DateManager.calculate_companies_products_quantity(
            products_list
        )
        with io.StringIO() as my_stream:
            print(
                f"Data de fabricação mais antiga: {fabrication_date}\n"
                f"Data de validade mais próxima: {validation_date}\n"
                f"Empresa com mais produtos: {biggest_company}",
                file=my_stream,
                end="",
            )
            return my_stream.getvalue()
