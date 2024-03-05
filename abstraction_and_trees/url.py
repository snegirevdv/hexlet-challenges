# https://ru.hexlet.io/challenges/python_data_abstraction_url_exercise

from typing import Any
import urllib.parse
from urllib.parse import ParseResult as Url


def make(url: str) -> Url:
    return urllib.parse.urlparse(url)


def get_scheme(data: Url) -> str:
    return data.scheme


def set_scheme(data: Url, scheme: str) -> str:
    return data._replace(scheme=scheme)


def get_host(data: Url) -> str:
    return data.netloc


def set_host(data: Url, host: str) -> str:
    return data._replace(netloc=host)


def get_path(data: Url) -> str:
    return data.path


def set_path(data: Url, path: str) -> str:
    return data._replace(path=path)


def get_query(data: Url) -> str:
    return data.query


def set_query(data: Url, query: str):
    return data._replace(query=query)


def get_params(data: Url) -> dict[str, Any]:
    query = get_query(data)
    return urllib.parse.parse_qs(query)


def get_query_param(data: Url, param_name: str, default=None):
    params = get_params(data)
    return params.get(param_name, [default])[0]


def set_query_param(data: Url, key: str, value: Any):
    params = get_params(data)

    if value:
        params[key] = [value]
    else:
        params.pop(key, None)

    new_query = urllib.parse.urlencode(params, doseq=True)
    return set_query(data, new_query)


def to_string(data: Url) -> str:
    return urllib.parse.urlunparse(data)
