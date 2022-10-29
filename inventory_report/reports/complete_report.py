import io
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
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
    def ordenate_companies_set(cls, product_spec_list):
        companies = []

        for company in product_spec_list:
            company_name = company["nome_da_empresa"]
            if company_name not in companies:
                companies.append(company_name)
        return companies

    @classmethod
    def companies_products_quantity(cls, product_spec_list):
        companies = {}

        for company in product_spec_list:
            company_name = company["nome_da_empresa"]
            if company_name not in companies:
                companies[company_name] = 1
            else:
                companies[company_name] += 1
        return companies

    @classmethod
    def companies_qt_report(cls, companies_products_quantities, companies):
        report = "Produtos estocados por empresa:\n"
        for company_name in companies:
            product_qt = companies_products_quantities[company_name]
            report += f"- {company_name}: {product_qt}\n"
        return report

    @classmethod
    def generate(cls, products_list):
        simple_report_data = super().generate(products_list)
        companies_products_qt = cls.companies_products_quantity(products_list)
        companies_in_order = cls.ordenate_companies_set(products_list)
        extra_companies_report = cls.companies_qt_report(
            companies_products_qt, companies_in_order
        )

        complete_report = f"{simple_report_data}\n" + extra_companies_report
        with io.StringIO() as my_stream:
            print(complete_report, file=my_stream, end="")
            text = my_stream.getvalue()
            return text
