"""Исключения сервиса."""

class FailedRequestError(ConnectionError):
    """Код возврата страницы - не 200."""

class ServerError(ConnectionError):
    """Ошибка на стороне сервера."""
