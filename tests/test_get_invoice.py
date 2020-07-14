from bling import Api


def test_should_call_make_request_with_correct_arguments(mocker):
    mock_make_request = mocker.patch.object(Api, '_make_request')

    api = Api(api_key='fake-api-key')
    resp = api.get_invoice(12345, 1)

    mock_make_request.assert_called_with('GET', '/notafiscal/12345/1')


def test_should_return_correct_data(mocker):
    mock_make_request = mocker.patch.object(Api, '_make_request')

    resp = mock_make_request.return_value = {
        'retorno': {
            'notasfiscais': [
                {
                    'notafiscal': {
                        'numero': '12345',
                        'tipo': 'E'
                    }
                },
                {
                    'notafiscal': {
                        'numero': '12345',
                        'tipo': 'S'
                    }
                },
            ]
        }
    }

    api = Api(api_key='fake-api-key')
    invoice = api.get_invoice(12345, 1)

    assert invoice == resp['retorno']['notasfiscais'][1]['notafiscal']


def test_should_return_correct_data_for_incoming_invoice(mocker):
    mock_make_request = mocker.patch.object(Api, '_make_request')

    resp = mock_make_request.return_value = {
        'retorno': {
            'notasfiscais': [
                {
                    'notafiscal': {
                        'numero': '12345',
                        'tipo': 'E'
                    }
                },
                {
                    'notafiscal': {
                        'numero': '12345',
                        'tipo': 'S'
                    }
                },
            ]
        }
    }

    api = Api(api_key='fake-api-key')
    invoice = api.get_invoice(12345, 1, 'E')

    assert invoice == resp['retorno']['notasfiscais'][0]['notafiscal']
