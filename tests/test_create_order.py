from bling import Api


def test_should_create_order_without_nfe(mocker):
    mock_make_request = mocker.patch.object(Api, '_make_request')

    api = Api(api_key='fake-api-key')
    xml = '<pedido></pedido>'
    resp = api.create_order(xml)

    mock_make_request.assert_called_with(
        'POST', '/pedido',
        data={
            'xml': xml,
            'gerarnfe': False
        }
    )

    assert resp == mock_make_request.return_value


def test_should_create_order_with_nfe(mocker):
    mock_make_request = mocker.patch.object(Api, '_make_request')

    api = Api(api_key='fake-api-key')
    xml = '<pedido></pedido>'
    resp = api.create_order(xml, gen_nfe=True)

    mock_make_request.assert_called_with(
        'POST', '/pedido',
        data={
            'xml': xml,
            'gerarnfe': True
        }
    )

    assert resp == mock_make_request.return_value
