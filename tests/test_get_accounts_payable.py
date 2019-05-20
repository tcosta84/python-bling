from unittest import mock

from bling import Api


def test_should_call_get_objects_with_correct_arguments_when_all_filters_are_provided(mocker):
    mock_get_objects = mocker.patch.object(Api, '_get_objects')

    api = Api(api_key='fake-api-key')
    api.get_accounts_payable(
        issued_date=['17/05/2019', '17/05/2019'],
        due_date=['17/05/2019', '17/05/2019'],
        situation='pago'
    )

    expected_params = {
        'filters': 'dataEmissao[17/05/2019 TO 17/05/2019];dataVencimento[17/05/2019 TO 17/05/2019];situacao[pago]'
    }
    mock_get_objects.assert_called_with(
        'contaspagar', 'contapagar', expected_params
    )


def test_should_return_correct_content(mocker):
    mock_get_objects = mocker.patch.object(Api, '_get_objects')

    expected_resp = mock.Mock()
    mock_get_objects.return_value = expected_resp

    api = Api(api_key='fake-api-key')
    accounts = api.get_accounts_payable(['17/05/2019', '17/05/2019'], 'pago')

    assert accounts == expected_resp
