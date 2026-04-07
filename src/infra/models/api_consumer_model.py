from dataclasses import dataclass
from typing import Union

from requests import Request


@dataclass
class ApiConsumerResponse:
    status_code: int
    request: Request
    response: Union[list, dict]