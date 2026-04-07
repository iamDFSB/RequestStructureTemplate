from http import HTTPStatus

from src.infra.api_consumer import ApiConsumer
from src.errors import HttpRequestError


def test_get_bank_by_code(requests_mock):
    code = 1
    requests_mock.get(
        f"https://brasilapi.com.br/api/banks/v1/{code}",
        status_code=HTTPStatus.OK,
        json={'ispb': '00000000', 'name': 'BCO DO BRASIL S.A.', 'code': 1, 'fullName': 'Banco do Brasil S.A.'}
    )
    get_bank_by_code_response = ApiConsumer().get_bank_by_code()
    print(get_bank_by_code_response)

    assert get_bank_by_code_response.request.method == "GET"
    assert get_bank_by_code_response.status_code == HTTPStatus.OK
    assert isinstance(get_bank_by_code_response.response, dict)
    assert get_bank_by_code_response.response.get("name") is not None
    assert get_bank_by_code_response.response["code"] == 1


def test_get_bank_by_invalid_code(requests_mock):
    code = 2
    requests_mock.get(
        url=f"https://brasilapi.com.br/api/banks/v1/{code}",
        status_code=HTTPStatus.NOT_FOUND,
        json={"message": "Código bancário não encontrado", "type": "BANK_CODE_NOT_FOUND"}
    )

    try:
        ApiConsumer().get_bank_by_code(code)
    except HttpRequestError as e:
        print(e)
        assert e.status_code == HTTPStatus.NOT_FOUND
        assert e.message == "Código bancário não encontrado"
    else:
        assert False


def test_get_all_banks():
    get_all_banks_response = ApiConsumer().get_all_banks()
    print(get_all_banks_response)

    assert get_all_banks_response.request.method == "GET"
    assert get_all_banks_response.status_code == HTTPStatus.OK
    assert isinstance(get_all_banks_response.response, list)
