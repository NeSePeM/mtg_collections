import logging
from sys import stdout
from http import HTTPStatus
from logging.handlers import RotatingFileHandler

import requests

from .exceptions import FailedRequestError, ServerError
from .literals import *


logger = logging.getLogger(__name__)
logging.basicConfig(
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=(
        RotatingFileHandler(filename=f'{__file__}.log'),
        logging.StreamHandler(stdout),
    ),
    level=logging.DEBUG,
)


ENDPOINT = 'https://api.scryfall.com/cards/'
HEADERS = {
    ...
}


API_TO_APP_FIELDS = {
    ...
}


def get_api_answer():
    """Подучение ответа API."""
    request_params = dict(
        url=ENDPOINT,
        params={...},
        headers=HEADERS,
    )
    request_params_log = REQUEST_PARAMS.format(**request_params)
    try:
        response = requests.get(**request_params)
    except requests.RequestException as error:
        raise ConnectionError(
            API_FAILED_REQUEST.format(error=error, log=request_params_log)
        )
    if response.status_code != HTTPStatus.OK:
        raise FailedRequestError(
            ENDPOINT_UNREACH.format(url=ENDPOINT, log=request_params_log)
        )

    response = response.json()

    for key in ('code', 'error'):
        if key in response:
            raise ServerError(
                SERVER_ERRORS_KEYS.format(
                    error=response[key],
                    log=request_params_log
                )
            )

    return response


def check_response(response):
    """Валидация ответа API."""
    # if not isinstance(response, dict):
    #     raise TypeError(
    #         RESPONSE_TYPE_ERROR.format(
    #             expected_type=dict,
    #             actual_type=type(response)
    #         )
    #     )
    # if (key := 'homeworks') not in response:
    #     raise KeyError(KEY_ERROR.format(key=key))
    # if not isinstance(homeworks := response['homeworks'], list):
    #     raise TypeError(
    #         VALUE_TYPE_ERROR.format(
    #             key='homeworks',
    #             expected_type=list,
    #             actual_type=type(homeworks)
    #         )
    #     )


def get_cards(data) -> list:
    """Формирование списка карт из ответа API."""
    # if (key := 'status') not in homework:
    #     raise KeyError(KEY_ERROR.format(key=key))
    # if (key := 'homework_name') not in homework:
    #     raise KeyError(KEY_ERROR.format(key=key))
    # if (status := homework['status']) not in HOMEWORK_VERDICTS:
    #     raise ValueError(STATUS_VALUE_ERROR.format(status=status))
    # return UPDATED_STATUS.format(
    #     name=homework['homework_name'],
    #     verdict=HOMEWORK_VERDICTS[status]
    # )


def save_card(cards, choose):
    # try:
    #     data = get_api_answer()
    #     if check_response(data):
    #         cards = parse_status(homework_statuses)
    # except Exception as error:
    #     message = f'Сбой в работе программы: {error}'
    #     print(message)
