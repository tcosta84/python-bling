from bling import Api


def test_should_update_product(mocker):
    mock_make_request = mocker.patch.object(Api, '_make_request')

    api = Api(api_key='fake-api-key')
    code = 'SKU-123'
    xml = '<produto></produto>'
    resp = api.update_product(code, xml)

    mock_make_request.assert_called_with(
        'POST', '/produto/{}'.format(code),
        data={
            'xml': xml
        }
    )

    assert resp == mock_make_request.return_value
