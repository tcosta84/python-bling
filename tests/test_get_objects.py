from unittest.mock import call

from bling import Api


def test_should_call_make_requests_at_least_2_times(mocker):
    mock_make_request = mocker.patch.object(Api, '_make_request')

    mock_make_request.side_effect = [
        {
            'retorno': {
                'notasfiscais': [{
                    'notafiscal': {
                        'numero': '12345'
                    }
                }]
            }
        },
        {
            'retorno': {
                'erros': []
            }
        }
    ]

    api = Api(api_key='fake-api-key')
    api._get_objects('notasfiscais', 'notafiscal')

    assert mock_make_request.call_count == 2

    expected_calls = [
        call('GET', '/notasfiscais/page=1', params=None),
        call('GET', '/notasfiscais/page=2', params=None)
    ]
    mock_make_request.assert_has_calls(expected_calls, any_order=True)


def test_should_return_correct_data(mocker):
    mock_make_request = mocker.patch.object(Api, '_make_request')

    mock_make_request.side_effect = [
        {
            'retorno': {
                'notasfiscais': [{
                    'notafiscal': {
                        'numero': '12345'
                    }
                }]
            }
        },
        {
            'retorno': {
                'erros': []
            }
        }
    ]

    api = Api(api_key='fake-api-key')
    objs = api._get_objects('notasfiscais', 'notafiscal')

    assert objs == [{'numero': '12345'}]
