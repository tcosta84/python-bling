from bling import Api


def test_should_call_make_request_with_correct_arguments(mocker):
    mock_make_request = mocker.patch.object(Api, '_make_request')

    api = Api(api_key='fake-api-key')
    resp = api.get_logistics()

    mock_make_request.assert_called_with('GET', '/logisticas/servicos')


def test_should_return_correct_data(mocker):
    mock_make_request = mocker.patch.object(Api, '_make_request')

    mock_make_request.return_value = {
        'retorno': {
            'logisticas': [[{
                'logistica': {
                    'id_logistica': '57389'
                }
            }]]
        }
    }

    api = Api(api_key='fake-api-key')
    resp = api.get_logistics()

    assert resp == [{'id_logistica': '57389'}]
