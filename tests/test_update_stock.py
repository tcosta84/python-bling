from bling import Api


def test_should_update_stock(mocker):
    mock_update_product = mocker.patch.object(Api, 'update_product')

    code = 'SKU-123'
    qty = 5

    api = Api(api_key='fake-api-key')
    resp = api.update_stock(code, qty)

    expected_xml = '<produto><codigo>SKU-123</codigo><estoque>5</estoque></produto>'
    mock_update_product.assert_called_with(code, expected_xml)

    assert resp == mock_update_product.return_value
