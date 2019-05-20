import pytest
from unittest import mock

from requests.exceptions import HTTPError, RequestException

from bling import Api, ApiError


def test_should_call_make_request_with_default_arguments(mocker):
    mock_request = mocker.patch('bling.base.requests.Session.request')

    api = Api(api_key='fake-api-key')
    api._make_request('GET', '/pedido')

    mock_request.assert_called_with(
        'GET', 'https://bling.com.br/Api/v2/pedido/json/?apikey=fake-api-key',
        params=None, data=None
    )


def test_should_call_make_request_with_data_argument(mocker):
    mock_request = mocker.patch('bling.base.requests.Session.request')

    api = Api(api_key='fake-api-key')
    api._make_request('POST', '/pedido', data={})

    mock_request.assert_called_with(
        'POST', 'https://bling.com.br/Api/v2/pedido/json/?apikey=fake-api-key',
        params=None, data={}
    )


def test_should_call_make_request_with_params_argument(mocker):
    mock_request = mocker.patch('bling.base.requests.Session.request')

    api = Api(api_key='fake-api-key')
    api._make_request('POST', '/pedido', params={})

    mock_request.assert_called_with(
        'POST', 'https://bling.com.br/Api/v2/pedido/json/?apikey=fake-api-key',
        params={}, data=None
    )


def test_should_return_correct_data(mocker):
    mock_request = mocker.patch('bling.base.requests.Session.request')

    api = Api(api_key='fake-api-key')
    resp = api._make_request('GET', '/pedido')

    assert resp == mock_request.return_value.json.return_value


def test_should_raise_ApiError_when_a_HTTPError_occurs(mocker):
    mock_request = mocker.patch('bling.base.requests.Session.request')

    request = mock.Mock()
    response = mock.Mock()
    mock_request.side_effect = HTTPError(
        request=request,
        response=response
    )

    api = Api(api_key='fake-api-key')

    with pytest.raises(ApiError) as e:
        api._make_request('GET', '/pedido')

    assert e.value.request == request
    assert e.value.response == response


def test_should_raise_ApiError_when_a_RequestException_occurs(mocker):
    mock_request = mocker.patch('bling.base.requests.Session.request')

    request = mock.Mock()
    mock_request.side_effect = RequestException(
        request=request,
    )

    api = Api(api_key='fake-api-key')

    with pytest.raises(ApiError) as e:
        api._make_request('GET', '/pedido')

    assert e.value.request == request
    assert e.value.response == None
