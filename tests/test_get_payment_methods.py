from bling import Api


def test_should_call_make_request_with_correct_arguments(mocker):
    mock_make_request = mocker.patch.object(Api, '_make_request')

    api = Api(api_key='fake-api-key')
    resp = api.get_payment_methods()

    mock_make_request.assert_called_with('GET', '/formaspagamento')


def test_should_return_correct_data(mocker):
    mock_make_request = mocker.patch.object(Api, '_make_request')

    mock_make_request.return_value = {
        "retorno": {
            "formaspagamento": [{
                "formapagamento": {
                    "id": "1",
                    "descricao": "Dinheiro",
                    "codigoFiscal": "1",
                    "padrao": "0",
                    "situacao": 1
                }
            }]
        }
    }

    api = Api(api_key='fake-api-key')
    resp = api.get_payment_methods()

    # import ipdb;ipdb.set_trace()

    assert resp == [{
        "id": "1",
        "descricao": "Dinheiro",
        "codigoFiscal": "1",
        "padrao": "0",
        "situacao": 1
    }]
