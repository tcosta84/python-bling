from bling import Api


def test_should_return_correct_data(mocker):
    mock_make_request = mocker.patch.object(Api, '_make_request')

    api = Api(api_key='fake-api-key')
    resp = api.issue_invoice(12345, 1)

    assert resp == mock_make_request.return_value


def test_should_call_make_request_with_sendEmail_param(mocker):
    mock_make_request = mocker.patch.object(Api, '_make_request')

    api = Api(api_key='fake-api-key')
    api.issue_invoice(12345, 1)

    mock_make_request.assert_called_with(
        'POST', '/notafiscal',
        data={
            'number': 12345,
            'serie': 1,
            'sendEmail': 'true'
        }
    )


def test_should_issue_invoice_but_dont_send_email(mocker):
    mock_make_request = mocker.patch.object(Api, '_make_request')

    api = Api(api_key='fake-api-key')
    resp = api.issue_invoice(12345, 1, send_email=False)

    mock_make_request.assert_called_with(
        'POST', '/notafiscal',
        data={
            'number': 12345,
            'serie': 1,
            'sendEmail': 'false'
        }
    )
