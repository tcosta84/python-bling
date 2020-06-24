from bling import Api


def test_should_update_situation(mocker):
    mock_make_request = mocker.patch.object(Api, '_make_request')

    number = '12345'
    situation_id = 7

    api = Api(api_key='fake-api-key')
    resp = api.update_order_situation(number, situation_id)

    xml = '<pedido><idSituacao>%s</idSituacao></pedido>' % situation_id

    mock_make_request.assert_called_with(
        'PUT', '/pedido/%s' % number,
        params={
            'xml': xml
        }
    )

    assert resp == mock_make_request.return_value
