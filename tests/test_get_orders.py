from bling import Api


def test_should_call_get_objects_with_correct_arguments_when_all_filters_are_provided(mocker):
    mock_get_objects = mocker.patch.object(Api, '_get_objects')

    api = Api(api_key='fake-api-key')
    api.get_orders(
        issued_date=['17/05/2019', '17/05/2019'],
        change_date=['17/05/2019', '17/05/2019'],
        expected_date=['17/05/2019', '17/05/2019'],
        situation_id=1,
        contact_id=1,
    )

    expected_params = {
        'filters': 'dataEmissao[17/05/2019 TO 17/05/2019];dataAlteracao[17/05/2019 TO 17/05/2019];dataPrevista[17/05/2019 TO 17/05/2019];idSituacao[1];idContato[1]'
    }
    mock_get_objects.assert_called_with(
        'pedidos', 'pedido', expected_params
    )


def test_should_call_get_objects_with_correct_arguments_when_no_filters_are_provided(mocker):
    mock_get_objects = mocker.patch.object(Api, '_get_objects')

    api = Api(api_key='fake-api-key')
    api.get_orders()

    expected_params = {}
    mock_get_objects.assert_called_with(
        'pedidos', 'pedido', expected_params
    )


def test_should_return_correct_content(mocker):
    mock_get_objects = mocker.patch.object(Api, '_get_objects')

    api = Api(api_key='fake-api-key')
    objs = api.get_orders()

    assert objs == mock_get_objects.return_value
