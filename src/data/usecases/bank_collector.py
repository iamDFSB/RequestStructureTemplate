from typing import List, Type

from src.data import BankModel, ApiConsumerInterface
from src.domain import BankCollectorInterface


class BankCollector(BankCollectorInterface):

    def __init__(self, api_consumer: ApiConsumerInterface):
        self.__api_consumer = api_consumer

    def list(self) -> List[BankModel]:
        get_all_banks_response = self.__api_consumer.get_all_banks()
        return [BankModel(**bank) for bank in get_all_banks_response.response]