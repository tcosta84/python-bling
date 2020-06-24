from bling import Api


def test_should_call_make_request_with_correct_arguments(mocker):
    mock_make_request = mocker.patch.object(Api, '_make_request')

    module = 'Vendas'

    api = Api(api_key='fake-api-key')
    resp = api.get_situations(module)

    mock_make_request.assert_called_with(
        'GET',
        '/situacao/%s' % module
    )


def test_should_return_correct_data(mocker):
    mock_make_request = mocker.patch.object(Api, '_make_request')

    mock_make_request.return_value = {
        'retorno': {
            'situacoes': [{
                'situacao': {
                    'id': '9',
                    'idHerdado': '0',
                    'nome': 'Atendido',
                    'cor': '#3FB57A'
                }
            }]
        }
    }

    module = 'Vendas'

    api = Api(api_key='fake-api-key')
    resp = api.get_situations(module)

    assert resp == [{
        'situacao': {
            'id': '9',
            'idHerdado': '0',
            'nome': 'Atendido',
            'cor': '#3FB57A'
        }
    }]
