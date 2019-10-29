from bling import Api


def test_should_call_get_objects_with_correct_arguments_when_all_filters_are_provided(mocker):
    mock_get_objects = mocker.patch.object(Api, '_get_objects')

    api = Api(api_key='fake-api-key')
    api.get_products(situation='A', type='P')

    expected_params = {'filters': 'tipo[P];situacao[A]'}
    mock_get_objects.assert_called_with(
        'produtos', 'produto', expected_params
    )


def test_should_call_get_objects_with_correct_arguments_when_no_filters_are_provided(mocker):
    mock_get_objects = mocker.patch.object(Api, '_get_objects')

    api = Api(api_key='fake-api-key')
    api.get_products()

    expected_params = {}
    mock_get_objects.assert_called_with(
        'produtos', 'produto', expected_params
    )


def test_should_return_correct_content(mocker):
    mock_get_objects = mocker.patch.object(Api, '_get_objects')

    api = Api(api_key='fake-api-key')
    objs = api.get_products()

    assert objs == mock_get_objects.return_value
