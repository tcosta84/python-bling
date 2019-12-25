from bling import Api


def test_should_update_stock(mocker):
    mock_make_request = mocker.patch.object(Api, '_make_request')

    nf_number = '12345'
    nf_series = '1'
    service_id = '3797312'
    tracking = 'PX0183938391262'

    api = Api(api_key='fake-api-key')
    resp = api.update_tracking_code(nf_number, nf_series, service_id, tracking)

    expected_uri = '/logistica/rastreamento/notafiscal/{}/{}'.format(
        nf_number, nf_series
    )
    expected_xml = '<rastreamentos><rastreamento><id_servico>{}</id_servico><codigo>{}</codigo></rastreamento></rastreamentos>'.format(service_id, tracking)
    mock_make_request.assert_called_with(
        'POST',
        expected_uri,
        data={'xml': expected_xml}
    )

    assert resp == mock_make_request.return_value
