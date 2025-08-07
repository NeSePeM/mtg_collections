ERROR = 'Сбой в работе программы: {error}'
REQUEST_PARAMS = (
    '\nПараметры запроса: url={url}, headers={headers}, params={params}'
)
API_FAILED_REQUEST = (
    'Сбой при запросе к API Scryfall. '
    '{error} {log}'
)
ENDPOINT_UNREACH = 'Эндпоинт {url} недоступен. {log}'
SERVER_ERRORS_KEYS = 'Аварийный ключ в ответе сервера. {error} {log}'
RESPONSE_TYPE_ERROR = (
    'Ответ сервера не является '
    '{expected_type}, а {actual_type}.'
)
VALUE_TYPE_ERROR = (
    'Значение ключа {key} не является '
    '{expected_type}, а {actual_type}.'
)
KEY_ERROR = 'Ключ {key} отсутствует.'
ANSWER_VALUE_ERROR = (
    'Неожиданный ответ, обнаруженный в ответе API: {status}'
)
