from src.infra.api_consumer import ApiConsumer
from src.data import BankModel, BankCollector



def test_bank_collector_list():
    bank_list_collector = BankCollector(api_consumer=ApiConsumer())
    list_of_banks = bank_list_collector.list()

    assert isinstance(list_of_banks, list)
    assert isinstance(list_of_banks[0], BankModel)

