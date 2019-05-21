from bling import Api


def test_should_call_get_objects_with_correct_arguments_when_all_filters_are_provided(mocker):
    mock_get_objects = mocker.patch.object(Api, '_get_objects')

    api = Api(api_key='fake-api-key')
    api.get_invoices(
        issued_date=['17/05/2019', '17/05/2019'],
        situation='pago',
        type='S',
    )

    expected_params = {
        'filters': 'dataEmissao[17/05/2019 TO 17/05/2019];situacao[pago];tipo[S]'
    }
    mock_get_objects.assert_called_with(
        'notasfiscais', 'notafiscal', expected_params
    )


def test_should_call_get_objects_with_correct_arguments_when_no_filters_are_provided(mocker):
    mock_get_objects = mocker.patch.object(Api, '_get_objects')

    api = Api(api_key='fake-api-key')
    api.get_invoices()

    expected_params = {}
    mock_get_objects.assert_called_with(
        'notasfiscais', 'notafiscal', expected_params
    )


def test_should_return_correct_content(mocker):
    mock_get_objects = mocker.patch.object(Api, '_get_objects')

    api = Api(api_key='fake-api-key')
    objs = api.get_invoices(['17/05/2019', '17/05/2019'], 1)

    assert objs == mock_get_objects.return_value
