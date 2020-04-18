from bling import Api


def test_should_call_get_objects_with_correct_arguments_when_all_arguments_are_provided(mocker):
    mock_get_objects = mocker.patch.object(Api, '_get_objects')

    api = Api(api_key='fake-api-key')
    api.get_products(
        creation_date=['01/04/2020', '18/04/2020'],
        modification_date=['01/04/2020', '18/04/2020'],
        store_creation_date=['01/04/2020', '18/04/2020'],
        store_modification_date=['01/04/2020', '18/04/2020'],
        situation='A', type='P',
        store_code='8987292029202'
    )

    expected_params = {
        'estoque': 'S', 'imagem': 'N', 'loja': '8987292029202',
        'filters': 'dataInclusao[01/04/2020 TO 18/04/2020];dataAlteracao[01/04/2020 TO 18/04/2020];dataInclusaoLoja[01/04/2020 TO 18/04/2020];dataAlteracaoLoja[01/04/2020 TO 18/04/2020];tipo[P];situacao[A]'
    }
    mock_get_objects.assert_called_with(
        'produtos', 'produto', expected_params
    )


def test_should_call_get_objects_with_default_arguments_when_no_arguments_are_provided(mocker):
    mock_get_objects = mocker.patch.object(Api, '_get_objects')

    api = Api(api_key='fake-api-key')
    api.get_products()

    expected_params = {'estoque': 'S', 'imagem': 'N'}
    mock_get_objects.assert_called_with(
        'produtos', 'produto', expected_params
    )


def test_should_return_correct_content(mocker):
    mock_get_objects = mocker.patch.object(Api, '_get_objects')

    api = Api(api_key='fake-api-key')
    objs = api.get_products()

    assert objs == mock_get_objects.return_value
