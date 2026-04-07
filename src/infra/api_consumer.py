from http import HTTPStatus

import requests
from requests import Request, Response
from typing import Type

from src.data.interfaces.api_consumer_interface import ApiConsumerInterface
from src.infra.models.api_consumer_model import ApiConsumerResponse
from src.errors.http_request_error import HttpRequestError


class ApiConsumer(ApiConsumerInterface):
    @classmethod
    def get_all_banks(cls) -> ApiConsumerResponse:
        req = requests.Request(
            method="GET",
            url=f"https://brasilapi.com.br/api/banks/v1"
        )

        req_prepared = req.prepare()
        response = cls.__send_http_request(req_prepared)
        status_code = response.status_code

        if status_code == HTTPStatus.OK:
            return ApiConsumerResponse(
                status_code=response.status_code,
                request=req,
                response=response.json()
            )

        raise HttpRequestError(status_code=status_code, message=response.json()["message"])


    @classmethod
    def get_bank_by_code(cls, code: int = 1) -> ApiConsumerResponse:
        req = requests.Request(
            method="GET",
            url=f"https://brasilapi.com.br/api/banks/v1/{code}"
        )

        req_prepared = req.prepare()
        response = cls.__send_http_request(req_prepared)
        status_code = response.status_code

        if (status_code >= HTTPStatus.OK) and (status_code <= 299):
            return ApiConsumerResponse(
                status_code=response.status_code,
                request=req,
                response=response.json()
            )

        raise HttpRequestError(status_code=status_code, message=response.json()["message"])


    @classmethod
    def __send_http_request(cls, req_prepared: Type[Request]) -> Response:
        http_session = requests.Session()
        response = http_session.send(req_prepared)
        return response


if __name__ == "__main__":
    consumer = ApiConsumer()
    print(consumer.get_bank_by_code())
