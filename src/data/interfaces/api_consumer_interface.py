from abc import ABC, abstractmethod

from src.infra.models.api_consumer_model import ApiConsumerResponse


class ApiConsumerInterface(ABC):
    @classmethod
    @abstractmethod
    def get_all_banks(cls) -> ApiConsumerResponse:
        raise Exception("Method Not Implemented")

    @classmethod
    @abstractmethod
    def get_bank_by_code(cls, code: int = 1) -> ApiConsumerResponse:
        raise Exception("Method Not Implemented")